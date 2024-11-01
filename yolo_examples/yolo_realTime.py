import cv2
from picamera2 import Picamera2
from libcamera import Transform
from ultralytics import YOLO

# Initialize the Picamera2
picam2 = Picamera2()
camera_config = picam2.create_still_configuration(main={"size": (1640,1232)},transform=Transform(vflip=True,hflip=True))
picam2.configure(camera_config)
picam2.start()

# Load the YOLO11 model
model = YOLO("yolov8n_ncnn_model")

while True:
    # Capture frame-by-frame
    frame = picam2.capture_array()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Run YOLO11 inference on the frame
    results = model(frame)

    # Visualize the results on the frame
    annotated_frame = results[0].plot()

    # Display the resulting frame
    cv2.imshow("Camera", annotated_frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) == ord("q"):
        break

# Release resources and close windows
cv2.destroyAllWindows()
