from repositories.report_repository import ReportRepository
from services.base_service import BaseService

class ReportService(BaseService):
    def __init__(self, repo: ReportRepository):
        super().__init__(repo)

    def list_reports(self):
        return self.repo.get_all_reports()

    def get_report(self, report_id):
        r = self.repo.get_report(report_id)
        if not r:
            raise ValueError("Report not found")
        return r

    def create_report(self, payload):
        return self.repo.create_report(payload)

    def delete_report(self, report_id):
        rc = self.repo.delete_report(report_id)
        if rc == 0:
            raise ValueError("Report not found")
        return rc
