from collections import defaultdict
class Wafer:
    def __init__(self,type,steps,quantity):
        self.type=type
        self.steps=steps
        self.quantity=quantity
        self.sequence=[]

    def topoSort(self,step_dictionary):
        adj=defaultdict(list)
        # print(self.steps)
        for step in self.steps.keys():
            dependency_list=step_dictionary[step].dependency
            # print(dependency_list)
            if(dependency_list!=None):
                for dependency in dependency_list:
                    adj[dependency].append(step)
            else:
                if(len(adj[step])==0):
                    adj[step]=[]

        visited=defaultdict(bool)
        for i in adj.keys():
            visited[i]=False

        def topo(step):
            visited[step]=True
            for adjacency_node in adj[step]:
                if(visited[adjacency_node]==False):
                    topo(adjacency_node)
            self.sequence.insert(0,step)

        for step in self.steps.keys():
            if(visited[step]==False):
                topo(step)
        # print(self.sequence)

    def printData(self):
        print(f"type: {self.type}")
        print(f"steps: {self.steps}")
        print(f"quantity: {self.quantity}")
        print("\n\n\n")