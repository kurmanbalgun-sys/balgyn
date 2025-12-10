from .base import BaseEntity

class Project(BaseEntity):
    def _init_(self, name: str, description: str = ""):
        super()._init_()
        self._name = name
        self._description = description

    @property
    def name(self):
        return self._name

    @property
    def description(self):
        return self._description

    def _repr_(self):
        return f"Project({self._name})"