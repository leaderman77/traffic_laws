import os
import cv2 as cv
import supervision as sv
from ultralytics import YOLO

PROJECT_DIR = os.path.dirname(os.path.dirname(__file__))
VIDEO_FILE = "data/video/vid_39_1284-2_3881.mp4"
MODEL_PATH = "models/best.pt"
DISPLAY_SIZE = (800, 600)

# necessary for counting
# LINE_START = sv.Point(320, 0)
# LINE_END = sv.Point(320, 480)


def tracking_objects(model_path, video_path, show=True, conf=0.2, iou=0.1, stream=True):
    os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'

    # model = YOLO("yolov8n.pt")
    yolo_model = YOLO(model_path)

    results = yolo_model.track(
        source=video_path,
        show=show,
        conf=conf,
        iou=iou,
        stream=stream,
        agnostic_nms=True)

    return results, yolo_model


def display_tracking(tracking_results, yolo_model):

    # line_counter = sv.LineZone(start=LINE_START, end=LINE_END)
    # line_annotator = sv.LineZoneAnnotator(thickness=2, text_thickness=1, text_scale=0.5)
    box_annotator = sv.BoxAnnotator(thickness=2, text_thickness=1, text_scale=0.5)

    for result in tracking_results:
        frame = result.orig_img
        detections = sv.Detections.from_yolov8(result)

        if result.boxes.id is not None:
            detections.tracker_id = result.boxes.id.cpu().numpy().astype(int)
            print(detections.tracker_id)
        # detections = detections[(detections.class_id != 60) & (detections.class_id != 0)]

        labels = [
            f"{tracker_id} {yolo_model.model.names[class_id]} {confidence:0.2f}"
            for _, confidence, class_id, tracker_id
            in detections
        ]
        print(labels)
        frame = box_annotator.annotate(
            scene=frame,
            detections=detections,
            labels=labels
        )

        # line_counter.trigger(detections=detections)
        # line_annotator.annotate(frame=frame, line_counter=line_counter)

        # resize the frame to fit the display window
        frame = cv.resize(frame, DISPLAY_SIZE)
        cv.imshow("yolov8", frame)

        if cv.waitKey(1) == ord("q"):
            break


def main():

    # model and video path
    model_path = os.path.join(PROJECT_DIR, MODEL_PATH)
    video_path = os.path.join(PROJECT_DIR, "data", "video", "vid_39_1284-2_3881.mp4")
    tracking_results, yolo_model = tracking_objects(model_path, video_path)
    display_tracking(tracking_results, yolo_model)


if __name__ == "__main__":
    main()
