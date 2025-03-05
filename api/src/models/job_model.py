from datetime import datetime, timezone
from src.config.bd_config import db

class Job(db.Model):
    __tablename__ = "jobs"
    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    freelancer_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    description = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(50), default="pending") 
    estimated_price = db.Column(db.Float)
    final_price = db.Column(db.Float)
    created_at = db.Column(db.DateTime, unique = False, nullable = False, default=datetime.now(timezone.utc))

    def __repr__(self):
        return f'<Job {self.id}>'
    
    def to_dict(self):
        return {
            "id": self.id,
            "client_id": self.client_id,
            "freelancer_id": self.freelancer_id,
            "description": self.description,
            "status": self.status,
            "estimated_price": self.estimated_price,
            "final_price": self.final_price,
            "created_at": self.created_at.isoformat()
        }   
