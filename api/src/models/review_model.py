from src.config.bd_config import db

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    job_id = db.Column(db.Integer, db.ForeignKey('job.id'), nullable=False)
    rating = db.Column(db.Integer, nullable=False)  
    comment = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=db.func.now())

    def __repr__(self):
        return f'<Review {self.id}>'
    
    def to_dict(self):
        return {
            "id": self.id,
            "job_id": self.job_id,
            "rating": self.rating,
            "comment": self.comment,
            "created_at": self.created_at.isoformat()
        }