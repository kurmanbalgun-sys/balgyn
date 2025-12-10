from abc import ABC, abstractmethod
import uuid
from datetime import datetime

class BaseEntity(ABC):
    def _init_(self):
        self._id = str(uuid.uuid4())
        self._created_at = datetime.utcnow()

    @property
    def id(self):
        return self._id

    @property
    def created_at(self):
        return self._created_at