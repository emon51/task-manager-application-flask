from flask import Blueprint, request, jsonify
from models import db
from models.task import Task
from datetime import datetime

api_bp = Blueprint('api', __name__, url_prefix='/api')

@api_bp.route('/tasks', methods=['POST'])
def create_task():
    """Create a new task"""
    data = request.get_json()
    
    # Validation: title is required
    if not data or 'title' not in data or not data['title'].strip():
        return jsonify({'error': 'Title is required'}), 400
    
    # Validation: status must be valid
    valid_statuses = ['todo', 'in_progress', 'done']
    status = data.get('status', 'todo')
    if status not in valid_statuses:
        return jsonify({'error': 'Invalid status. Must be: todo, in_progress, or done'}), 400
    
    # Parse due_date if provided
    due_date = None
    if 'due_date' in data and data['due_date']:
        try:
            due_date = datetime.strptime(data['due_date'], '%Y-%m-%d').date()
        except ValueError:
            return jsonify({'error': 'Invalid due_date format. Use YYYY-MM-DD'}), 400
    
    # Create task
    task = Task(
        title=data['title'].strip(),
        description=data.get('description', ''),
        status=status,
        due_date=due_date
    )
    
    db.session.add(task)
    db.session.commit()
    
    return jsonify(task.to_dict()), 201