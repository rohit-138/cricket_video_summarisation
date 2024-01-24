from moviepy.video.io.VideoFileClip import VideoFileClip
import imageio
import os
class VideoTrimmer:
    def __init__(self, input_path):
        self.input_path = input_path

    # def trim_video(self, start_time, end_time,path):
    #     try:

    #         video_clip = VideoFileClip(self.input_path)
    #         trimmed_clip = video_clip.subclip(start_time, end_time)
    #         trimmed_clip.write_videofile(path, codec="libx264", audio_codec="aac")
    #         video_clip.close()
    #         print(f"Trimmed video saved to {self.path}")
    #     except Exception as e:
    #         print(f"Error: {e}")
def trim_video(input_path, output_path, start_time, end_time):
    # Open the video file
    cap = cv2.VideoCapture(input_path)

    # Get video properties
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    # fourcc = int(cap.get(cv2.CAP_PROP_FOURCC))

    # Calculate start and end frame numbers
    start_frame = int(start_time * fps)
    end_frame = int(end_time * fps)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    # Create VideoWriter object
    out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))

    # Set the video capture position to the start frame
    cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)

    # Read and write frames until the end frame
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret or cap.get(cv2.CAP_PROP_POS_FRAMES) > end_frame:
            break

        # Write the frame to the output video
        out.write(frame)

    # Release video capture and writer objects
    cap.release()
    out.release()

    print("Trimmed video saved at:", output_path)
input_video_path = "D:\BE Final Year Project\inputs\eight.mp4"
output_video_path = "D:\BE Final Year Project\output"
# start_time_seconds = 10
# end_time_seconds = 30

# video_trimmer = VideoTrimmer(input_video_path, output_video_path)
# video_trimmer.trim_video(start_time_seconds, end_time_seconds)
# data={'fours': [181, 261, 284, 302, 317, 330, 389, 454, 537, 685, 719, 800, 880, 910, 973], 'sixes': [207, 239, 2452, 255, 263, 269, 286, 291, 351, 520, 745, 793, 871], 'wickets': [349, 406, 552, 606, 822]}
data={'fours': [181, 261], 'sixes': [207, 239], 'wickets': [349, 406, 552]}
video_trimmer = VideoTrimmer(input_video_path)
for key,value in data.items():
    for item in value:
        filename=f"{item}.mp4"
        path=os.path.join(output_video_path,key)
        print("path is is "+ path)
        video_trimmer.trim_video(item-5, item+5,path)