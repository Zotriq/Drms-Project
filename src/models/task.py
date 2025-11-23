class Task:
    def __init__(self, taskID=None, title=None, description=None, taskType='other', status='unassigned',
                 assignedVolunteerID=None, createdBy=None, relatedRequestID=None, createdAt=None, updatedAt=None):
        self.taskID = taskID
        self.title = title
        self.description = description
        self.taskType = taskType
        self.status = status
        self.assignedVolunteerID = assignedVolunteerID
        self.createdBy = createdBy
        self.relatedRequestID = relatedRequestID
        self.createdAt = createdAt
        self.updatedAt = updatedAt

    def __repr__(self):
        return f"<Task {self.taskID}: {self.title}>"
