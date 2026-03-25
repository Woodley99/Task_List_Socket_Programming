import json
import os

# Stores files in a variable called FILE_NAME
FILE_NAME = "tasks.json"


# Check if the file exists, if it doesnt return an empty list
def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    
    # 'r' is read mode, "f" is file object, so when the file is opened its being given the name f
    with open(FILE_NAME, "r") as f:

        # try and return the json file if it fails return an empty list
        try: 
            return json.load(f)
        except:
            return []
        
# opens the file "w" is write mode, if the file exists it gets overwritten, if it doesnt it gets created
def save_tasks(tasks):
    with open(FILE_NAME, "w") as f:
        # dumps data into the file and indents it
        json.dump(tasks, f, indent=4)