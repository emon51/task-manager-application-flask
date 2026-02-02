from flask import Flask
from config import Config
from models import db
from models.task import Task
from routes.api import api_bp
from routes.web import web_bp

app = Flask(__name__)
app.config.from_object(Config)

# Initialize database
db.init_app(app)

# Register blueprints
app.register_blueprint(api_bp)
app.register_blueprint(web_bp)

# Create database tables
with app.app_context():
    db.create_all()
    print("Database tables created!")

if __name__ == '__main__':
    app.run(debug=True)