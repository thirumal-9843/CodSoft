from json_utiil import *
from tabulate import tabulate

def add_task(task):
    data=read_json()
    id=len(data["task"])+1
    task_data={
        "id":id,
        "task_desc":task,
        "status":"open"
        
    }
    data["task"].append(task_data)
    write_json(data)
    print("task created")
def view_task():
    data=read_json()
    table=[]
    for task in data["task"]:
        row=[task["id"],task["task_desc"],task["status"]]
        table.append(row)
    print(tabulate(table,headers=["ID","TASK_DESCRPTION","STATUS"],tablefmt="grid",numalign="center",stralign="center"))
def update_task(id):
    data=read_json()
    flag="n"
    for task in data["task"]:
        if task["id"]==id:
            flag="y"
            if task["status"]!="Done":
                task["status"]="Done"
                write_json(data)
                print("Task {id} marked as Done")
            else:
                print("Task is already completed")
        if flag=="n":
            print(f"{id} not found!")
def delete_task(id):
    data=read_json()
    flag="n"
    for task in data["task"]:
        if task["id"]==id:
            flag="y"
            data["task"].remove(task)
            i=1
            for t in data["task"]:
                t["id"]=i
                i+=1
            write_json(data)
            print(f"{id} deleted successfully")
        if flag == "n":
            print(f"{id} not found!")
            

