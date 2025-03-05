from models.job_model import Job
from config.bd_config import db

class JobService:
    @staticmethod
    def create_job(client_id, description, estimated_price=None):
        job = Job(
            client_id=client_id,
            description=description,
            estimated_price=estimated_price
        )
        db.session.add(job)
        db.session.commit()
        return job