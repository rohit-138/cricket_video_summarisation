import cv2
import os
from tqdm import tqdm

def extract_frames(video_path, output_dir):
    # Open the video file

    cap = cv2.VideoCapture(video_path)

    # Get frames per second (FPS) of the video
    fps = int(cap.get(cv2.CAP_PROP_FPS))

    # Get the total number of frames in the video
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    progress_bar = tqdm(total=total_frames, desc="Extracting Frames")
    # Calculate the total length of the video in seconds
    total_length_seconds = total_frames // fps

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    frame_count = 0

    while True:
        ret, frame = cap.read()
        print("Progress:-  ",frame_count,"out of ",total_length_seconds)

        if not ret:
            break

        # Save the frame as an image
        frame_filename = os.path.join(output_dir, f"frame_{frame_count:04d}.jpg")
        cv2.imwrite(frame_filename, frame)

        frame_count += 1

        # Move to the next second in the video
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_count * fps)

    # Release the video capture object
    cap.release()

if __name__ == "__main__":
    video_path = input("Enter the path to the video file: ")
    output_dir = input("Enter the directory to save frames: ")

    # video_path="D:/BE Final Year Project/Implementation/input_video.mp4"
    # output_dir="D:\BE Final Year Project\Implementation\frames"

    extract_frames(video_path, output_dir)

    print("Frames extracted successfully.")
