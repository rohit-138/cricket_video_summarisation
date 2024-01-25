from moviepy.video.io.VideoFileClip import VideoFileClip
import imageio
import os,shutil
import cv2

class VideoTrimmer:
    def __init__(self, input_path):
        self.input_path = input_path
        

    def trim_video(self, start_time, end_time,path):
        try:

            video_clip = VideoFileClip(self.input_path).subclip(start_time, end_time)
            video_clip.write_videofile(path)
            video_clip.close()
            print(f"Trimmed video saved to '{self.input_path}'")
        except Exception as e:
            print(f"Error: {e}")


    
# start_time_seconds = 10
# end_time_seconds = 30

# video_trimmer = VideoTrimmer(input_video_path, output_video_path)
# video_trimmer.trim_video(start_time_seconds, end_time_seconds)
# data={'fours': [181, 261, 284, 302, 317, 330, 389, 454, 537, 685, 719, 800, 880, 910, 973], 'sixes': [207, 239, 2452, 255, 263, 269, 286, 291, 351, 520, 745, 793, 871], 'wickets': [349, 406, 552, 606, 822]}
# data={'fours': [181, 261]}
data={'fours': [181, 261], 'sixes': [207, 239], 'wickets': [349, 406, 552]}
video_trimmer = VideoTrimmer("D:\BE Final Year Project\inputs/nine.mp4")
for key,value in data.items():
    filepath=f"Outputs/{key}"
    if os.path.exists(filepath):#if already exists delete
            print(f"'{filepath}' exists already. Attempting delete!")
            try:
                # Remove the folder and its contents
                shutil.rmtree(filepath)
                print(f"Removed older version of '{filepath}' and Created new one of it ")
                os.makedirs(filepath)


            except Exception as e:
                print(f"Error removing folder '{filepath}': {e}")
    else:
        os.makedirs(filepath)
for key,value in data.items():
    for item in value:

        filepath=f"Outputs/{key}/{item}.mp4"
        video_trimmer.trim_video(item-5, item+5,filepath)