from flask import Flask
from config import app_config
from app.api.routes.views.political import version1 as party
from app.api.routes.views.office import version1 as office

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    #
    app.register_blueprint(party)
    app.register_blueprint(office)
    return app
