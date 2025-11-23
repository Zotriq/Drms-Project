class Report:
    def __init__(self, reportID=None, reportType=None, parameters=None, generatedBy=None, generatedAt=None, filePath=None):
        self.reportID = reportID
        self.reportType = reportType
        self.parameters = parameters
        self.generatedBy = generatedBy
        self.generatedAt = generatedAt
        self.filePath = filePath

    def __repr__(self):
        return f"<Report {self.reportID}: {self.reportType}>"
