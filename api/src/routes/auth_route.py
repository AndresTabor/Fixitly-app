from flask import Blueprint, request, jsonify
from src.models import User, Role
from src.config.bd_config import db
from src.models.schemas.user import UserCreate, UserLogin
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = UserCreate(**request.json)
    if User.query.filter_by(email=data.email).first():
        return jsonify({"msg": "Email ya registrado"}), 400
    user = User(
        email=data.email,
        password=generate_password_hash(data.password),
        name=data.name,
        role=Role[data.role]
    )
    db.session.add(user)
    db.session.commit()
    return jsonify({"msg": "Usuario creado"}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = UserLogin(**request.json)
    user = User.query.filter_by(email=data.email).first()
    if user and check_password_hash(user.password, data.password):
        token = create_access_token(identity=user.id)
        return jsonify({"token": token}), 200
    return jsonify({"msg": "Credenciales inválidas"}), 401