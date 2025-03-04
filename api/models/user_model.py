from datetime import datetime, timezone
from config.bd_config import db
from enum import Enum as PyEnum 

class User_Role(str, PyEnum):
    ADMIN = "admin"
    CLIENT = "client"
    PROFESSIONAL = "professional"

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key = True)
    fullname = db.Column(db.String(120), unique = False, nullable = False)
    email = db.Column(db.String(120), unique = True, nullable = False)
    password = db.Column(db.String(120), unique = False, nullable = False)
    location = db.Column(db.String(120), unique = False, nullable = False)
    image = db.Column(db.String(200), unique = False, nullable = False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False, default=True)
    date_at = db.Column(db.DateTime, unique = False, nullable = False, default=datetime.now(timezone.utc))
    role = db.Column(db.Enum(User_Role, name="user_role_enum"), nullable=False, default=User_Role.CLIENT)

    def __repr__(self):
        return f'<User {self.fullname}>'
    

    def to_dict(self):
        return {
            "id": self.id,
            "fullname": self.fullname,
            "email": self.email,
            "location": self.location,
            "image": self.image,
            "is_active": self.is_active,
            "date_at": self.date_at.isoformat(),
        }
