import os
import cv2
import pytesseract
import re
from tqdm import tqdm

class TextExtractionUsingOCR:
    def __init__(self, folder_path, output_file_path):
        self.folder_path = folder_path
        self.output_file_path = f"D:\BE Final Year Project\workspace\output\ocr_output\{output_file_path}"

        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        # Set the path to the Tesseract executable (update this based on your installation)
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        print(f"Applying OCR on files in  {self.folder_path}")

    def extract_text(self, image_path):
        # Read the image using OpenCV
        img = cv2.imread(image_path,0)

        # Convert the image to grayscale
        # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        _, bw_img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

        # Use Tesseract to do OCR on the image
        text = pytesseract.image_to_string(bw_img)

        return text

    def process_frames(self):
        # Open the text file in write mode
        with open(self.output_file_path, 'w') as output_file:

            # Get the total number of frames for the progress bar
            total_frames = len([f for f in os.listdir(
                self.folder_path) if f.endswith(('.png', '.jpg', '.jpeg'))])

            # Initialize the tqdm progress bar
            for frame_name in tqdm(os.listdir(self.folder_path), total=total_frames, desc="Processing Frames"):
            # for frame_name in os.listdir(self.folder_path):
                if frame_name.endswith(('.png', '.jpg', '.jpeg')):
                    frame_path = os.path.join(self.folder_path, frame_name)

                    # Extract text from the current frame
                    scorecard_text = self.extract_text(frame_path)

                    pattern = r'\b\s*\d+\s*-\s*\d+\b'

                    match = re.findall(pattern, scorecard_text)
                    # print(match)
                    # if len(match) > 0 :
                    #     output_file.write(f'frameNo{frame_name}=>{scorecard_text}')   
                    output_file.write(f'frameNo{frame_name}=>{scorecard_text}\n\n')          
                    # runs_match = re.search(
                    #     r'(\d+)(\s)+-(\d+)', scorecard_text)
                    # wickets_match = re.search(
                    #     r'(\d+)\s+wickets', scorecard_text)
                    # team_name_match = re.search(
                    #     r'(\w+)\s+\(\d+-\d+', scorecard_text)

                    # Initialize variables with default values
                    # runs = None
                    # wickets = None
                    # team_name = None 

                    # Update variables if matches are found
                    # if runs_match:
                    #     # Format runs as "336-6"
                    #     runs = f"{runs_match.group(1)}-{runs_match.group(2)}"
                    #     output_file.write(
                    #         f'Text from {frame_name}:\n{runs}\n\n')
                    # if wickets_match:
                    #     wickets = wickets_match.group(1)
                        
                    # if team_name_match:
                    #     team_name = team_name_match.group(1)

                    # # Print or write the extracted information
                    # print(f"{team_name}-{runs}-{wickets}")

                    # if runs_match or wickets_match or team_name_match:
                        # print("true")
                    

        print(f'Extracted text has been saved to {self.output_file_path}')

# Example usage:
# folder_path = r"D:\BE Final Year Project\workspace\extracted_frames"
# # folder_path = r"D:\BE Final Year Project\workspace\runs\detect\predict\crops\scorecard"
# output_file_path = "3.txt"

# text_extractor = TextExtractionUsingOCR(folder_path, output_file_path)
# text_extractor.process_frames()
