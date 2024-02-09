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
        return df
