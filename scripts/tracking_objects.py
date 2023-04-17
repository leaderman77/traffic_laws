import os
import cv2 as cv
import supervision as sv
from ultralytics import YOLO

PROJECT_DIR = os.path.dirname(os.path.dirname(r"C:\Users\sardo\Documents\DS\PyCharm\cradle\traffic_laws\data\test\images"))
IMAGE_FILE = "data/images/frame3922.jpg"
MODEL_PATH = "models/best.pt"
DISPLAY_SIZE = (800, 600)

# necessary for counting
# LINE_START = sv.Point(320, 0)
# LINE_END = sv.Point(320, 480)


def tracking_objects(model_path, source_path, show=False, conf=0.2, iou=0.1, stream=True):
    os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'

    yolo_model = YOLO(model_path)

    results = yolo_model.track(
            source=source_path,
            show=show,
            conf=conf,
            iou=iou,
            stream=stream,
            agnostic_nms=True)
    return results, yolo_model


def tracking_video_process(video_path, model_path):
    tracking_results, yolo_model = tracking_objects(model_path, video_path)

    box_annotator = sv.BoxAnnotator(thickness=2, text_thickness=1, text_scale=0.5)

    for result in tracking_results:
        image = result.orig_img
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
        image = box_annotator.annotate(
            scene=image,
            detections=detections,
            labels=labels
        )
        image = cv.resize(image, DISPLAY_SIZE)
        cv.imshow("Tracking Video", image)
        if cv.waitKey(1) & 0xFF == ord("q"):
            break
        # cv.waitKey(0)
        # cv.destroyAllWindows()


def tracking_images_process(images_path, model_path):
    # Loop through all files in directory
    for img_file in os.listdir(images_path):
        image_file_path = os.path.join(images_path, img_file)

        # get image from file path
        if os.path.isfile(image_file_path) and os.stat(image_file_path).st_size <= 0:
            print(f"{image_file_path} is empty or does not exist.")
            return None

        tracking_results, yolo_model = tracking_objects(model_path, image_file_path)

        # line_counter = sv.LineZone(start=LINE_START, end=LINE_END)
        # line_annotator = sv.LineZoneAnnotator(thickness=2, text_thickness=1, text_scale=0.5)
        box_annotator = sv.BoxAnnotator(thickness=2, text_thickness=1, text_scale=0.5)

        for result in tracking_results:
            image = result.orig_img
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
            image = box_annotator.annotate(
                scene=image,
                detections=detections,
                labels=labels
            )

        image = cv.resize(image, DISPLAY_SIZE)
        cv.imshow("Image with tracking", image)
        cv.waitKey(0)
        cv.destroyAllWindows()


def main():
    # model and video path
    model_path = os.path.join(PROJECT_DIR, MODEL_PATH)
    image_path = os.path.join(PROJECT_DIR, IMAGE_FILE)
    video_path = os.path.join(PROJECT_DIR, "data", "video", "vid_39_1284-2_3881.mp4")

    # display tracking from video
    # tracking_video_process(video_path, model_path)

    # display tracking from images
    tracking_images_process(image_path, model_path)


if __name__ == "__main__":
    main()
