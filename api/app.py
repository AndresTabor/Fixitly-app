from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate


from config.bd_config import SQLALCHEMY_DATABASE_URI, db

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
migrate = Migrate(app, db)
CORS(app)
from models import User  

@app.route('/')
def hello_world():
    return 'Hello, World 2!'

if __name__ == '__main__':
    app.run(debug=True)
