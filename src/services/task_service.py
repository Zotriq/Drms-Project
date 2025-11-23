from repositories.task_repository import TaskRepository
from services.base_service import BaseService

class TaskService(BaseService):
    def __init__(self, repo: TaskRepository):
        super().__init__(repo)

    def list_tasks(self):
        return self.repo.get_all_tasks()

    def get_task(self, task_id):
        t = self.repo.get_task(task_id)
        if not t:
            raise ValueError("Task not found")
        return t

    def create_task(self, payload):
        return self.repo.create_task(payload)

    def update_task(self, task_id, payload):
        rc = self.repo.update_task(task_id, payload)
        if rc == 0:
            raise ValueError("Task not found or nothing changed")
        return rc

    def delete_task(self, task_id):
        rc = self.repo.delete_task(task_id)
        if rc == 0:
            raise ValueError("Task not found")
        return rc
