from .celery import app
from celery import Task
from celery.exceptions import Ignore
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


class PowerOfTwoTask(Task):
    def __init__(self):
        self.number = 1

    def run(self):
        if self.number == 1024:
            raise Ignore()

        self.number *= 2
        return self.number


t = PowerOfTwoTask()
app.register_task(t)
