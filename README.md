# Task Manager - AC1

This project was developed for the Software Project course.

## Description

Task Manager is a simple web application that allows users to add and view tasks.

The goal of this project is to demonstrate a basic system architecture with:

* Frontend
* Backend
* Database

## Technologies Used

* Python
* Flask
* HTML
* CSS
* JSON (as database)

## Project Structure

task_manager
│
├── app.py
├── tasks.json
├── static
│   └── style.css
└── templates
└── index.html

## Features

* Add new tasks
* List tasks
* Edit existing tasks
* Delete tasks
* Mark tasks as completed (with visual feedback)
* Progress counter showing "X of Y tasks completed" with animated progress bar
* Asynchronous updates via Fetch API (no page reload when completing a task)

## How the "Complete Task" Feature Works

Each task has a completion state stored in the JSON database. When the user
clicks the **"Concluir"** button, the browser sends an asynchronous request
(AJAX) to the Flask server using the Fetch API, without reloading the page.
The server updates the task's status and responds with the new state and
updated statistics in JSON format.

The interface reflects the change instantly: the completed task is crossed
out and highlighted in green, the button switches to **"Feito ✓"**, and both
the counter and the progress bar at the top are updated in real time. If
JavaScript is disabled, the system falls back to a traditional form
submission, ensuring full compatibility.

## How to Run

1. Install Flask

pip install flask

2. Run the application

python app.py

3. Open in the browser

http://127.0.0.1:5000

## Author

Luis Henrique
