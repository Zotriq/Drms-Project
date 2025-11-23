from repositories.base_repository import BaseRepository
from db.connection import Database
from models.auditlog import AuditLog

class AuditLogRepository(BaseRepository):
    def __init__(self, db: Database):
        super().__init__(db, "AuditLog")

    def get_all_logs(self):
        rows = self.fetch_all()
        return [AuditLog(**r) for r in rows]

    def create_log(self, data: dict):
        conn = self.db.get_connection()
        cur = conn.cursor()
        sql = "INSERT INTO AuditLog (actorUserID, action, targetTable, targetID, details) VALUES (%s,%s,%s,%s,%s)"
        cur.execute(sql, (data.get("actorUserID"), data.get("action"), data.get("targetTable"), data.get("targetID"), data.get("details")))
        conn.commit()
        last = cur.lastrowid
        cur.close()
        return last
