import cv2

def trim_video_with_audio(input_path, output_path, start_time, end_time):
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
output_video_path = r"D:\BE Final Year Project/output/output_video.fmp4"  # or another valid video file extension
start_time_seconds = 100  # Start time in seconds
end_time_seconds = 110   # End time in seconds

trim_video_with_audio(input_video_path, output_video_path, start_time_seconds, end_time_seconds)
