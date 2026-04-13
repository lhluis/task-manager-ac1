from flask import Flask, render_template, request, redirect
import json

app = Flask(__name__)

DB = "tasks.json"


def load_tasks():
    try:
        with open(DB, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_tasks(tasks):
    with open(DB, "w") as f:
        json.dump(tasks, f)


@app.route("/")
def index():
    tasks = load_tasks()
    return render_template("index.html", tasks=tasks)


@app.route("/add", methods=["POST"])
def add_task():
    tasks = load_tasks()
    title = request.form["title"].strip()

    if title:
        tasks.append({"title": title})
        save_tasks(tasks)

    return redirect("/")


@app.route("/delete/<int:task_id>", methods=["POST"])
def delete_task(task_id):
    tasks = load_tasks()

    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
        save_tasks(tasks)

    return redirect("/")


@app.route("/edit/<int:task_id>", methods=["GET"])
def edit_task(task_id):
    tasks = load_tasks()

    if 0 <= task_id < len(tasks):
        return render_template("edit.html", task=tasks[task_id], task_id=task_id)

    return redirect("/")


@app.route("/edit/<int:task_id>", methods=["POST"])
def update_task(task_id):
    tasks = load_tasks()
    new_title = request.form["title"].strip()

    if 0 <= task_id < len(tasks) and new_title:
        tasks[task_id]["title"] = new_title
        save_tasks(tasks)

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)