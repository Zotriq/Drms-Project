class Shelter:
    def __init__(self, shelterID=None, name=None, latitude=None, longitude=None, capacity=0, current_occupancy=0, contact=None):
        self.shelterID = shelterID
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.capacity = capacity
        self.current_occupancy = current_occupancy
        self.contact = contact

    def __repr__(self):
        return f"<Shelter {self.shelterID}: {self.name}>"
