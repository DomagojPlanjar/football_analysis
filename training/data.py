import shutil

# Training dataset for object detection
# You can obtain it from https://universe.roboflow.com/roboflow-jvuqo/football-players-detection-3zvbc/dataset/1
# You will be provided next 5 lines of code with your unique api key

from roboflow import Roboflow
rf = Roboflow(api_key="")
project = rf.workspace("roboflow-jvuqo").project("football-players-detection-3zvbc")
version = project.version(1)
dataset = version.download("yolov5")

# Rearrangement of files is needed to get the model to work

shutil.move('football-players-detection-1/train',
            'football-players-detection-1/football-players-detection-1/train'
            )

shutil.move('football-players-detection-1/test',
            'football-players-detection-1/football-players-detection-1/test'
            )

shutil.move('football-players-detection-1/valid',
            'football-players-detection-1/football-players-detection-1/valid'
            )