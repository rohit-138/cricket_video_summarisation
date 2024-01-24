from frame_extractor import FrameExtractor
from text_extractor import TextExtractionUsingOCR
from yolo import YOLOModelWrapper
if __name__ == "__main__":
    video_path = "D:\BE Final Year Project\inputs\one"
    extracted_frame_dir = "D:\BE Final Year Project\workspace\outputs\extracted_frames"
    # Frame Extraction
    # frame_extractor = FrameExtractor(video_path, extracted_frame_dir)
    # frame_extractor.extract_frames_by_framecount(1000)#enter appropriate frame count
    # # frame_extractor.extract_frames_by_percentage(60)
    # print("Frames extracted successfully.")

    # # #finding Scoreboard using yolo
    # model_path = "D:\BE Final Year Project\models\Anand_dataset.pt"
    # model_input_source_path = extracted_frame_dir
    
    # yolo_wrapper = YOLOModelWrapper(model_path)
    # detection_results = yolo_wrapper.run_detection(model_input_source_path)

    # #getting text module
    # # input_text_extractor=r"D:\BE Final Year Project\workspace\runs\detect\predict\crops\scorecard"
    # input_text_extractor="D:\BE Final Year Project\workspace\output\extracted_frames"
    # text_file_name=input("Enter text file name ")
    text_extractor = TextExtractionUsingOCR(input_text_extractor, text_file_name)
    text_extractor.process_frames()



