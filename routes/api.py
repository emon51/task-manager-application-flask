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


@api_bp.route('/tasks', methods=['GET'])
def list_tasks():
    """List all tasks with optional filters"""
    # Get query parameters
    status_filter = request.args.get('status')
    search_query = request.args.get('q')
    sort_by = request.args.get('sort', 'created_at')
    
    # Start with base query
    query = Task.query
    
    # Apply status filter
    if status_filter:
        valid_statuses = ['todo', 'in_progress', 'done']
        if status_filter not in valid_statuses:
            return jsonify({'error': 'Invalid status filter'}), 400
        query = query.filter_by(status=status_filter)
    
    # Apply search filter
    if search_query:
        search_pattern = f'%{search_query}%'
        query = query.filter(
            db.or_(
                Task.title.like(search_pattern),
                Task.description.like(search_pattern)
            )
        )
    
    # Apply sorting
    if sort_by == 'due_date':
        query = query.order_by(Task.due_date.asc())
    else:
        query = query.order_by(Task.created_at.desc())
    
    tasks = query.all()
    return jsonify([task.to_dict() for task in tasks]), 200


@api_bp.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    """Get a single task by ID"""
    task = Task.query.get(task_id)
    
    if not task:
        return jsonify({'error': 'Task not found'}), 404
    
    return jsonify(task.to_dict()), 200

@api_bp.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    """Update an existing task"""
    task = Task.query.get(task_id)
    
    if not task:
        return jsonify({'error': 'Task not found'}), 404
    
    data = request.get_json()
    
    if not data:
        return jsonify({'error': 'No data provided'}), 400
    
    # Update title if provided
    if 'title' in data:
        if not data['title'].strip():
            return jsonify({'error': 'Title cannot be empty'}), 400
        task.title = data['title'].strip()
    
    # Update description if provided
    if 'description' in data:
        task.description = data['description']
    
    # Update status if provided
    if 'status' in data:
        valid_statuses = ['todo', 'in_progress', 'done']
        if data['status'] not in valid_statuses:
            return jsonify({'error': 'Invalid status. Must be: todo, in_progress, or done'}), 400
        task.status = data['status']
    
    # Update due_date if provided
    if 'due_date' in data:
        if data['due_date']:
            try:
                task.due_date = datetime.strptime(data['due_date'], '%Y-%m-%d').date()
            except ValueError:
                return jsonify({'error': 'Invalid due_date format. Use YYYY-MM-DD'}), 400
        else:
            task.due_date = None
    
    db.session.commit()
    return jsonify(task.to_dict()), 200


@api_bp.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    """Delete a task"""
    task = Task.query.get(task_id)
    
    if not task:
        return jsonify({'error': 'Task not found'}), 404
    
    db.session.delete(task)
    db.session.commit()
    
    return jsonify({'message': 'Task deleted successfully'}), 200