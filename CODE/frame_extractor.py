import cv2#frame extraction
import os,shutil
from tqdm import tqdm

class FrameExtractor:
    def __init__(self, video_path):
        self.video_path = video_path
        self.cap = cv2.VideoCapture(video_path)
        if self.cap.isOpened():
            print(f"The video file at '{video_path}' is valid.")
        else:
            raise ValueError(f"Failed to open the video file at '{video_path}'.") 

        self.fps = int(self.cap.get(cv2.CAP_PROP_FPS))
        self.total_frames = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))
        self.total_length_seconds = self.total_frames // self.fps
        self.frame_count = 0
        self.extracted_frames="./Storage/extracted_frames"
        if os.path.exists(self.extracted_frames):#if already exists delete it and recreate
            print(f"'{self.extracted_frames}' exists already. Attempting delete!")
            try:
                # Remove the folder and its contents
                shutil.rmtree(self.extracted_frames)
                print(f"Removed older version of '{self.extracted_frames}' and recreated it")
                os.makedirs(self.extracted_frames)

            except Exception as e:
                print(f"Error removing folder '{self.extracted_frames}': {e}")
        else:#recreate path
            os.makedirs(self.extracted_frames)
        print(f"Total video length: {self.total_length_seconds} seconds")
        print(f"FPS OF VIDEO :{self.fps}")

    def extract_frames_by_percentage(self, percentage=100):
        if percentage < 0 or percentage > 100:
            raise ValueError("Percentage must be between 0 and 100")

        frames_to_extract = int(self.total_length_seconds * (percentage / 100))
        progress_bar = tqdm(total=frames_to_extract, desc="Extracting Frames")
        # print(f" frames_to_extract: {frames_to_extract}")

        while self.frame_count < frames_to_extract:
            ret, frame = self.cap.read()
            if not ret:
                break
            frame_filename = os.path.join(self.extracted_frames, f"frame_{self.frame_count:04d}.jpg")
            cv2.imwrite(frame_filename, frame)
            self.frame_count += 1
            self.cap.set(cv2.CAP_PROP_POS_FRAMES, self.frame_count * self.fps)
            progress_bar.update(1)
        progress_bar.close()
        self.cap.release()
    def extract_frames_by_framecount(self, frames_to_extract):
        progress_bar = tqdm(total=frames_to_extract, desc="Extracting Frames")
        while self.frame_count < frames_to_extract:
            ret, frame = self.cap.read()
            if not ret:
                break
            frame_filename = os.path.join(self.extracted_frames, f"frame_{self.frame_count:04d}.jpg")
            cv2.imwrite(frame_filename, frame)
            self.frame_count += 1
            self.cap.set(cv2.CAP_PROP_POS_FRAMES, self.frame_count * self.fps)
            progress_bar.update(1)
        progress_bar.close()
        self.cap.release()

        
