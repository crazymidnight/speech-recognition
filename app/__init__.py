from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from .client_app import client_bp

app = Flask(__name__, static_folder="../dist/")
app.register_blueprint(client_bp)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models
