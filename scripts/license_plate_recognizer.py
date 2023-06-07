import cv2
import glob
import json
import os.path
import traceback
import numpy as np
from PIL import Image
from python import ultimateAlprSdk


class LicensePlateRecognizer:
    def __init__(self, json_config, image_types_mapping):
        self.image_folder = os.path.join(PROJECT_DIR, 'assets', 'images')
        self.charset = "latin"
        self.assets_folder = os.path.join(PROJECT_DIR, 'assets')
        self.image_save_path = os.path.join(PROJECT_DIR, 'assets', 'result_imgs')
        self.is_save = True
        self.is_result_show = False
        self.json_config = json_config
        self.image_types_mapping = image_types_mapping
        self.result_dict = {}

    def load_cv2_image(self, path):
        image = cv2.imread(path)
        if image is None:
            raise ValueError("Failed to load image: %s" % path)

        orientation = 1
        try:
            pil_image = Image.open(path)
            exif_data = pil_image.getexif()
            if exif_data is not None:
                for tag, value in exif_data.items():
                    if tag == 0x0112:  # Tag for orientation
                        orientation = value
                        break
        except Exception as e:
            print("An exception occurred: {}".format(e))
            traceback.print_exc()

        if orientation > 1:
            rotate_code = cv2.ROTATE_90_CLOCKWISE if orientation == 6 else cv2.ROTATE_90_COUNTERCLOCKWISE
            image = cv2.rotate(image, rotate_code)

        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        image_mode = None
        if image.shape[2] == 3:
            image_mode = 'RGB'
        elif image.shape[2] == 4:
            image_mode = 'RGBA'
        elif image.shape[2] == 1:
            image_mode = 'L'
        else:
            raise ValueError("Invalid number of channels in the image")

        if image_mode not in self.image_types_mapping:
            raise ValueError("Invalid mode: %s" % image_mode)

        image_type = self.image_types_mapping[image_mode]

        return image, image_type

    def visualize_result(self, image):
        if "plates" not in self.result_dict:
            print("No license plates found in the result.")
            return image

        plates = self.result_dict["plates"]

        # Draw bounding boxes and labels on the image
        for plate in plates:
            plate_text = plate["text"]
            confidence_det = plate["confidences"][1]
            warped_box = plate["warpedBox"]
            pts = np.array([(warped_box[i], warped_box[i + 1]) for i in range(0, len(warped_box), 2)], dtype=np.int32)

            cv2.polylines(image, [pts], True, (0, 255, 0), 2)
            cv2.putText(image, f"{plate_text} ({confidence_det:.2f})", tuple(pts[0]), cv2.FONT_HERSHEY_SIMPLEX, 0.8,
                        (0, 255, 0), 2)

            car_box = np.array(plate["car"]["warpedBox"], dtype=np.int32).reshape((-1, 2))
            cv2.polylines(image, [car_box], True, (255, 0, 0), 2)
            car_confidence = plate["car"]["confidence"]
            car_text = f"Car Confidence: {car_confidence:.2f}%"
            text_position = (car_box[0][0], car_box[0][1] - 10)
            font = cv2.FONT_HERSHEY_SIMPLEX
            font_scale = 0.5
            font_thickness = 1
            cv2.putText(image, car_text, text_position, font, font_scale, (255, 0, 0), font_thickness)

        return image

    def save_result_image(self, image, image_path):
        filename = os.path.basename(image_path)
        result_image_path = os.path.join(self.image_save_path, filename)
        cv2.imwrite(result_image_path, image)

        print("Result image saved:", result_image_path)

    def check_result(self, operation, result):
        if not result.isOK():
            print(TAG + operation + ": failed -> " + result.phrase())
            assert False
        else:
            print(TAG + operation + ": OK -> " + result.json())
            result_dict = json.loads(result.json())

            if not result_dict:
                return None

            self.result_dict = result_dict

    def process_images(self):
        self.json_config["assets_folder"] = self.assets_folder
        self.json_config["charset"] = self.charset

        self.check_result("Init", ultimateAlprSdk.UltAlprSdkEngine_init(json.dumps(self.json_config)))

        images = glob.glob(os.path.join(self.image_folder, '*.*'))
        for image_path in images:
            if not os.path.isfile(image_path):
                raise OSError("File doesn't exist: %s" % image_path)

            image, image_type = self.load_cv2_image(image_path)
            height, width, channels = image.shape
            results = ultimateAlprSdk.UltAlprSdkEngine_process(
                image_type,
                image.tobytes(),
                width,
                height,
                0,
                1
            )

            self.check_result("Process", results)
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            image = self.visualize_result(image)
            image = cv2.resize(image, display_size)
            if self.is_result_show:
                cv2.imshow("License Plate Recognition", image)
                cv2.waitKey(0)
                cv2.destroyAllWindows()

            # save the image to the folder - assets/result_imgs
            if self.is_save:
                self.save_result_image(image, image_path)
        self.check_result("DeInit", ultimateAlprSdk.UltAlprSdkEngine_deInit())


if __name__ == "__main__":
    PROJECT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    display_size = (1200, 700)
    TAG = "[PythonRecognizer] "

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

    recognizer = LicensePlateRecognizer(JSON_CONFIG, IMAGE_TYPES_MAPPING)
    recognizer.process_images()
