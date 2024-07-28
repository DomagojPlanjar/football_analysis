import multiprocessing
from ultralytics import YOLO

# Fine tuning YOLOv5 model to find ball, goalkeepers, players and referees
# Model weights can be found in 'runs/detect/train/weights directory as 'best.pt' and 'last.pt'
# Move them to models directory to fit in training structure

# Training can be done on Google Colab with free GPU resources or locally depending
# on your graphics card


if __name__ == "__main__":
    multiprocessing.freeze_support()

    # Training config
    # Load YOLO model (Can use s,m,l,x model type depending on available resources)
    # Change data_cfg to your path to data.yaml file
    model = YOLO('yolov8l.pt')
    data_cfg = "..\\football-players-detection-1\\data.yaml"

    # Train the model
    model.train(
        data=data_cfg,
        epochs=100,
        imgsz=640,
        batch=16,
        device='0'  # Use '0' for GPU, 'cpu' for CPU
    )
