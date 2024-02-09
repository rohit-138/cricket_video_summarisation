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
    video_path = r"D:\BE Final Year Project/inputs/nine.mp4"
    scorecard_model_path="./model/best.pt"
    bowler_model_path="./model/bowler.pt"
    if not os.path.exists('./Outputs/CSV'):
        os.makedirs('./Outputs/CSV')
    # Frame Extraction
    print("*****step 1 ******")
    s1_start_time=time.time()
    frame_extractor = FrameExtractor(video_path)
    # frame_extractor.extract_frames_by_framecount(5)#enter appropriate frame count
    frame_extractor.extract_frames_by_percentage()
    print("Frames extracted successfully.")
    s1_end_time=time.time()
    
    #finding Scoreboard using yolo
    s2_start_time=time.time()
    print("*****step 2******")

    yolo_wrapper = YOLOScorecardModelWrapper(scorecard_model_path)
    scorecard_df = yolo_wrapper.run_scorecard_detection()

    s2_end_time=time.time()

    print("*****step 3 ******")

    s3_start_time=time.time()
    yolo_wrapper = YOLOBowlerModelWrapper(bowler_model_path)
    bowler_df = yolo_wrapper.run_bowler_detection()

    merged_df=pd.merge(scorecard_df,bowler_df,on='sec',how='inner')
    #getting text from scoreboard
    merged_df.to_csv("./Outputs/CSV/merged_df.csv")
    s3_end_time=time.time()
    print("*****step 4 ******")

    s4_start_time=time.time()

    text_extractor = TextExtractionUsingOCR()
    df=text_extractor.extract_text()
    df.to_csv('./Outputs/CSV/ocr_data.csv')


    s4_end_time=time.time()
    print("*****step 5 ******")

    s5_start_time=time.time()
    data=ProcessSummary().process_summary(df,merged_df)
    print(data)
    s5_end_time=time.time()
    print("*****step 6 ******")

    s6_start_time=time.time()
    video_trimmer=VideoEditor(video_path,data)
    video_trimmer.generate_summary_videos()
    video_trimmer.generate_full_summary()
    s6_end_time=time.time()


    end_time=time.time()

    Total_time=end_time-start_time
    step_1_time=s1_end_time-s1_start_time
    step_2_time=s2_end_time-s2_start_time
    step_3_time=s3_end_time-s3_start_time
    step_4_time=s4_end_time-s4_start_time
    step_5_time=s5_end_time-s5_start_time
    step_6_time=s6_end_time-s6_start_time


    print("Total execution time:", end_time-start_time  , "seconds")
    print("Step 1 execution time:", s1_end_time-s1_start_time, "seconds",((step_1_time*100)/Total_time)," %")
    print("Step 2 execution time:", s2_end_time-s2_start_time, "seconds",((step_2_time*100)/Total_time)," %")
    print("Step 3 execution time:", s3_end_time-s3_start_time, "seconds",((step_3_time*100)/Total_time)," %")
    print("Step 4 execution time:", s4_end_time-s4_start_time, "seconds",((step_4_time*100)/Total_time)," %")
    print("Step 5 execution time:", s5_end_time-s5_start_time, "seconds",((step_5_time*100)/Total_time)," %")
    print("Step 6 execution time:", s6_end_time-s6_start_time, "seconds",((step_6_time*100)/Total_time)," %")

