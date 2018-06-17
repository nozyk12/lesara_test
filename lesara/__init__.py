from flask import Flask
from flask_mysqldb import MySQL
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object('lesara.settings')
db = SQLAlchemy(app)

migrate = Migrate(app, db)

import lesara.views
import lesara.models
import lesara.commands