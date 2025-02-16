# To Do App - Django

This is a basic To Do Application in Django, with a React frontend. The application allows users to create, update, and delete tasks. Each task has a title, description, creation date, due date, and status.

## Features

- **Create Tasks**: Add new tasks with a title, description, and due date.
- **Update Tasks**: Edit existing tasks to update their details.
- **Delete Tasks**: Remove tasks that are no longer needed.
- **Task Status**: Mark tasks as completed or pending.



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
    - Build the project:
        ```sh
        npm run build
        ```

## Usage

- Open your browser and navigate to `http://localhost:8000` to use the application.


## API Documentation

### `GET /task/<pk>/`
Retrieve a single task by its ID.

**Request:**
- Method: `GET`
- URL: `/task/<pk>/`
- URL Parameters:
  - `pk` (integer): The primary key of the task to retrieve.

**Response:**
- Status: `200 OK`
  - Body: JSON object containing the task data.
- Status: `404 Not Found`
  - Body: Empty.

```sh
curl -X GET http://localhost:8000/task/1/
```

### `GET /task-list/`
Retrieve all tasks with optional filtering and sorting.

**Request:**
- Method: `GET`
- URL: `/task-list/`
- Query Parameters:
  - `status` (string, optional): Filter tasks by status (e.g., `PENDING`, `IN_PROGRESS`, `COMPLETED`).
  - `due_date` (string, optional): Filter tasks by due date in `YYYY-MM-DD` format.
  - `sort_by` (string, optional): Sort tasks by `created_at` or `due_date`.
  - `order` (string, optional): Sort order, either `asc` (ascending) or `desc` (descending). Default is `asc`.

**Response:**
- Status: `200 OK`
  - Body: JSON array containing a list of all tasks.

#### Example Usage
```sh
# Get all tasks
curl -X GET http://localhost:8000/task/task-list/

# Get tasks with status 'PENDING'
curl -X GET "http://localhost:8000/task/task-list/?status=PENDING"

# Get tasks with due date '2025-12-31'
curl -X GET "http://localhost:8000/task/task-list/?due_date=2025-12-31"

# Get tasks sorted by due date in descending order
curl -X GET "http://localhost:8000/task/task-list/?sort_by=due_date&order=desc"
```

### `POST /task-create/`
Create a new task.

**Request:**
- Method: `POST`
- URL: `/task-create/`
- Body: JSON object containing the task data.
  - `title` (string): The title of the task.
  - `description` (string): The description of the task.
  - `due_date` (string): The due date of the task in `YYYY-MM-DD` format.
  - `status` (string): The status of the task (e.g., `PENDING`, `IN_PROGRESS`, `COMPLETED`).

**Response:**
- Status: `201 Created`
  - Body: JSON object containing the created task data.
- Status: `400 Bad Request`
  - Body: JSON object containing validation errors.

```sh
curl -X POST http://localhost:8000/task/task-create/ -H "Content-Type: application/json" -d '{
  "title": "New Task",
  "description": "This is a new task.",
  "due_date": "2025-12-31",
  "status": "PENDING"
}'
```


### `PUT /task-update/<pk>/`
Update an existing task by its ID.

**Request:**
- Method: `PUT`
- URL: `/task-update/<pk>/`
- URL Parameters:
  - `pk` (integer): The primary key of the task to update.
- Body: JSON object containing the updated task data.
    - `id` (number): The id of the task.
    - `title` (string): The title of the task.
    - `description` (string): The description of the task.
    - `created_at` (string): The date of creation.
    - `due_date` (string): The due date of the task in `YYYY-MM-DD` format.
    - `status` (string): The status of the task (e.g., `PENDING`, `IN_PROGRESS`, `COMPLETED`).

**Response:**
- Status: `200 OK`
  - Body: JSON object containing the updated task data.
- Status: `400 Bad Request`
  - Body: JSON object containing validation errors.
- Status: `404 Not Found`
  - Body: Empty.

```sh
curl -X PUT http://localhost:8000/task/task-update/1/ -H "Content-Type: application/json" -d '{
  "title": "Updated Task Title",
  "description": "Updated description",
  "due_date": "2025-12-31",
  "status": "COMPLETED"
}'
```

### `DELETE /task-delete/<pk>/`
Delete a task by its ID.

**Request:**
- Method: `DELETE`
- URL: `/task-delete/<pk>/`
- URL Parameters:
  - `pk` (integer): The primary key of the task to delete.

**Response:**
- Status: `204 No Content`
  - Body: Empty.
- Status: `404 Not Found`
  - Body: Empty.

```sh
curl -X DELETE http://localhost:8000/task/task-delete/1/
```