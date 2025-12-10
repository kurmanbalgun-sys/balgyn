from .task import SimpleTask, RecurringTask
from .enums import Priority

class TaskFactory:
    def create_task(self, title, description="", assignee=None, project=None, priority=Priority.MEDIUM, recurring=False, **kwargs):
        if recurring:
            return RecurringTask(title, description=description, assignee=assignee, project=project, priority=priority, **kwargs)
        else:
            return SimpleTask(title, description=description, assignee=assignee, project=project, priority=priority)