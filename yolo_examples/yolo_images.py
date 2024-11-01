import cv2
from ultralytics import YOLO

# Load a YOLO11n PyTorch model
model = YOLO("yolov8n.pt")

# Export the model to NCNN format
model.export(format="ncnn")  # creates 'yolo11n_ncnn_model'

# Load the exported NCNN model
ncnn_model = YOLO("yolov8n_ncnn_model")

# Run inference
results = ncnn_model("bus.jpg")

annotated_frame = results[0].plot()

cv2.imshow("Restuls", annotated_frame)
cv2.waitKey(0)
cv2.destroyAllWindows()
