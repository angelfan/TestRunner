import os
import warnings
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand
from werkzeug.contrib.fixers import ProxyFix


from src.app import create_app, db

# app = create_app(os.getenv('FLASK_CONFIG') or 'default')
app = create_app('development')
manager = Manager(app)
migrate = Migrate(app, db)
app.wsgi_app = ProxyFix(app.wsgi_app)


def init():
    pass


with app.app_context():
    init()
    # cache.clear()

if __name__ == '__main__':
    manager.run()