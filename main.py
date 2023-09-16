from frame_extractor import FrameExtractor

# D:\BE Final Year Project\Implementation\input_video.mp4
# D:\BE Final Year Project\Implementation\frames
if __name__ == "__main__":
    # video_path = input("Enter the path to the video file: ")
    video_path = "D:\BE Final Year Project\Implementation\input_video.mp4"
    output_dir = input("Enter the directory to save frames: ")

    frame_extractor = FrameExtractor(video_path, output_dir)
    # frame_extractor.extract_frames_by_framecount(10)
    frame_extractor.extract_frames_by_percentage(10)

    print("Frames extracted successfully.")
