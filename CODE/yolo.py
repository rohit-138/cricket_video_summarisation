from ultralytics import YOLO

class YOLOModelWrapper:
    def __init__(self, model_path):
        self.model = YOLO(model_path)

    def run_detection(self, input_source, confidence_threshold=0.85, save_crop=True, save=True):
        results = self.model.predict(source=input_source, conf=confidence_threshold, save_crop=save_crop, save=save)
        return results

# def main():
#     model_path = r'D:\BE Final Year Project\workspace\CODE\best.pt'
#     input_source = "D:\\images"

#     yolo_wrapper = YOLOModelWrapper(model_path)
#     detection_results = yolo_wrapper.run_detection(input_source)

# if __name__ == "__main__":
#     main()
