from repositories.base_repository import BaseRepository
from db.connection import Database
from models.shelter import Shelter

class ShelterRepository(BaseRepository):
    def __init__(self, db: Database):
        super().__init__(db, "Shelter")

    def get_all_shelters(self):
        rows = self.fetch_all()
        return [Shelter(**r) for r in rows]

    def get_shelter(self, shelter_id):
        row = self.fetch_by_id("shelterID", shelter_id)
        return Shelter(**row) if row else None

    def create_shelter(self, data: dict):
        conn = self.db.get_connection()
        cur = conn.cursor()
        sql = """INSERT INTO Shelter (name, latitude, longitude, capacity, current_occupancy, contact)
                 VALUES (%s,%s,%s,%s,%s,%s)"""
        cur.execute(sql, (data.get("name"), data.get("latitude"), data.get("longitude"), data.get("capacity", 0), data.get("current_occupancy", 0), data.get("contact")))
        conn.commit()
        last = cur.lastrowid
        cur.close()
        return last

    def update_shelter(self, shelter_id, data: dict):
        conn = self.db.get_connection()
        cur = conn.cursor()
        sql = """UPDATE Shelter SET name=%s, latitude=%s, longitude=%s, capacity=%s, current_occupancy=%s, contact=%s WHERE shelterID=%s"""
        cur.execute(sql, (data.get("name"), data.get("latitude"), data.get("longitude"), data.get("capacity"), data.get("current_occupancy"), data.get("contact"), shelter_id))
        conn.commit()
        rc = cur.rowcount
        cur.close()
        return rc

    def delete_shelter(self, shelter_id):
        conn = self.db.get_connection()
        cur = conn.cursor()
        cur.execute("DELETE FROM Shelter WHERE shelterID=%s", (shelter_id,))
        conn.commit()
        rc = cur.rowcount
        cur.close()
        return rc
