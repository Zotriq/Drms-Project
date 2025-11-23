from repositories.base_repository import BaseRepository
from db.connection import Database
from models.report import Report

class ReportRepository(BaseRepository):
    def __init__(self, db: Database):
        super().__init__(db, "Report")

    def get_all_reports(self):
        rows = self.fetch_all()
        return [Report(**r) for r in rows]

    def get_report(self, report_id):
        row = self.fetch_by_id("reportID", report_id)
        return Report(**row) if row else None

    def create_report(self, data: dict):
        conn = self.db.get_connection()
        cur = conn.cursor()
        sql = "INSERT INTO Report (reportType, parameters, generatedBy, filePath) VALUES (%s,%s,%s,%s)"
        cur.execute(sql, (data.get("reportType"), data.get("parameters"), data.get("generatedBy"), data.get("filePath")))
        conn.commit()
        last = cur.lastrowid
        cur.close()
        return last

    def delete_report(self, report_id):
        conn = self.db.get_connection()
        cur = conn.cursor()
        cur.execute("DELETE FROM Report WHERE reportID=%s", (report_id,))
        conn.commit()
        rc = cur.rowcount
        cur.close()
        return rc
