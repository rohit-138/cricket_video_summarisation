from ultralytics import YOLO
model = YOLO('../Model/bowler.pt')

video_path = "D:\BE Final Year Project\inputs/nine.mp4"

model.predict(source=video_path,save=True,conf=0.4,project='./Storage/output')