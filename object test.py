import yaml
import cv2
from ultralytics import YOLO

# Load the YAML file
with open("D:\\A\\interview.yolov8\\data.yaml", 'r') as file:
    config = yaml.safe_load(file)

# Extract names and colors
names = config.get('names', [])
colors = config.get('colors', {})

# Convert color list to tuple
class_colors = {name: tuple(color) for name, color in colors.items()}

# Load YOLO model
model = YOLO('D:\\A\\runs\\detect\\train\\weights\\best.pt')

# Open the video file
cap = cv2.VideoCapture('D:\\A\\test\\v1.mp4')

# Get video writer setup
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('D:\\A\\test\\output_v1.mp4', fourcc, 20.0, (int(cap.get(3)), int(cap.get(4))))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Run YOLO model on the frame
    results = model(frame)

    # Draw bounding boxes with labels and colors
    for result in results:
        for box in result.boxes:
            # Get class ID and bounding box coordinates
            class_id = int(box.cls)
            class_name = names[class_id]

            # Extract bounding box coordinates
            x1, y1, x2, y2 = box.xyxy[0].cpu().numpy()

            # Get the color for the class
            color = class_colors.get(class_name, (0, 255, 0))  # Default color if not found

            # Draw the bounding box
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), color, 2)
            cv2.putText(frame, class_name, (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)

    # Write the frame to the output video file
    out.write(frame)

    # Optional: If you still want to visualize, save the frames to disk or use an appropriate viewer
    # cv2.imshow('YOLO Detection', frame)
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     break

# Release resources
cap.release()
out.release()
# cv2.destroyAllWindows()  # This line can also be removed if imshow is not used
