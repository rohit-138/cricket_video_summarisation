import os
import requests
from tqdm import tqdm 

def perform_ocr(api_key, image_path):
    url = 'https://api.ocr.space/parse/image'
    payload = {
        'apikey': api_key,
        'isOverlayRequired': False,
    }

    with open(image_path, 'rb') as image_file:
        files = {'image': image_file}
        response = requests.post(url, files=files, data=payload)
        result = response.json()

    return result

# API key for OCR.space
api_key = 'K86699440688957'

# Folder path containing images
folder_path = r'D:\BE Final Year Project\workspace\runs\detect\predict\crops\scorecard'

# Get a list of image files
image_files = [filename for filename in os.listdir(folder_path) if filename.endswith(('.jpg', '.png', '.jpeg'))]
output_file_path = 'ocr_result.txt'

Process each image in the folder with tqdm
with open(output_file_path, 'w') as output_file:
    for filename in tqdm(image_files, desc="Processing Images"):
        image_path = os.path.join(folder_path, filename)
        result = perform_ocr(api_key, image_path)
        output=result['ParsedResults'][0]['ParsedText']
        # Write the OCR result to the text file
        output_file.write(f"OCR Result for {filename}:\n{output}\n{'='*30}\n")
csv_file_path = 'output.csv'
with open(csv_file_path, 'w', newline='') as csv_file:

    writer = csv.writer(csv_file)

    # Write header (optional)
    writer.writerow(['Column 1', 'Column 2'])
    for filename in tqdm(image_files, desc="Processing Images"):
        image_path = os.path.join(folder_path, filename)
        result = perform_ocr(api_key, image_path)
        output=result['ParsedResults'][0]['ParsedText']
        # Write the OCR result to the text file
        # output_file.write(f"OCR Result for {filename}:\n{output}\n{'='*30}\n")
        writer.writerow([filename[-4:], output])

    # Write data row
print(f"OCR results written to: {output_file_path}")
