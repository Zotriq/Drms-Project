from repositories.base_repository import BaseRepository
from db.connection import Database
from models.feedback import Feedback

class FeedbackRepository(BaseRepository):
    def __init__(self, db: Database):
        super().__init__(db, "Feedback")

    def get_all_feedback(self):
        rows = self.fetch_all()
        return [Feedback(**r) for r in rows]

    def get_feedback(self, feedback_id):
        row = self.fetch_by_id("feedbackID", feedback_id)
        return Feedback(**row) if row else None

    def create_feedback(self, data: dict):
        conn = self.db.get_connection()
        cur = conn.cursor()
        sql = "INSERT INTO Feedback (requestID, victimID, rating, comments) VALUES (%s,%s,%s,%s)"
        cur.execute(sql, (data.get("requestID"), data.get("victimID"), data.get("rating"), data.get("comments")))
        conn.commit()
        last = cur.lastrowid
        cur.close()
        return last

    def delete_feedback(self, feedback_id):
        conn = self.db.get_connection()
        cur = conn.cursor()
        cur.execute("DELETE FROM Feedback WHERE feedbackID=%s", (feedback_id,))
        conn.commit()
        rc = cur.rowcount
        cur.close()
        return rc
