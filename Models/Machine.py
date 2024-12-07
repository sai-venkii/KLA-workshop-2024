class Machine:
    def __init__(self,id,cooldown_time,initial_parameters,fluctuations,capacity):
        self.id=id
        self.current_wafer_count=0
        self.cooldown_time=cooldown_time
        self.initial_parameters=initial_parameters
        self.current_parameters=initial_parameters
        self.fluctuations=fluctuations
        self.capacity=capacity
        self.isIdle=True

    def incrementCurrentWafer(self):
        self.current_wafer_count+=1   