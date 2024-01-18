# Latest Skills in demand

An application to scan upworks for latest projects extract skills required and show it in a dashboard to understand the skills in demand. can be extended to other channels.
## Tech Stack

**Scrapper:** Python,  Flask cli , click , Atom Feed 

**Database:** MySql , PostGres , Sqlite

~**Server:** Flask, sqlalchamy~

~**WEB UI:**:Reactjs,TailwindCSS~

~**Mobile app:** React Native~


## Installation
1) Clone the repo checkout as master.
2) Change to the repo directory.
2) Copy .env.sample to .env and update the details like db details and upworks feed url.
3) Get skills api credentials from https://docs.lightcast.dev/apis/skills and update the .env file.
4) Create a virtual env and install requirements.
5) Run env FLASK_APP=wsgi.py python -m flask runner start to start the runner.
6) Schedule it using cron to run repeatedly.
    
## Roadmap

- add a way to filter out duplicate posts so that skills frequency is not getting polluted
- apis to generate the dashboard.
- api documentation
- Dashboard UI in Reactjs.
- Mobile App in React Native.
- Browser Extension for chrome.
- Notifications to send periodic digest of the skills.


## License

[GPL3](https://choosealicense.com/licenses/lgpl-3.0/)
