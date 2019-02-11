from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from webapp.main.config.config import app_config
from webapp import blueprint
from webapp.main import engine, create_app
from webapp import blueprint

app = create_app()

app.register_blueprint(blueprint)

manager = Manager(app)
migrate = Migrate(app, engine)

manager.add_command('engine', MigrateCommand)


@manager.command
def run():
    app.run()


if __name__ == '__main__':
    '# Change to production to hide messages from filthy rebel scum'
    app.config.from_object(app_config['development'])
    manager.run()
