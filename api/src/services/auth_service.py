from src.models.user_model import User, User_Role
from src.config.bd_config import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token

class AuthService:
    @staticmethod
    def register(email, password, name, role):
        if User.query.filter_by(email=email).first():
            raise ValueError("Email ya registrado")
        user = User(
            email=email,
            password=generate_password_hash(password),
            name=name,
            role=User_Role[role]
        )
        db.session.add(user)
        db.session.commit()
        return user

    @staticmethod
    def login(email, password):
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            token = create_access_token(identity=user.id)
            return token
        raise ValueError("Credenciales inválidas")