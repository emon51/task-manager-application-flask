from flask import Flask
from config import Config
from models import db
from models.task import Task

app = Flask(__name__)
app.config.from_object(Config)

# Initialize database
db.init_app(app)

@app.route('/')
def home():
    return "Welcome to Task Manager Application"

# Create database tables
with app.app_context():
    db.create_all()
    print("Database tables created!")

if __name__ == '__main__':
    app.run(debug=True)