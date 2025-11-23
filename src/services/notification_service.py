from repositories.notification_repository import NotificationRepository
from services.base_service import BaseService

class NotificationService(BaseService):
    def __init__(self, repo: NotificationRepository):
        super().__init__(repo)

    def list_notifications(self):
        return self.repo.get_all_notifications()

    def get_notification(self, notification_id):
        n = self.repo.get_notification(notification_id)
        if not n:
            raise ValueError("Notification not found")
        return n

    def create_notification(self, payload):
        return self.repo.create_notification(payload)

    def update_notification(self, notification_id, payload):
        rc = self.repo.update_notification(notification_id, payload)
        if rc == 0:
            raise ValueError("Notification not found or nothing changed")
        return rc

    def delete_notification(self, notification_id):
        rc = self.repo.delete_notification(notification_id)
        if rc == 0:
            raise ValueError("Notification not found")
        return rc
