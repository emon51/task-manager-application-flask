from flask import Blueprint, render_template, request, redirect, url_for
from models import db
from models.task import Task

web_bp = Blueprint('web', __name__)

@web_bp.route('/')
def home():
    """Home page"""
    return render_template('home.html')


@web_bp.route('/tasks')
def tasks():
    """Tasks listing page"""
    status_filter = request.args.get('status', '')
    
    # Build query
    query = Task.query
    
    # Apply status filter
    if status_filter:
        query = query.filter_by(status=status_filter)
    
    # Get all tasks ordered by created_at
    tasks = query.order_by(Task.created_at.desc()).all()
    
    return render_template('tasks.html', tasks=tasks, status_filter=status_filter)


@web_bp.route('/tasks/<int:task_id>/mark-done', methods=['POST'])
def mark_done(task_id):
    """Mark a task as done"""
    task = Task.query.get_or_404(task_id)
    task.status = 'done'
    db.session.commit()
    return redirect(url_for('web.tasks'))