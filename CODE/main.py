from frame_extractor import FrameExtractor
from text_extractor import TextExtractionUsingOCR
from scoreboard_extractor import YOLOModelWrapper
from video_editor import VideoEditor
if __name__ == "__main__":
    video_path = "D:\BE Final Year Project\inputs/nine.mp4"
    # Frame Extraction
    frame_extractor = FrameExtractor(video_path)
    # frame_extractor.extract_frames_by_framecount(100)#enter appropriate frame count
    frame_extractor.extract_frames_by_percentage(100)
    print("Frames extracted successfully.")

    # # #finding Scoreboard using yolo
    yolo_model_path="../Model/best.pt"
    yolo_wrapper = YOLOModelWrapper(yolo_model_path)
    detection_results = yolo_wrapper.run_detection()

    #getting text from scoreboard

    text_extractor = TextExtractionUsingOCR()
    data=text_extractor.process_frames()
    print(data)

    # data={'fours': [181, 261]}
    video_trimmer=VideoEditor(video_path)
    video_trimmer.generate_summary_videos(data,left=20,right=5)




