import pandas as pd
import os
from frame_extractor import FrameExtractor
from text_extractor import TextExtractionUsingOCR
from scoreboard_extractor import YOLOScorecardModelWrapper
from bowler_extractor import YOLOBowlerModelWrapper
from video_editor import VideoEditor
from process_summary import ProcessSummary
if __name__ == "__main__":
    video_path = "D:\BE Final Year Project\inputs/nine.mp4"
    scorecard_model_path="../Model/best.pt"
    bowler_model_path="../Model/bowler.pt"
    if not os.path.exists('./Outputs/CSV'):
        os.makedirs('./Outputs/CSV')
    # Frame Extraction
    frame_extractor = FrameExtractor(video_path)
    # frame_extractor.extract_frames_by_framecount(5)#enter appropriate frame count
    frame_extractor.extract_frames_by_percentage(100)
    print("Frames extracted successfully.")
    #finding Scoreboard using yolo

    yolo_wrapper = YOLOScorecardModelWrapper(scorecard_model_path)
    scorecard_df = yolo_wrapper.run_scorecard_detection()

    yolo_wrapper = YOLOBowlerModelWrapper(bowler_model_path)
    bowler_df = yolo_wrapper.run_bowler_detection()

    merged_df=pd.merge(scorecard_df,bowler_df,on='sec',how='inner')
    #getting text from scoreboard
    merged_df.to_csv("./CSV/merged_df.csv")

    text_extractor = TextExtractionUsingOCR()


    df=text_extractor.extract_text()
    df.to_csv('./CSV/ocr_data.csv')
    data=ProcessSummary().process_summary(df,merged_df)
    print(data)

    # data={'fours': [181, 261]}
    video_trimmer=VideoEditor(video_path)
    video_trimmer.generate_summary_videos(data,left=20,right=5)




