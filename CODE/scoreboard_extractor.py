from ultralytics import YOLO
import os,shutil
class YOLOModelWrapper:
    def __init__(self, model_path):
        self.model = YOLO(model_path)
        self.model_output="./runs"
        if os.path.exists(self.model_output):#if already exists delete
            print(f"'{self.model_output}' exists already. Attempting delete!")
            try:
                # Remove the folder and its contents
                shutil.rmtree(self.model_output)
                print(f"Removed older version of '{self.model_output}'")

            except Exception as e:
                print(f"Error removing folder '{self.model_output}': {e}")
        
    def  run_detection(self):
        results = self.model.predict(source="./Storage/extracted_frames", conf=0.4, save_crop=True)
        # print(results)
        return results

# def main():
#     model_path ="D:\BE Final Year Project\codespace/Model/best.pt"
#     input_source = "./Storage/extracted_frames"

#     yolo_wrapper = YOLOModelWrapper(model_path)
#     detection_results = yolo_wrapper.run_detection(input_source)

# if __name__ == "__main__":
#     main()
