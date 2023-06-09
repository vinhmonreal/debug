from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import sys
print(sys.executable)
app = Flask(__name__)
app.config.from_object(Config)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.blueprints.main import bp as main_bp
app.register_blueprint(main_bp)
from app.blueprints.auth import bp as auth_bp
app.register_blueprint(auth_bp)

from app.blueprints.auth import models