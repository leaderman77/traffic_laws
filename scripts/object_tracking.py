import os
import cv2 as cv
import supervision as sv
from ultralytics import YOLO

# necessary for counting
# LINE_START = sv.Point(320, 0)
# LINE_END = sv.Point(320, 480)


def load_model():
    project_dir = os.path.dirname(os.path.dirname(__file__))
    model_path = os.path.join(project_dir, "models", "best.pt")
    source_path = os.path.join(project_dir, "data", "video", "vid_39_1284-2_3881.mp4")

    # model = YOLO("yolov8n.pt")
    model = YOLO(model_path)
    results = model.track(
        source=source_path,
        show=True,
        conf=0.1,
        iou=0.1,
        stream=True,
        agnostic_nms=True)

    return results, model


def tracking():

    display_size = (800, 600)
    # line_counter = sv.LineZone(start=LINE_START, end=LINE_END)
    # line_annotator = sv.LineZoneAnnotator(thickness=2, text_thickness=1, text_scale=0.5)
    box_annotator = sv.BoxAnnotator(
        thickness=2,
        text_thickness=1,
        text_scale=0.5
    )

    os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'
    results, model = load_model()

    # for result in model.track(source=0, show=True, stream=True, agnostic_nms=True):
    for result in results:
        frame = result.orig_img
        detections = sv.Detections.from_yolov8(result)

        if result.boxes.id is not None:
            detections.tracker_id = result.boxes.id.cpu().numpy().astype(int)
            print(detections.tracker_id)
        # detections = detections[(detections.class_id != 60) & (detections.class_id != 0)]

        labels = [
            f"{tracker_id} {model.model.names[class_id]} {confidence:0.2f}"
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
        frame = cv.resize(frame, display_size)
        cv.imshow("yolov8", frame)

        # if (cv2.waitKey(30) == 27):
        if cv.waitKey(1) == ord("q"):
            break


if __name__ == "__main__":
    tracking()