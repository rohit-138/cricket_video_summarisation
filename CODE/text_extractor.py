import os
import csv
import pytesseract
import re
from tqdm import tqdm
import pandas as pd
"""
TODO
separating runs and wickets only by - .try other symbols
"""
class TextExtractionUsingOCR:
    def __init__(self):
        self.folder_path = "./runs/detect/predict/crops/scorecard"
        pytesseract.pytesseract.tesseract_cmd = (
            r"C:/Program Files/Tesseract-OCR/tesseract.exe"
        )

    def apply_ocr(self, image_path):
        text = pytesseract.image_to_string(image_path, config="--psm 13")
        # text = pytesseract.image_to_string(image_path)

        return text

    def extract_text(self):
        ocr_data=[]
        total_frames = len(
                [
                    f
                    for f in os.listdir(self.folder_path)
                    if f.endswith((".png", ".jpg", ".jpeg"))
                ]
            )
        for frame_name in tqdm(
            os.listdir(self.folder_path),
            total=total_frames,
            desc="Applying OCR",
        ):
            if frame_name.endswith((".png", ".jpg", ".jpeg")):
                frame_path = os.path.join(self.folder_path, frame_name)
                scorecard_text = self.apply_ocr(frame_path)
                pattern = r"\b\s*\d+\s*-\s*\d+\b"
                match = re.findall(pattern, scorecard_text)
                if len(match)>0:
                    match_split=match[0].split('-')
                    temp=[frame_name.split('_')[1][:-4], match_split[0],match_split[1]]
                    ocr_data.append(temp)
                    # print(temp)
        
        columns=['secs','runs','wickets']

        df=pd.DataFrame(ocr_data,columns=columns)
        df=df.sort_values(by='secs')
        # df.to_csv("ocr_output.csv")
        return df

def main():
    textextractor = TextExtractionUsingOCR()
    df=textextractor.extract_text()
    df.to_csv("ocr_output.csv")

if __name__ == "__main__":
    main()
