import os
from flask import Blueprint
from flask.cli import with_appcontext
import click
import requests
import xmltodict
import json
import datetime
import re

from ..models.skill import Skill
from ..models.skillProject import SkillProject
from ..models.db import db


commands_bp = Blueprint('runner', __name__,cli_group='runner')

@commands_bp.cli.command('start')
@with_appcontext
@click.argument('source',required=False)
def start(source):
	if source==None:
		response = requests.get(os.getenv('UPWORKSFEEDURL'))
		api_access_token=get_api_access_token()
		if response.status_code==200:
			response_dict = xmltodict.parse(response.text, encoding='utf-8') 
			projects = response_dict['rss']['channel']['item']
			for project in projects:
				data1 = re.findall(r"Budget\<\/b\>:\s+\$(\d+)",project['description'])
				data2 = re.findall(r"Hourly Range\<\/b\>:\s+\$(\d+)",project['description'])
				project_type="Hourly"
				project_cost=30
				if len(data1)>0 :
					project_type="Fixed"
					project_cost=data1[0]
				if len(data2)>0 :
					project_cost=data2[0]
				skills = get_skills(project['description'],api_access_token)
				for skill in skills:
					exisitng_skill= db.session.query(Skill).filter(Skill.name==skill).first()
					if exisitng_skill is None:
						skill_db = Skill(name=skill)
						db.session.add(skill_db)
						db.session.flush()
						skillproject = SkillProject(
											skill_id=skill_db.id,
											price=project_cost,
											project_at=datetime.datetime.strptime(project['pubDate'],'%a, %d %b %Y %H:%M:%S %z'),
											project_type=project_type
										)
						db.session.add(skillproject)
						db.session.commit()

def get_api_access_token():
	response = requests.post(
		'https://auth.emsicloud.com/connect/token',
		headers={
			'Content-Type':'application/x-www-form-urlencoded'
		},
		data={
			'client_id':os.environ.get('SKILL_CLIENT_ID'),
			'client_secret':os.environ.get('SKILL_CLIENT_SECRET'),
			'grant_type':'client_credentials',
			'scope':'emsi_open'
		}
	)
	if response.status_code==200:
		response = json.loads(response.text)
		return response['access_token']
	else:
		return None

def get_skills(text,access_token):
	response = requests.post(
		'https://emsiservices.com/skills/versions/latest/extract?language=en',
		headers={
			'Content-Type':'application/json',
			'Authorization':'Bearer '+access_token
		},
		data=json.dumps({"text":text,"confidenceThreshold": 0.8})
	)
	if response.status_code==200:
		response = json.loads(response.text)
		skills=[]
		for data in response['data']:
			skills.append(data['skill']['name'])
		return skills
	else:
		return []