"""Initialize Flask app."""
from flask import Flask
from apiflask import APIFlask
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask_migrate import Migrate
from dotenv import load_dotenv

load_dotenv()


def create_app():
    """Construct the core application."""
    app = APIFlask(__name__)
    CORS(app)
    app.config.from_object("config.Config")
    app.config['API_PATH']=app.instance_path
    JWTManager(app)
    with app.app_context():
        from .models.db import db
        db.init_app(app)
        from .models.user import db as user_db
        from .models.skill import db as skill_db
        from .models.skillProject import db as skillproject_db
        Migrate(app, skill_db)
        Migrate(app, skillproject_db)
        Migrate(app, user_db)
        from .commands.runner import commands_bp
        from .views.dashboard import dashboard_bp
        app.register_blueprint(dashboard_bp, url_prefix='/')
        app.register_blueprint(commands_bp, cli_group='runner')
        db.create_all()  # Create database tables for our data models
        return app
