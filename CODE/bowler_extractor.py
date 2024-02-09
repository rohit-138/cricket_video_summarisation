from ultralytics import YOLO
import os,shutil
import pandas as pd
class YOLOBowlerModelWrapper:
    def __init__(self, model_path):
        self.model = YOLO(model_path)
    def  run_bowler_detection(self):
        results = self.model.predict(source="./Storage/extracted_frames",stream=True)
        results_list = []
        for result in results:
            sec = result.path if result.path is not None else None
            bowler = result.boxes.conf.numel()
            results_list.append({'sec': sec[-8:-4].split('_')[0],'bowler':bowler   })
        # Convert the list of dictionaries to a DataFrame
        df = pd.DataFrame(results_list)
        # df.to_csv("./Outputs/CSV/bowler.csv")
        return df

# def main():
#     model_path ="D:\BE Final Year Project\codespace/Model/best.pt"
#     input_source = "./Storage/extracted_frames"

#     yolo_wrapper = YOLOModelWrapper(model_path)
#     detection_results = yolo_wrapper.run_detection(input_source)

# if __name__ == "__main__":
#     main()
