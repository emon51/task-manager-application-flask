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

