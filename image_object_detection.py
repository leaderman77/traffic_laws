from ultralytics import YOLO
import numpy as np
import cv2 as cv
from utils import draw_detections
obj_cls = ["Stop Line"]


def get_bbox_coordinate(results):
    box = []
    for i in range(len(results)):
        boxes = results[i].boxes
        for j in range(len(boxes)):
            bbox_tensor = boxes[j].xyxy
            # get bounding box coordinates as NumPy array [x1, y1, x2, y2]
            bbox_na = bbox_tensor[0].cpu().numpy()

            x0 = bbox_na[0].item()
            y0 = bbox_na[1].item()
            x1 = bbox_na[2].item()
            y1 = bbox_na[3].item()

            det_box = np.array([x0, y0, x1, y1])
            bbox_tensor_conf = boxes[j].conf
            conf = bbox_tensor_conf[0].cpu().numpy()
            print(conf)
            print(det_box)
            return det_box, conf


def inference(image_file):
    # load model
    model = YOLO("models/best.pt")

    # prediction
    results = model(image_file, conf=0.2)

    return results


def main():
    results = inference("dataset/test/images/frame676.jpg")

    # original image
    image = results[0].orig_img

    # bbox coordinates
    # xmin, ymin, xmax, ymax, conf = get_bbox_coordinate(results)
    box, conf = get_bbox_coordinate(results)

    drawed_img = draw_detections(image, [box], [conf], [0])
    # create a named window and set its properties
    cv.namedWindow("Image with Bounding Box", cv.WINDOW_NORMAL)
    cv.resizeWindow("Image with Bounding Box", (800, 600))

    # # display the image with the bounding box
    cv.imshow("Image with Bounding Box", drawed_img)
    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == '__main__':
    main()


