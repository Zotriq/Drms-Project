from repositories.shelter_repository import ShelterRepository
from services.base_service import BaseService

class ShelterService(BaseService):
    def __init__(self, repo: ShelterRepository):
        super().__init__(repo)

    def list_shelters(self):
        return self.repo.get_all_shelters()

    def get_shelter(self, shelter_id):
        s = self.repo.get_shelter(shelter_id)
        if not s:
            raise ValueError("Shelter not found")
        return s

    def create_shelter(self, payload):
        return self.repo.create_shelter(payload)

    def update_shelter(self, shelter_id, payload):
        rc = self.repo.update_shelter(shelter_id, payload)
        if rc == 0:
            raise ValueError("Shelter not found or nothing changed")
        return rc

    def delete_shelter(self, shelter_id):
        rc = self.repo.delete_shelter(shelter_id)
        if rc == 0:
            raise ValueError("Shelter not found")
        return rc
