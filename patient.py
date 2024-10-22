class Patient:
    def __init__(self, timeRequired, isAssigned):
        self.workTimeRequired = timeRequired
        self.isAssigned = isAssigned

    def checkAssignment(self):
        return self.isAssigned
    
    def changeAssignmentStatus(self):
        if self.isAssigned == True:
            return "Already assigned"
        
        else:
            self.isAssigned == True
            return "Assignment completed"
    
    def getTimeRequired(self):
        return self.workTimeRequired
        
    def __str__(self):
        return f"Patient requires {self.workTimeRequired} to complete examination"