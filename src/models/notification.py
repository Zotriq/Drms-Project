class Notification:
    def __init__(self, notificationID=None, message=None, channel='in_app', recipientUserID=None, recipientRole=None, createdAt=None, deliveredAt=None, status='pending', meta=None):
        self.notificationID = notificationID
        self.message = message
        self.channel = channel
        self.recipientUserID = recipientUserID
        self.recipientRole = recipientRole
        self.createdAt = createdAt
        self.deliveredAt = deliveredAt
        self.status = status
        self.meta = meta

    def __repr__(self):
        return f"<Notification {self.notificationID}: {self.channel}>"
