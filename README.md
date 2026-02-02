# Flask Task Manager

A simple task management application built with Flask that provides both REST API and web interface for managing tasks.

## Features

- Create, read, update and delete tasks via REST API
- View tasks in a web interface
- Filter tasks by status (todo, in_progress, done)
- Mark tasks as done directly from the UI
- SQLite database with SQLAlchemy ORM
- Environment-based configuration

## Tech Stack

- **Backend**: Flask
- **Database**: SQLite3 with SQLAlchemy ORM
- **Frontend**: HTML, CSS
- **Configuration**: python-dotenv

## Project Structure
```
task-manager/
├── app.py                   # Application entry point
├── templates/
│   ├── base.html            # Base template
│   ├── home.html            # Home page
│   └── tasks.html           # Tasks listing page
├── static/
│   └── style.css            # Stylesheet
├── data/
│   └── tasks.db             # SQLite database (auto-generated)
├── config/
│   └── __init__.py          # App configuration
├── models/
│   ├── __init__.py          # Database initialization
│   └── task.py              # Task model
├── routes/
│   ├── __init__.py
│   ├── api.py               # API endpoints
│   └── web.py               # Web routes
├── .env                     # Environment variables
├── .env.example             # Example environment file
├── .gitignore               # Git ignore file
├── requirements.txt         # Python dependencies
└── README.md                # README.md file
```

## Installation

### 1. Clone the repository or download the zip file of this project
```bash
git clone https://github.com/emon51/task-manager-application-flask.git
```

### 2. Create virtual environment
```bash
python3 -m venv venv
```

### 3. Activate virtual environment
**On Windows:**
```bash
venv\Scripts\activate
```
**On Mac/Linux:**
```bash
source venv/bin/activate
```

### 4. Create a directory named '**data**' in the root directory
```bash
mkdir data
```

### 5. Rename **.env.example** file to **.env**
```bash
mv .env.example .env
```

### 6. Install dependencies
```bash
pip install -r requirements.txt
```


### 7. Run the application
```bash
python3 app.py
```

The application will be available at 
```bash
http://127.0.0.1:5000/
```


## API Endpoints

### Create Task
```bash
POST /api/tasks
Content-Type: application/json

{
  "title": "Buy milk",
  "description": "2 liters",
  "status": "todo",
  "due_date": "2026-02-05"
}

# Response: 201 Created
{
  "id": 1,
  "title": "Buy milk",
  "description": "2 liters",
  "status": "todo",
  "created_at": "2026-01-30",
  "due_date": "2026-02-05"
}
```

### List Tasks
```bash
GET /api/tasks
GET /api/tasks?status=todo
GET /api/tasks?q=milk
GET /api/tasks?sort=due_date

# Response: 200 OK
[
  {
    "id": 1,
    "title": "Buy milk",
    "description": "2 liters",
    "status": "todo",
    "created_at": "2026-01-30",
    "due_date": "2026-02-05"
  }
]
```

### Get Single Task
```bash
GET /api/tasks/1

# Response: 200 OK
{
  "id": 1,
  "title": "Buy milk",
  ...
}

# Response: 404 Not Found
{
  "error": "Task not found"
}
```

### Update Task
```bash
PUT /api/tasks/1
Content-Type: application/json

{
  "title": "Buy organic milk",
  "status": "in_progress",
  "due_date": "2026-02-10"
}

# Response: 200 OK
{
  "id": 1,
  "title": "Buy organic milk",
  "status": "in_progress",
  ...
}
```

### Delete Task
```bash
DELETE /api/tasks/1

# Response: 200 OK
{
  "message": "Task deleted successfully"
}
```

## API Usage Examples

### Using cURL

**Create a task:**
```bash
curl -X POST http://127.0.0.1:5000/api/tasks \
  -H "Content-Type: application/json" \
  -d '{"title":"Buy groceries","description":"Milk, bread, eggs","due_date":"2026-02-05"}'
```

**List all tasks:**
```bash
curl http://127.0.0.1:5000/api/tasks
```

**Filter by status:**
```bash
curl http://127.0.0.1:5000/api/tasks?status=todo
```

**Search tasks:**
```bash
curl http://127.0.0.1:5000/api/tasks?q=groceries
```

**Update a task:**
```bash
curl -X PUT http://127.0.0.1:5000/api/tasks/1 \
  -H "Content-Type: application/json" \
  -d '{"status":"done"}'
```

**Delete a task:**
```bash
curl -X DELETE http://127.0.0.1:5000/api/tasks/1
```

### Using Postman

1. Create a new request
2. Set method (GET, POST, PUT, DELETE)
3. Enter URL: `http://127.0.0.1:5000/api/tasks`
4. For POST/PUT: Set Headers `Content-Type: application/json`
5. For POST/PUT: Add JSON body in the Body tab (raw)
6. Click Send

## Task Model

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | Integer | Auto | Primary key |
| title | String | Yes | Task title |
| description | Text | No | Task description |
| status | String | No | todo, in_progress, or done (default: todo) |
| created_at | DateTime | Auto | Creation timestamp |
| due_date | Date | No | Due date (YYYY-MM-DD) |

## Validation

- **Title**: Required, cannot be empty
- **Status**: Must be one of: `todo`, `in_progress`, `done`
- **Due Date**: Must be in format `YYYY-MM-DD`
- Invalid data returns `400 Bad Request`
- Non-existent task ID returns `404 Not Found`

## Web Interface

- **Home Page**:
```bash
http://127.0.0.1:5000/
```
- **Tasks List**: 
```bash
http://127.0.0.1:5000/tasks
``` 
  - View all tasks in a table
  - Filter by status using dropdown
  - Mark tasks as done with a button

## Database

The application uses SQLite database stored in `data/tasks.db`. The database is automatically created on first run.

To reset the database, simply delete the `tasks.db` file from **data** directory and restart the application.

## Development

**Enable debug mode** (already enabled in development):
```python
app.run(debug=True)
```

**View logs**: The application prints database initialization messages and any errors to the console.

## License

This project is created for educational purposes

