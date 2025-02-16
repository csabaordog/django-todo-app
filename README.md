# To Do App - Django

This is a basic To Do Application in Django, with a React frontend. The application allows users to create, update, and delete tasks. Each task has a title, description, due date, and status.

## Features

- **Create Tasks**: Add new tasks with a title, description, and due date.
- **Update Tasks**: Edit existing tasks to update their details.
- **Delete Tasks**: Remove tasks that are no longer needed.
- **Task Status**: Mark tasks as completed or pending.
- **Smart Suggestions**: Get task suggestions based on previous tasks.

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/csabaordog/django-todo-app.git
    cd django-todo-app
    ```

2. **Backend Setup**:
    - Create a virtual environment and activate it:
        ```sh
        python3 -m venv venv
        source venv/bin/activate
        ```
    - Install the required packages:
        ```sh
        pip install -r requirements.txt
        ```
    - Run migrations:
        ```sh
        python manage.py migrate
        ```
    - Start the Django development server:
        ```sh
        python manage.py runserver
        ```

3. **Frontend Setup**:
    - Navigate to the frontend directory:
        ```sh
        cd todo_frontend
        ```
    - Install the required packages:
        ```sh
        npm install
        ```
    - Start the React development server:
        ```sh
        npm start
        ```

## Usage

- Open your browser and navigate to `http://localhost:8000` to use the application.
