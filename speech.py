import cv2
from ultralytics import YOLO
import torch
import pyttsx3

# Initialize TTS engine
engine = pyttsx3.init()

# Load the YOLOv8 model
model = YOLO("runs/detect/train6/weights/best.pt")

# If your model doesn't automatically load class names, define them.
# Provided names: ['10', '100', '20', '200', '2000', '50', '500', 'Invalid Currency', 'fake currency']
# If your model has a names attribute, you may skip this.
if not hasattr(model, 'names') or model.names is None:
    names = ['10', '100', '20', '200', '2000', '50', '500', 'Invalid Currency', 'fake currency']
    # Create a dictionary mapping index to name
    model.names = {i: name for i, name in enumerate(names)}

# Open the video source (0 for webcam)
video_capture = cv2.VideoCapture(0)

# Get video frame dimensions
frame_width = int(video_capture.get(3))
frame_height = int(video_capture.get(4))

# Define the codec and create a VideoWriter object to save the output video
output_path = "output_video.avi"
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(output_path, fourcc, 30, (frame_width, frame_height))

with torch.no_grad():
    while True:
        ret, frame = video_capture.read()
        if not ret:
            break

        # Perform object detection using YOLOv8 on the current frame
        results = model(source=frame)
        res_plotted = results[0].plot()
        res_bgr = cv2.cvtColor(res_plotted, cv2.COLOR_RGB2BGR)

        # Display the frame with detected objects
        cv2.imshow("Video Prediction", res_bgr)
        # Write the frame to the output video
        out.write(res_bgr)

        # Collect unique detected currencies from this frame.
        # The YOLOv8 result object has a `boxes` attribute with detected boxes.
        detected_currencies = set()
        if results[0].boxes is not None:
            for cls in results[0].boxes.cls:
                class_id = int(cls.item())
                currency = model.names.get(class_id, "Unknown")
                detected_currencies.add(currency)

        # For each unique detection, say the corresponding message
        for currency in detected_currencies:
            # Only speak if the detection is valid (optional filtering)
            engine.say(f"{currency} rupee detected")

        if detected_currencies:
            engine.runAndWait()  # This call blocks until all queued commands are spoken

        # Press 'q' to exit the loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Release the video capture and output objects
video_capture.release()
out.release()
cv2.destroyAllWindows()
