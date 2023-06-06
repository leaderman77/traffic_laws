from python import ultimateAlprSdk
import json
import os.path
import glob
import cv2
from PIL import ImageDraw
import numpy as np

PROJECT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

TAG = "[PythonRecognizer] "

# Defines the default JSON configuration. More information at https://www.doubango.org/SDKs/anpr/docs/Configuration_options.html
JSON_CONFIG = {
    "debug_level": "info",
    "debug_write_input_image_enabled": False,
    "debug_internal_data_path": ".",

    "num_threads": -1,
    "gpgpu_enabled": True,
    "max_latency": -1,

    "klass_vcr_gamma": 1.5,

    "detect_roi": [0, 0, 0, 0],
    "detect_minscore": 0.1,

    "car_noplate_detect_min_score": 0.8,

    "pyramidal_search_enabled": True,
    "pyramidal_search_sensitivity": 0.28,
    "pyramidal_search_minscore": 0.3,
    "pyramidal_search_min_image_size_inpixels": 800,

    "recogn_rectify_enabled": True,
    "recogn_minscore": 0.3,
    "recogn_score_type": "min"
}

IMAGE_TYPES_MAPPING = {
    'RGB': ultimateAlprSdk.ULTALPR_SDK_IMAGE_TYPE_RGB24,
    'RGBA': ultimateAlprSdk.ULTALPR_SDK_IMAGE_TYPE_RGBA32,
    'L': ultimateAlprSdk.ULTALPR_SDK_IMAGE_TYPE_Y
}


# Load image
def load_pil_image(path):
    from PIL import Image, ExifTags, ImageOps
    import traceback
    pil_image = Image.open(path)
    img_exif = pil_image.getexif()
    ret = {}
    orientation = 1
    try:
        if img_exif:
            for tag, value in img_exif.items():
                decoded = ExifTags.TAGS.get(tag, tag)
                ret[decoded] = value
            orientation = ret["Orientation"]
    except Exception as e:
        print(TAG + "An exception occurred: {}".format(e))
        traceback.print_exc()

    if orientation > 1:
        pil_image = ImageOps.exif_transpose(pil_image)

    if pil_image.mode in IMAGE_TYPES_MAPPING:
        imageType = IMAGE_TYPES_MAPPING[pil_image.mode]
    else:
        raise ValueError(TAG + "Invalid mode: %s" % pil_image.mode)

    return pil_image, imageType


# draw rectangle and confidence to cars and license plates on cars
def visualize_result(result_dict, image_path):
    plates = result_dict["plates"]

    # Draw bounding boxes and labels on the image
    for plate in plates:
        # Get the plate text and confidence
        plate_text = plate["text"]
        confidence = plate["confidences"][0]

        # Get the quadrilateral points
        warped_box = plate["warpedBox"]
        pts = [(warped_box[i], warped_box[i + 1]) for i in range(0, len(warped_box), 2)]

        # Load the image using OpenCV
        image = cv2.imread(image_path)

        # Convert points to integers
        pts = np.array(pts, dtype=np.int32)

        # Draw bounding box and text on the image
        cv2.polylines(image, [pts], True, (0, 255, 0), 2)
        cv2.putText(image, f"{plate_text} ({confidence:.2f})",
                    tuple(pts[0]), cv2.FONT_HERSHEY_SIMPLEX, 0.8,
                    (0, 255, 0), 2)

        # Draw rectangle around the car
        car_box = plate["car"]["warpedBox"]
        car_box = np.array(car_box, dtype=np.int32).reshape((-1, 2))
        cv2.polylines(image, [car_box], True, (255, 0, 0), 2)

        # Get confidence for the car
        car_confidence = plate["car"]["confidence"]

        # Define the text to display
        car_text = "Car Confidence: {:.2f}%".format(car_confidence)

        # Set the position and font settings for the text
        text_position = (car_box[0][0], car_box[0][1] - 10)
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 0.5
        font_thickness = 1

        # Draw the text on the image
        cv2.putText(image, car_text, text_position, font, font_scale, (255, 0, 0), font_thickness)

    return image


# Check result
def checkResult(operation, result, image_path=""):
    if not result.isOK():
        print(TAG + operation + ": failed -> " + result.phrase())
        assert False
    else:
        print(TAG + operation + ": OK -> " + result.json())
        result_dict = json.loads(result.json())

        if len(result_dict) == 0:
            return

        return result_dict


def process_images(image_folder, charset, assets_folder):
    # Update JSON options using values from the arguments
    JSON_CONFIG["assets_folder"] = assets_folder
    JSON_CONFIG["charset"] = charset

    # Process each image in the folder
    images = glob.glob(os.path.join(image_folder, '*.PNG'))
    for image_path in images:
        # Check if image exists
        if not os.path.isfile(image_path):
            raise OSError(TAG + "File doesn't exist: %s" % image_path)

        # Decode the image and extract type
        image, imageType = load_pil_image(image_path)
        width, height = image.size

        # Initialize the engine
        checkResult("Init", ultimateAlprSdk.UltAlprSdkEngine_init(json.dumps(JSON_CONFIG)))

        result_dict = checkResult("Process",
                    ultimateAlprSdk.UltAlprSdkEngine_process(
                        imageType,
                        image.tobytes(),  # type(x) == bytes
                        width,
                        height,
                        0,  # stride
                        1  # exifOrientation (already rotated in load_image -> use default value: 1)
                        ),
                    image_path
                    )
        image = visualize_result(result_dict, image_path)

        cv2.imshow("License Plate Recognition", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        # DeInit the engine
        checkResult("DeInit",ultimateAlprSdk.UltAlprSdkEngine_deInit())


if __name__ == "__main__":

    image_folder = os.path.join(PROJECT_DIR, 'assets', 'images')
    charset = "latin"
    assets_folder = os.path.join(PROJECT_DIR, 'assets')

    process_images(image_folder, charset, assets_folder)

