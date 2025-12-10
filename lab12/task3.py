# task3_logger.py
from abc import ABC, abstractmethod
from datetime import datetime

class Logger(ABC):
    @abstractmethod
    def log_info(self, message):
        pass

    @abstractmethod
    def log_error(self, message):
        pass


class ConsoleLogger(Logger):
    def log_info(self, message):
        print(f"[INFO] {datetime.now()} — {message}")

    def log_error(self, message):
        print(f"[ERROR] {datetime.now()} — {message}")


class FileLogger(Logger):
    def __init__(self, filename="logs.txt"):
        self.filename = filename

    def _write(self, text):
        with open(self.filename, "a", encoding="utf-8") as f:
            f.write(text + "\n")

    def log_info(self, message):
        self._write(f"[INFO] {datetime.now()} — {message}")

    def log_error(self, message):
        self._write(f"[ERROR] {datetime.now()} — {message}")


if __name__ == "__main__":
    console = ConsoleLogger()
    file_logger = FileLogger()

    console.log_info("Система запущена.")
    console.log_error("Произошла ошибка!")

    file_logger.log_info("Запись в файл прошла успешно.")
    file_logger.log_error("Ошибка сохранена в лог.")
