from repositories.base_repository import BaseRepository
from db.connection import Database
from models.task import Task

class TaskRepository(BaseRepository):
    def __init__(self, db: Database):
        super().__init__(db, "Task")

    def get_all_tasks(self):
        rows = self.fetch_all()
        return [Task(**r) for r in rows]

    def get_task(self, task_id):
        row = self.fetch_by_id("taskID", task_id)
        return Task(**row) if row else None

    def create_task(self, data: dict):
        conn = self.db.get_connection()
        cur = conn.cursor()
        sql = """INSERT INTO Task (title, description, taskType, status, assignedVolunteerID, createdBy, relatedRequestID)
                 VALUES (%s,%s,%s,%s,%s,%s,%s)"""
        cur.execute(sql, (data.get("title"), data.get("description"), data.get("taskType", "other"), data.get("status", "unassigned"), data.get("assignedVolunteerID"), data.get("createdBy"), data.get("relatedRequestID")))
        conn.commit()
        last = cur.lastrowid
        cur.close()
        return last

    def update_task(self, task_id, data: dict):
        conn = self.db.get_connection()
        cur = conn.cursor()
        sql = """UPDATE Task SET title=%s, description=%s, taskType=%s, status=%s, assignedVolunteerID=%s, createdBy=%s, relatedRequestID=%s WHERE taskID=%s"""
        cur.execute(sql, (data.get("title"), data.get("description"), data.get("taskType"), data.get("status"), data.get("assignedVolunteerID"), data.get("createdBy"), data.get("relatedRequestID"), task_id))
        conn.commit()
        rc = cur.rowcount
        cur.close()
        return rc

    def delete_task(self, task_id):
        conn = self.db.get_connection()
        cur = conn.cursor()
        cur.execute("DELETE FROM Task WHERE taskID=%s", (task_id,))
        conn.commit()
        rc = cur.rowcount
        cur.close()
        return rc
