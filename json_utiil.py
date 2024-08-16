import json

TASK_FILE="task.json"

def read_json():
    with open(TASK_FILE) as f:
        return json.load(f)
    
def write_json(data):
    with open(TASK_FILE, "w") as f:
        json.dump(data,f,indent=3)