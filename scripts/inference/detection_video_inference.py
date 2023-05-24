import os
import cv2
from ultralytics import YOLO

PROJECT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
yolo_model = os.path.join(PROJECT_DIR, "output", "yolov8n_custom", "weights", "best.pt")

# Load the YOLOv8 model
model = YOLO(yolo_model)

# Open the video file
video_path = os.path.join(PROJECT_DIR, "data_for_inference", "video", "vid_39_1284-2_11.mp4")
cap = cv2.VideoCapture(video_path)
display_size = (800, 600)

# Loop through the video frames
while cap.isOpened():
    # Read a frame from the video
    success, frame = cap.read()

    if success:
        # Run YOLOv8 inference on the frame
        # save plotted images
        plotted_result_path = os.path.join(PROJECT_DIR, "scripts", "inference")
        results = model.predict(source=frame,
                                save=True,
                                conf=0.2,
                                project=plotted_result_path)

        # Visualize the results on the frame
        annotated_frame = results[0].plot()

        # resize the frame to fit the display window
        annotated_frame = cv2.resize(annotated_frame, display_size)

        # Display the annotated frame
        cv2.imshow("YOLOv8 Inference", annotated_frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        # Break the loop if the end of the video is reached
        break

# Release the video capture object and close the display window
cap.release()
cv2.destroyAllWindows()
