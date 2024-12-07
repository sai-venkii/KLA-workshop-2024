import json
from Models.Machine import Machine
from Models.Step import Step
from Models.Wafer import Wafer

Wafer_dictionary={}
Step_dictionary={}
Machine_dictionary={}

def processSteps(steps_data):
    for step in steps_data:
        Step_dictionary[step["id"]]=Step(step["id"],step["parameters"],step["dependency"])

def printStepData():
    for keys in Step_dictionary.keys():
        Step_dictionary[keys].printData()

def processMachines(machine_data):
    for machine in machine_data:
        Machine_dictionary[machine["machine_id"]]=\
            Machine(\
                machine["machine_id"],\
                machine["cooldown_time"],\
                machine["initial_parameters"],\
                machine["fluctuation"],\
                machine["n"]\
                )
        Step_dictionary[machine["step_id"]].machines.append(machine["machine_id"])

def processWafer(wafer_data):
    for wafer in wafer_data:
        Wafer_dictionary[wafer["type"]]=Wafer(wafer["type"],wafer["processing_times"],wafer["quantity"])


final_schedule={"schedule":[]}
def addSchedule(wafer_id,step,machine,start_time,end_time):
    final_schedule["schedule"].append({
        "wafer_id":wafer_id,
        "step":step,
        "machine":machine,
        "start_time":start_time,
        "end_time":end_time
    })



def handleWafer(wafer,wafer_id,start_time,end_time):
    for step,step_time in wafer.steps.items():
        machines=Step_dictionary[step].machines
        for machine in machines:
            targetmachine=Machine_dictionary[machine]
            if(targetmachine.isIdle):
                start_time=end_time
                if(targetmachine.current_wafer_count == targetmachine.capacity):
                    for key,value in targetmachine.current_parameters.items():
                        targetmachine.current_parameters[key]+=targetmachine.fluctuations[key]
                
                targetmachine.incrementCurrentWafer()
                end_time+=step_time
                addSchedule(f"{wafer.type}-{wafer_id}",step,targetmachine.id,start_time,end_time)
                break
    return start_time,end_time


def writeToFile(milestone_num):
    f=open(f"Output/M{milestone_num}.json","w")
    json.dump(final_schedule,f)

def determineSchedule():
    start_time=0
    end_time=0
    for wafer in Wafer_dictionary.values():
        quantity=wafer.quantity
        for wafer_id in range(1,quantity+1):
            start_time,end_time=handleWafer(wafer,wafer_id,start_time,end_time)
    print(final_schedule)


if __name__ == "__main__":
    milestone_num=str(input("Enter your Milestone: "))
    FILE_NAME=f"Input/Milestone{milestone_num}.json"
    file=open(FILE_NAME,"r")
    data=json.load(file)
    processSteps(data["steps"])
    processMachines(data["machines"])
    processWafer(data["wafers"])
    # print(Wafer_dictionary)
    determineSchedule()
    writeToFile(milestone_num)
    # printStepData()
    # print(data["steps"])
