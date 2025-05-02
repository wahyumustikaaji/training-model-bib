from ultralytics import YOLO
import os
import yaml

# Cek apakah file data.yaml ada
if not os.path.exists("data.yaml"):
    print("Error: data.yaml file not found in the current directory")
    exit(1)

# Load dan validasi data.yaml
try:
    with open("data.yaml", "r") as f:
        data_config = yaml.safe_load(f)
        print(f"Dataset configuration loaded: {data_config}")
        print(f"Number of classes: {data_config.get('nc', 'not specified')}")
        print(f"Class names: {data_config.get('names', 'not specified')}")
except Exception as e:
    print(f"Error reading data.yaml: {e}")
    exit(1)

try:
    # Model YOLOv8
    model = YOLO("yolov8s.pt")  # Bisa pilih model yang sesuai

    # Melatih YOLOv8 dengan data.yaml
    model.train(data="data.yaml", epochs=50, imgsz=640)
except Exception as e:
    print(f"Error during training: {e}")
