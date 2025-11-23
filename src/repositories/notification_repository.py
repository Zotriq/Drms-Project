from repositories.base_repository import BaseRepository
from db.connection import Database
from models.notification import Notification

class NotificationRepository(BaseRepository):
    def __init__(self, db: Database):
        super().__init__(db, "Notification")

    def get_all_notifications(self):
        rows = self.fetch_all()
        return [Notification(**r) for r in rows]

    def get_notification(self, notification_id):
        row = self.fetch_by_id("notificationID", notification_id)
        return Notification(**row) if row else None

    def create_notification(self, data: dict):
        conn = self.db.get_connection()
        cur = conn.cursor()
        sql = "INSERT INTO Notification (message, channel, recipientUserID, recipientRole, status, meta) VALUES (%s,%s,%s,%s,%s,%s)"
        cur.execute(sql, (data.get("message"), data.get("channel", "in_app"), data.get("recipientUserID"), data.get("recipientRole"), data.get("status", "pending"), data.get("meta")))
        conn.commit()
        last = cur.lastrowid
        cur.close()
        return last

    def update_notification(self, notification_id, data: dict):
        conn = self.db.get_connection()
        cur = conn.cursor()
        sql = "UPDATE Notification SET message=%s, channel=%s, recipientUserID=%s, recipientRole=%s, status=%s, meta=%s WHERE notificationID=%s"
        cur.execute(sql, (data.get("message"), data.get("channel"), data.get("recipientUserID"), data.get("recipientRole"), data.get("status"), data.get("meta"), notification_id))
        conn.commit()
        rc = cur.rowcount
        cur.close()
        return rc

    def delete_notification(self, notification_id):
        conn = self.db.get_connection()
        cur = conn.cursor()
        cur.execute("DELETE FROM Notification WHERE notificationID=%s", (notification_id,))
        conn.commit()
        rc = cur.rowcount
        cur.close()
        return rc
