from flask import Flask, render_template, request, redirect
import json

app = Flask(__name__)

DB = "tasks.json"


def load_tasks():
    with open(DB, "r") as f:
        return json.load(f)


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
    title = request.form["title"]

    tasks.append({"title": title})

    save_tasks(tasks)

    return redirect("/")


app.run(debug=True)