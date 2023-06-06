import cv2
import glob
import json
import os.path
import numpy as np
from python import ultimateAlprSdk

PROJECT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
display_size = (1200, 700)
TAG = "[PythonRecognizer] "

# Defines the default JSON configuration. More information at
# https://www.doubango.org/SDKs/anpr/docs/Configuration_options.html
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
def load_cv2_image(path):
    import traceback

    # Load image using cv2
    image = cv2.imread(path)
    if image is None:
        raise ValueError(TAG + "Failed to load image: %s" % path)

    # Read image orientation from EXIF (if available)
    orientation = 1
    try:
        exif_data = image.getexif()
        if exif_data is not None:
            for tag, value in exif_data.items():
                if tag == 0x0112:  # Tag for orientation
                    orientation = value
                    break
    except Exception as e:
        print(TAG + "An exception occurred: {}".format(e))
        traceback.print_exc()

    # Apply orientation correction if needed
    if orientation > 1:
        rotate_code = cv2.ROTATE_90_CLOCKWISE if orientation == 6 else cv2.ROTATE_90_COUNTERCLOCKWISE
        image = cv2.rotate(image, rotate_code)

    # Convert BGR image to RGB
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Determine image mode
    image_mode = None
    if image.shape[2] == 3:
        image_mode = 'RGB'
    elif image.shape[2] == 4:
        image_mode = 'RGBA'
    elif image.shape[2] == 1:
        image_mode = 'L'
    else:
        raise ValueError(TAG + "Invalid number of channels in the image")

    # Get image type based on mode
    if image_mode not in IMAGE_TYPES_MAPPING:
        raise ValueError(TAG + "Invalid mode: %s" % image_mode)

    image_type = IMAGE_TYPES_MAPPING[image_mode]

    return image, image_type


# draw rectangle and confidence to cars and license plates on cars
def visualize_result(result_dict, image):
    plates = result_dict["plates"]

    # Draw bounding boxes and labels on the image
    for plate in plates:
        # Get the plate text and confidence
        plate_text = plate["text"]
        confidence_det = plate["confidences"][1]

        # Get the quadrilateral points
        warped_box = plate["warpedBox"]
        pts = [(warped_box[i], warped_box[i + 1]) for i in range(0, len(warped_box), 2)]

        # Convert points to integers
        pts = np.array(pts, dtype=np.int32)

        # Draw bounding box and text on the image
        cv2.polylines(image, [pts], True, (0, 255, 0), 2)
        cv2.putText(image, f"{plate_text} ({confidence_det:.2f})",
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
def check_result(operation, result):
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

    # Initialize the engine
    check_result("Init", ultimateAlprSdk.UltAlprSdkEngine_init(json.dumps(JSON_CONFIG)))

    # Process each image in the folder
    images = glob.glob(os.path.join(image_folder, '*.png'))
    for image_path in images:
        # Check if image exists
        if not os.path.isfile(image_path):
            raise OSError(TAG + "File doesn't exist: %s" % image_path)

        # Decode the image and extract type
        # image, imageType = load_pil_image(image_path)
        # width, height = image.size
        image, imageType = load_cv2_image(image_path)
        height, width, channels = image.shape
        results = ultimateAlprSdk.UltAlprSdkEngine_process(
                                      imageType,
                                      image.tobytes(),  # type(x) == bytes
                                      width,
                                      height,
                                      0,  # stride
                                      1  # exifOrientation (already rotated in load_image -> use default value: 1)
                                    )

        result_dict = check_result("Process", results)
        # Convert RGB image to BGR
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        image = visualize_result(result_dict, image)
        image = cv2.resize(image, display_size)
        cv2.imshow("License Plate Recognition", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    # DeInit the engine
    check_result("DeInit",ultimateAlprSdk.UltAlprSdkEngine_deInit())


if __name__ == "__main__":
    image_folder = os.path.join(PROJECT_DIR, 'assets', 'images')
    charset = "latin"
    assets_folder = os.path.join(PROJECT_DIR, 'assets')

    process_images(image_folder, charset, assets_folder)

