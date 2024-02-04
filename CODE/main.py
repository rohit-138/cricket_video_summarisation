import pandas as pd
import os
from frame_extractor import FrameExtractor
from text_extractor import TextExtractionUsingOCR
from scoreboard_extractor import YOLOScorecardModelWrapper
from bowler_extractor import YOLOBowlerModelWrapper
from video_editor import VideoEditor
from process_summary import ProcessSummary
import time

if __name__ == "__main__":
    start_time=time.time()
    video_path = "D:\BE Final Year Project\inputs/nine.mp4"
    scorecard_model_path="../Model/best.pt"
    bowler_model_path="../Model/bowler.pt"
    if not os.path.exists('./Outputs/CSV'):
        os.makedirs('./Outputs/CSV')
    # Frame Extraction
    s1_start_time=time.time()
    frame_extractor = FrameExtractor(video_path)
    # frame_extractor.extract_frames_by_framecount(5)#enter appropriate frame count
    frame_extractor.extract_frames_by_percentage(100)
    print("Frames extracted successfully.")
    s1_end_time=time.time()
    
    #finding Scoreboard using yolo
    s2_start_time=time.time()

    yolo_wrapper = YOLOScorecardModelWrapper(scorecard_model_path)
    scorecard_df = yolo_wrapper.run_scorecard_detection()

    s2_end_time=time.time()
    s3_start_time=time.time()
    yolo_wrapper = YOLOBowlerModelWrapper(bowler_model_path)
    bowler_df = yolo_wrapper.run_bowler_detection()

    merged_df=pd.merge(scorecard_df,bowler_df,on='sec',how='inner')
    #getting text from scoreboard
    merged_df.to_csv("./CSV/merged_df.csv")
    s3_end_time=time.time()

    s4_start_time=time.time()

    text_extractor = TextExtractionUsingOCR()
    df=text_extractor.extract_text()
    df.to_csv('./CSV/ocr_data.csv')


    s4_end_time=time.time()
    s5_start_time=time.time()
    data=ProcessSummary().process_summary(df,merged_df)
    print(data)
    s5_end_time=time.time()
    s6_start_time=time.time()
    video_trimmer=VideoEditor(video_path,data)
    # video_trimmer.generate_summary_videos()
    video_trimmer.generate_full_summary()
    s6_end_time=time.time()


    end_time=time.time()    

    print("Total execution time:", end_time-start_time  , "seconds")
    print("Step 1 execution time:", s1_end_time-s1_start_time, "seconds")
    print("Step 2 execution time:", s2_end_time-s2_start_time, "seconds")
    print("Step 3 execution time:", s3_end_time-s3_start_time, "seconds")
    print("Step 4 execution time:", s4_end_time-s4_start_time, "seconds")
    print("Step 5 execution time:", s5_end_time-s5_start_time, "seconds")
    print("Step 6 execution time:", s6_end_time-s6_start_time, "seconds")

