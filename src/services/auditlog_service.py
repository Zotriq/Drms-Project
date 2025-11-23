from repositories.auditlog_repository import AuditLogRepository
from services.base_service import BaseService

class AuditLogService(BaseService):
    def __init__(self, repo: AuditLogRepository):
        super().__init__(repo)

    def list_logs(self):
        return self.repo.get_all_logs()

    def create_log(self, payload):
        return self.repo.create_log(payload)
