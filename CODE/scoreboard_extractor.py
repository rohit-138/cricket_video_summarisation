from ultralytics import YOLO
import os,shutil
import pandas as pd
class YOLOScorecardModelWrapper:
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
        
    def  run_scorecard_detection(self):
        results = self.model.predict(source="./Storage/extracted_frames", conf=0.4, save_crop=True)
        # print(results)
        # print(type(results))
        results_list = []
        for result in results:
            sec = result.path if result.path is not None else None
            scorecard = result.boxes.conf.numel()
            results_list.append({'sec': sec[-8:-4].split('_')[0],'scorecard':scorecard   })

        # Convert the list of dictionaries to a DataFrame
        df = pd.DataFrame(results_list)
        # df.to_csv("./Outputs/CSV/scorecard.csv")
        return df

def main():
    model_path ="D:\BE Final Year Project\workpace/Model/best.pt"
    input_source = "D:\BE Final Year Project\inputs/nine.mp4"

    yolo_wrapper = YOLOScorecardModelWrapper(model_path)
    detection_results = yolo_wrapper.run_detection(input_source)

if __name__ == "__main__":
    main()
