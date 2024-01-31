from moviepy.editor import VideoFileClip


clip1=VideoFileClip("D:\BE Final Year Project\inputs/nine.mp4").subclip(10,20)
clip1.write_videofile("cliped video.mp4")
print("done")