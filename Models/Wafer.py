class Wafer:
    def __init__(self,type,steps,quantity):
        self.type=type
        self.steps=steps
        self.quantity=quantity
        self.sequence=[]

    def printData(self):
        print(f"type: {self.type}")
        print(f"steps: {self.steps}")
        print(f"quantity: {self.quantity}")
        print("\n\n\n")