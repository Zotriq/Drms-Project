class AuditLog:
    def __init__(self, logID=None, actorUserID=None, action=None, targetTable=None, targetID=None, details=None, loggedAt=None):
        self.logID = logID
        self.actorUserID = actorUserID
        self.action = action
        self.targetTable = targetTable
        self.targetID = targetID
        self.details = details
        self.loggedAt = loggedAt

    def __repr__(self):
        return f"<Audit {self.logID}: {self.action} on {self.targetTable}>"
