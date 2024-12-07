class Step:
    def __init__(self,id,parameters,dependency):
        self.id=id
        self.parameters=parameters
        self.dependency=dependency
        self.machines=[]

    def printData(self):
        print(f"id: {self.id}")
        print(f"parameters: {self.parameters}")
        print(f"dependency: {self.dependency}")
        print(f"machines: {self.machines}")
        print("\n\n\n")