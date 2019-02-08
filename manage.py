from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from webapp.main.config.postgres import postgres
from webapp.main.config.config import app_config
from webapp.main.controller.user import user_api
from webapp.main import engine, create_app

DB_URI = postgres
app = create_app()

app.register_blueprint(user_api)


manager = Manager(app)
migrate = Migrate(app, engine)

manager.add_command('engine', MigrateCommand)


if __name__ == '__main__':
    '# Change to production to hide messages from filthy rebel scum'
    app.config.from_object(app_config['development'])
    app.run()
    manager.run()
