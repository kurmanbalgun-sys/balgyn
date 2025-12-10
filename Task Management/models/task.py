from .base import BaseEntity
from .enums import TaskStatus, Priority
from abc import ABC, abstractmethod
from datetime import datetime, timedelta

class TaskBase(BaseEntity, ABC):
    def _init_(self, title: str, description: str = "", assignee=None, project=None, priority: Priority = Priority.MEDIUM):
        super()._init_()
        self._title = title
        self._description = description
        self._assignee = assignee
        self._project = project
        self._status = TaskStatus.TODO
        self._priority = priority
        self._due_date = None

    # encapsulation
    @property
    def title(self): return self._title
    @property
    def description(self): return self._description
    @property
    def assignee(self): return self._assignee
    @property
    def project(self): return self._project
    @property
    def status(self): return self._status
    @property
    def priority(self): return self._priority
    @property
    def due_date(self): return self._due_date

    def set_due_date(self, dt):
        self._due_date = dt

    def assign(self, user):
        self._assignee = user

    def change_status(self, status):
        if not isinstance(status, TaskStatus):
            raise ValueError("status must be TaskStatus")
        self._status = status

    @abstractmethod
    def work(self):
        """Полиморфная операция: разные таски работают по-разному"""
        pass

    def _repr_(self):
        return f"Task({self._title}, status={self._status})"

class SimpleTask(TaskBase):
    def _init_(self, *args, **kwargs):
        super()._init_(*args, **kwargs)

    def work(self):
        # простая реализация работы над задачей
        self._status = TaskStatus.IN_PROGRESS
        # ... do stuff
        self._status = TaskStatus.DONE
        return f"SimpleTask '{self._title}' completed."

class RecurringTask(TaskBase):
    def _init_(self, interval_days=1, *args, **kwargs):
        super()._init_(*args, **kwargs)
        self._interval_days = interval_days
        self._last_run = None

    def work(self):
        self._last_run = datetime.utcnow()
        self._status = TaskStatus.DONE
        # reschedule
        self._due_date = datetime.utcnow() + timedelta(days=self._interval_days)
        return f"RecurringTask '{self._title}' ran at {self._last_run} next due {self._due_date}."