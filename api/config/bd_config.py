import os

from flask_sqlalchemy import SQLAlchemy

SQLALCHEMY_DATABASE_URI = f"postgresql://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@db:5432/{os.getenv('POSTGRES_DB')}"
SQLALCHEMY_TRACK_MODIFICATIONS = False

db = SQLAlchemy()