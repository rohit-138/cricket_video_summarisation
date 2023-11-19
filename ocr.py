import os
import cv2
import pytesseract
import re

# Set the path to the Tesseract executable (update this based on your installation)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Function to extract text from an image
def extract_text(image_path):
    # Read the image using OpenCV
    img = cv2.imread(image_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Use Tesseract to do OCR on the image
    text = pytesseract.image_to_string(gray)

    return text

# Path to the folder containing frames
folder_path = "D:\BE Final Year Project\workspace\output"

# Output text file
output_file_path = "output_text.txt"

# Open the text file in write mode
with open(output_file_path, 'w') as output_file:

    # Loop through each frame in the folder
    for frame_name in os.listdir(folder_path):
        if frame_name.endswith(('.png', '.jpg', '.jpeg')):
            frame_path = os.path.join(folder_path, frame_name)

            # Extract text from the current frame
            scorecard_text = extract_text(frame_path)

            runs_match = re.search(
                r'(\d+)-(\d+)\s+NEED\s+(\d+)\s+TO WIN', scorecard_text)
            wickets_match = re.search(r'(\d+)\s+wickets', scorecard_text)
            team_name_match = re.search(
                r'(\w+)\s+\(\d+-\d+', scorecard_text)

            # Initialize variables with default values
            runs = "N/A"
            wickets = "N/A"
            team_name = "N/A"

            # Update variables if matches are found
            if runs_match:
                # Format runs as "336-6"
                runs = f"{runs_match.group(1)}-{runs_match.group(2)}"
            if wickets_match:
                wickets = wickets_match.group(1)
            if team_name_match:
                team_name = team_name_match.group(1)
            
            # if text is not None:

            #     p_text=re.search("\d{-}\d")
            #     if p_text is not None:
            print(f'Text from {frame_name}')
            if (team_name != "N/A") or (wickets != "N/A") or (runs != 'N/A'):
                output_file.write(f'Text from {frame_name}:\n{runs}\t{wickets}\t{team_name}\n\n')

print(f'Extracted text has been saved to {output_file_path}')
