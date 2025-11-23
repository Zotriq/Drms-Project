from repositories.feedback_repository import FeedbackRepository
from services.base_service import BaseService

class FeedbackService(BaseService):
    def __init__(self, repo: FeedbackRepository):
        super().__init__(repo)

    def list_feedback(self):
        return self.repo.get_all_feedback()

    def get_feedback(self, feedback_id):
        f = self.repo.get_feedback(feedback_id)
        if not f:
            raise ValueError("Feedback not found")
        return f

    def create_feedback(self, payload):
        return self.repo.create_feedback(payload)

    def delete_feedback(self, feedback_id):
        rc = self.repo.delete_feedback(feedback_id)
        if rc == 0:
            raise ValueError("Feedback not found")
        return rc
