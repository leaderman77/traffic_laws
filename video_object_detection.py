import cv2 as cv
import numpy as np
from ultralytics import YOLO
from utils import draw_detections
obj_cls = ["Stop Line"]


def get_bbox_coordinate(results):

    for i in range(len(results)):
        boxes = results[i].boxes
        # original image
        image = results[i].orig_img
        for j in range(len(boxes)):
            bbox_tensor = boxes[j].xyxy
            # get bounding box coordinates as NumPy array [x1, y1, x2, y2]
            bbox_na = bbox_tensor[0].cpu().numpy()
            # xmin = int(bbox_na[0].item())
            # ymin = int(bbox_na[1].item())
            # xmax = int(bbox_na[2].item())
            # ymax = int(bbox_na[3].item())

            x0 = bbox_na[0].item()
            y0 = bbox_na[1].item()
            x1 = bbox_na[2].item()
            y1 = bbox_na[3].item()

            det_box = np.array([x0, y0, x1, y1])
            bbox_tensor_conf = boxes[j].conf
            conf = bbox_tensor_conf[0].cpu().numpy()
            image = draw_detections(image, [det_box], [conf], [0])
            # draw the bounding box
            # cv.rectangle(image, (xmin, ymin), (xmax, ymax), (0, 255, 0), 2)
            # cv.putText(image, "Stop Line", (xmin, ymin - 10), cv.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
    return image


def detect_stop_line(model, image, conf_thresh):
    # get detection results
    results = model(image, conf=conf_thresh)

    # bbox coordinates
    image = get_bbox_coordinate(results)

    return image


def main():
    # load the YOLO model
    model = YOLO("models/best.pt")

    # create a VideoCapture object for the video file
    cap = cv.VideoCapture("data/video/vid_39_1284-2_3881.mp4")
    # set the size of the display window
    display_size = (800, 600)

    # loop through the frames of the video
    while True:
        # read a frame from the video
        ret, frame = cap.read()

        if not ret:
            break

        # resize the frame to fit the display window
        frame = cv.resize(frame, display_size)

        # detect stop lines in the frame
        frame = detect_stop_line(model, frame, conf_thresh=0.2)

        # display the frame with the bounding boxes
        cv.imshow("Stop Line Detection", frame)

        # wait for a key press
        if cv.waitKey(1) == ord("q"):
            break

    # release the VideoCapture object and close all windows
    cap.release()
    cv.destroyAllWindows()


if __name__ == "__main__":
    main()
