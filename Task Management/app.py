from flask import Flask, render_template, request, redirect, url_for
from models.user import User
from models.project import Project
from models.factory import TaskFactory
from models.repository import TaskRepository
from models.enums import TaskStatus, Priority

app = Flask(__name__)

repo = TaskRepository.get_instance()

# demo seed
u1 = User("alice", "Alice Johnson")
u2 = User("bob", "Bob Ivanov")
repo.add_user(u1); repo.add_user(u2)

p1 = Project("Website", "Website redesign")
p2 = Project("Mobile App", "Mobile app v1.0")
repo.add_project(p1); repo.add_project(p2)

# create sample tasks via factory
task_f = TaskFactory()
t1 = task_f.create_task("Design homepage", assignee=u1, project=p1, priority=Priority.HIGH)
t2 = task_f.create_task("Setup CI", assignee=u2, project=p1, priority=Priority.MEDIUM)
t3 = task_f.create_task("Daily backup", assignee=u1, project=p2, priority=Priority.LOW, recurring=True)
repo.add_task(t1); repo.add_task(t2); repo.add_task(t3)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users')
def users():
    return render_template('users.html', users=repo.get_users())

@app.route('/projects')
def projects():
    return render_template('projects.html', projects=repo.get_projects())

@app.route('/tasks')
def tasks():
    return render_template('tasks.html', tasks=repo.get_tasks(), statuses=TaskStatus, priorities=Priority)

@app.route('/tasks/add', methods=['POST'])
def add_task():
    title = request.form['title']
    desc = request.form.get('description','')
    assignee_id = request.form.get('assignee')
    project_id = request.form.get('project')
    priority = request.form.get('priority', 'MEDIUM')
    recurring = request.form.get('recurring') == 'on'

    assignee = repo.get_user_by_username(assignee_id) if assignee_id else None
    project = repo.get_project_by_name(project_id) if project_id else None
    task = TaskFactory().create_task(title, description=desc, assignee=assignee, project=project, priority=Priority[priority], recurring=recurring)
    repo.add_task(task)
    return redirect(url_for('tasks'))

if __name__ == '__main__':
    app.run(debug=True)