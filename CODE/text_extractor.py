import os
import csv
import pytesseract
import re
from tqdm import tqdm
import pandas as pd

class TextExtractionUsingOCR:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        pytesseract.pytesseract.tesseract_cmd = (
            r"C:/Program Files/Tesseract-OCR/tesseract.exe"
        )

    def extract_text(self, image_path):
        text = pytesseract.image_to_string(image_path, config="--psm 13")
        return text

    def process_frames(self):
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
            desc="Processing Frames",
        ):
            if frame_name.endswith((".png", ".jpg", ".jpeg")):
                frame_path = os.path.join(self.folder_path, frame_name)
                scorecard_text = self.extract_text(frame_path)
                pattern = r"\b\s*\d+\s*-\s*\d+\b"
                match = re.findall(pattern, scorecard_text)
                
                if len(match)>0:
                    match_split=match[0].split('-')
                    temp=[frame_name.split('_')[1][:-4], match_split[0],match_split[1]]
                    ocr_data.append(temp)
        
        columns=['secs','runs','wickets']

        df=pd.DataFrame(ocr_data,columns=columns)
        df['runs'] = pd.to_numeric(df['runs'], errors='coerce')
        df['wickets'] = pd.to_numeric(df['wickets'], errors='coerce')
        df['secs'] = pd.to_numeric(df['secs'], errors='coerce')
        run_diff = df['runs'].diff()
        wickets_diff=df['wickets'].diff()
        increase_by_4 = df[run_diff == 4]
        increase_by_6 = df[run_diff == 6]
        increase_by_1=df[wickets_diff==1]
        processed_data={'fours':increase_by_4['secs'].tolist(),'sixes': increase_by_6['secs'].tolist(),'wickets':increase_by_1['secs'].tolist()}
        return processed_data

from video_editor import VideoTrimmer
def main():
    frames_folder = (
        "D:\BE Final Year Project\workspace/runs\detect\predict\crops\scorecard"
    )
    input_video_path = "D:\BE Final Year Project\inputs\eight.mp4"
    output_video_path = "D:\BE Final Year Project\output"
    # output_file_path="D:\BE Final Year Project\workspace\ocrouput\c.txt"
    textextractor = TextExtractionUsingOCR(frames_folder)
    data=textextractor.process_frames()
    print(data)
    video_trimmer = VideoTrimmer(input_video_path, output_video_path)
    for key,value in data.items():
        for item in value:
            filename=f"{key}/item"
            path=os.path.join(output_video_path,key,value)
            video_trimmer.trim_video(item-5, item+5,path)
if __name__ == "__main__":
    main()
