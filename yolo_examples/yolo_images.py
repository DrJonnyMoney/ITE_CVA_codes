import cv2
from ultralytics import YOLO

# Load a YOLO11n PyTorch model
model = YOLO("yolov8n.pt")

# Export the model to NCNN format
model.export(format="ncnn")  # creates 'yolo11n_ncnn_model'

# Load the exported NCNN model
ncnn_model = YOLO("yolov8n_ncnn_model")

# Run inference
results = ncnn_model(""https://ultralytics.com/images/bus.jpg"")

# Visualize the results on the image
annotated_image = results[0].plot()

# Display the resulting image
cv2.imshow("Restuls", annotated_image)

# Quit on key press
cv2.waitKey(0)

# Close windows
cv2.destroyAllWindows()
