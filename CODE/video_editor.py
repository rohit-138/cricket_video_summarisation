from moviepy.editor import VideoFileClip,concatenate_videoclips   
import os,shutil
import cv2

class VideoEditor:
    def __init__(self, input_path,data):
        self.input_path = input_path
        self.data=data

    def trim_video(self, start_time, end_time,path):
        try:
            video_clip = VideoFileClip(self.input_path).subclip(start_time, end_time)
            video_clip.write_videofile(path)
            video_clip.close()
            print(f"Trimmed video saved to '{self.input_path}'")
        except Exception as e:
            print(f"Error: {e}")
    
    def generate_full_summary(self):
        paths={'fours':r"./Inputs/four_animation.mp4",'sixs':r"./Inputs/six_animation.mp4",
        'wickets':r"./Inputs/wicket_animation.mp4"}
       
        
       
        try:
            allclips=[]
            for key,value in self.data.items():
                for event in value:

                    print(paths[key])
                    transition_animation=VideoFileClip(paths[key])#todo
                    clip=VideoFileClip(self.input_path).subclip(event[0], event[1])
                    transition_animation = transition_animation.resize(width=clip.size[0], height=clip.size[1])
                    allclips.append(transition_animation)
                    allclips.append(clip)
                    # clip.close()
            final_clip=concatenate_videoclips(allclips)  
            final_clip.write_videofile("./Outputs/full_length_output.mp4") 
            

        except Exception as e:
            print(f"Error:{e}")
        # finally:
        #     clip.close()
        #     final_clip.close()
        #     transition_animation.close()
    def generate_summary_videos(self):

        for key,value in self.data.items():
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
        for key,value in self.data.items():
            for item in value:
                filepath=f"Outputs/{key}/{item}.mp4"
                self.trim_video(item[0], item[1],filepath)

        
# def main():
#     video_path = "D:\BE Final Year Project\inputs/nine.mp4"
#     # data={'fours': [(198, 217)], 'sixs': [(217, 237)], 'wickets': [(28, 56), (88, 109)]}
#     data={'fours': [(198, 217)], 'sixs': [(217, 237)]}
#     video_trimmer=VideoEditor(video_path,data)
#     # video_trimmer.generate_summary_videos()
#     video_trimmer.generate_full_summary()

# # if __name__ == "__main__":
    # main()