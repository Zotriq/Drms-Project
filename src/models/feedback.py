class Feedback:
    def __init__(self, feedbackID=None, requestID=None, victimID=None, rating=None, comments=None, createdAt=None):
        self.feedbackID = feedbackID
        self.requestID = requestID
        self.victimID = victimID
        self.rating = rating
        self.comments = comments
        self.createdAt = createdAt

    def __repr__(self):
        return f"<Feedback {self.feedbackID}: rating={self.rating}>"
