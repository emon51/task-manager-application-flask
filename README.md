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

The application will be available at `http://127.0.0.1:5000/`

