import os
import cv2
import pytesseract
import re
from tqdm import tqdm


class TextExtractionUsingOCR:
    def __init__(self, folder_path, output_file_name):
        self.folder_path = folder_path
        self.output_file_path = (
            "D:\BE Final Year Project\workspace\output\ocr_output/" + output_file_name
        )
        print(self.output_file_path)

        pytesseract.pytesseract.tesseract_cmd = (
            r"C:/Program Files/Tesseract-OCR/tesseract.exe"
        )
        print(f"Applying OCR on files in  {self.folder_path}")

    def extract_text(self, image_path):
        text = pytesseract.image_to_string(image_path, config="--psm 13")
        return text

    def process_frames(self):
        # Open the text file in write mode
        with open(self.output_file_path, "w") as output_file:
            # Get the total number of frames for the progress bar
            total_frames = len(
                [
                    f
                    for f in os.listdir(self.folder_path)
                    if f.endswith((".png", ".jpg", ".jpeg"))
                ]
            )
            # Initialize the tqdm progress bar
            for frame_name in tqdm(
                os.listdir(self.folder_path),
                total=total_frames,
                desc="Processing Frames",
            ):
                # for frame_name in os.listdir(self.folder_path):
                if frame_name.endswith((".png", ".jpg", ".jpeg")):
                    frame_path = os.path.join(self.folder_path, frame_name)
                    # Extract text from the current frame
                    scorecard_text = self.extract_text(frame_path)
                    pattern = r"\b\s*\d+\s*-\s*\d+\b"
                    match = re.findall(pattern, scorecard_text)
                    output_file.write(
                        f"frameNo{frame_name}=>{scorecard_text}-------{match}\n\n"
                    )
        print(f"Extracted text has been saved to {self.output_file_path}")


def main():
    frames_folder = (
        "D:\BE Final Year Project\workspace/runs\detect\predict\crops\scorecard"
    )
    # output_file_path="D:\BE Final Year Project\workspace\ocrouput\c.txt"
    textextractor = TextExtractionUsingOCR(frames_folder, "3.txt")
    textextractor.process_frames()


if __name__ == "__main__":
    main()
