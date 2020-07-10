class EventSourcer():
    # Do not change the signature of any functions

    def __init__(self):
        self.value = 0
        self.redoStack=[]
        self.operationStack=[]
        self.operationStack.append(0)

    def add(self, num: int):
        self.value=self.value+num
        self.operationStack.append(self.value)
        return self.operationStack[-1]

    def subtract(self, num: int):
        self.value=self.value-num
        self.operationStack.append(self.value)
        return self.operationStack[-1]

    def undo(self):
        try:
            operationValue=self.operationStack.pop()
            differenceValue=operationValue-self.operationStack[-1]
            self.redoStack.append(differenceValue)
            self.value=self.operationStack[-1]
            return self.value
        except:
            return str(0) + " (Nothing to undo)"


    def redo(self):
        try:
            operationValue=self.redoStack.pop()
            self.operationStack.append(self.operationStack[-1]+operationValue)
            self.value=self.operationStack[-1]
            return self.value
        except:
            return str(self.operationStack[-1])+" (Nothing to redo)"


    def bulk_undo(self, steps: int):
        try:
            for step in range(0,steps):
                operationValue = self.operationStack.pop()
                differenceValue = operationValue - self.operationStack[-1]
                self.redoStack.append(differenceValue)
            self.value=self.operationStack[-1]
            return self.value
        except:
            return str(0) + " (Nothing to undo)"


    def bulk_redo(self, steps: int):
        try:
            for step in range(0,steps):
                try:
                    operationValue = self.redoStack.pop()
                    self.operationStack.append(self.operationStack[-1] + operationValue)
                except:
                    pass
            self.value=self.operationStack[-1]
            return self.value
        except:
            return str(self.operationStack[-1])+" (Nothing to redo)"
    # Undo the specific step (Count starts from first step)
    def specific_undo(self, step_no: int):
        try:
            operationValue = self.operationStack[len(self.operationStack)-step_no-1]
            previousValue = self.operationStack[len(self.operationStack)-step_no-2]
            differenceValue=operationValue-previousValue
            # Changing the values from the list after step_no index
            for index in range(step_no-1,len(self.operationStack)):
                self.operationStack[index]-=differenceValue
            self.operationStack.pop(len(self.operationStack) - step_no - 1)
            self.redoStack.append(differenceValue)
            return self.operationStack[-1]
        except:
            return self.operationStack[-1]

