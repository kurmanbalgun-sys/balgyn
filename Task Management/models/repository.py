class TaskRepository:
    _instance = None

    def _init_(self):
        if TaskRepository._instance is not None:
            raise Exception("Use get_instance()")
        self._tasks = []
        self._projects = []
        self._users = []

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = TaskRepository()
        return cls._instance

    def add_task(self, task):
        self._tasks.append(task)

    def get_tasks(self):
        return list(self._tasks)

    def add_project(self, project):
        self._projects.append(project)

    def get_projects(self):
        return list(self._projects)

    def add_user(self, user):
        self._users.append(user)

    def get_users(self):
        return list(self._users)

    def get_user_by_username(self, username):
        for u in self._users:
            if u.username == username:
                return u
        return None

    def get_project_by_name(self, name):
        for p in self._projects:
            if p.name == name:
                return p
        return None