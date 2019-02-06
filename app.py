from flask import Flask
from webapp.main.controller.user import user_api
from webapp.main.config.postgres import postgres
from webapp.main.config.config import app_config

app = Flask(__name__)

app.register_blueprint(user_api)

app.config['SQLALCHEMY_DATABASE_URI'] = postgres


if __name__ == '__main__':
    # Change to production to hide messages from filthy rebel scum
    app.config.from_object(app_config['development'])
    app.run()
