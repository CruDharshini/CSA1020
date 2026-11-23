from flask import Flask, redirect, render_template_string, request, url_for

app = Flask(__name__)
tasks = []

PAGE = """
<!doctype html><title>Flask To-Do</title>
<h1>My To-Do List</h1>
<form method="post"><input name="task" required placeholder="Enter a task">
<button type="submit">Add Task</button></form>
<ul>{% for task in tasks %}<li>{{ task }}</li>{% endfor %}</ul>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        task = request.form.get("task", "").strip()
        if task:
            tasks.append(task)
        return redirect(url_for("index"))
    return render_template_string(PAGE, tasks=tasks)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
