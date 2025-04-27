from ultralytics import YOLO
model = YOLO("runs/detect/train6/weights/best.pt")
results = model.predict("train/images/20__108_jpg.rf.13f457cf6df51c07b4daa2463a7794fe.jpg")
result = results[0]


len(result.boxes)
box = result.boxes[0]
print("Object type:", box.cls)
print("Coordinates:", box.xyxy)
print("Probability:", box.conf)

print(result.names)

# Display the resized image

result = results[0].plot()
import cv2
# Resize the plotted image to fit a 1000x1200 window
resized_image = cv2.resize(result, (600, 600))
cv2.imshow("result", resized_image)

cv2.waitKey(0)