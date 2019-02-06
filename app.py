from flask import Flask
from webapp.main.model.models import db
from webapp.main.config.postgres import postgres
from webapp.main.config.config import app_config
from webapp.main.controller.user import user_api

app = Flask(__name__)

DB_URI = postgres

app.config['SQLALCHEMY_DATABASE_URI'] = postgres
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.register_blueprint(user_api)

db.init_app(app)

if __name__ == '__main__':
    '# Change to production to hide messages from filthy rebel scum'
    app.config.from_object(app_config['development'])
    app.run()
