import cv2#frame extraction
import os#
from tqdm import tqdm

class FrameExtractor:
    def __init__(self, video_path, output_dir):
        self.video_path = video_path
        self.output_dir = output_dir
        self.cap = cv2.VideoCapture(video_path)
        self.fps = int(self.cap.get(cv2.CAP_PROP_FPS))
        self.total_frames = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))
        self.total_length_seconds = self.total_frames // self.fps
        self.frame_count = 0

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        print(f"outputdir of frameextractor is {output_dir}")
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
            
            frame_filename = os.path.join(self.output_dir, f"frame_{self.frame_count:04d}.jpg")
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

            frame_filename = os.path.join(self.output_dir, f"frame_{self.frame_count:04d}.jpg")
            cv2.imwrite(frame_filename, frame)

            self.frame_count += 1
            self.cap.set(cv2.CAP_PROP_POS_FRAMES, self.frame_count * self.fps)

            progress_bar.update(1)

        progress_bar.close()
        self.cap.release()

        
