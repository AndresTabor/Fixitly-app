from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from config.bd_config import SQLALCHEMY_DATABASE_URI, db

jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    
    db.init_app(app)
    jwt.init_app(app)
    CORS(app)
    
    with app.app_context():
        
        from . import models
        from routes.auth_route import auth_bp
        app.register_blueprint(auth_bp, url_prefix='/auth')
  
        db.create_all()  
    
    return app