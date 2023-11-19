import os
import csv
from tqdm import tqdm
import requests
import re

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

# Your OCR.space API key
api_key = 'K87901128888957'
# Folder path containing images
folder_path = r'D:\BE Final Year Project\workspace\runs\detect\predict\crops\scorecard'
# Get a list of image files
image_files = [filename for filename in os.listdir(folder_path) if filename.endswith(('.jpg', '.png', '.jpeg'))]
# Output CSV file path
output_csv_path = 'result_ocr.csv'


parsed_text_pattern = re.compile(r'"ParsedText":"(.*?)"')
# Process each image in the folder with tqdm
with open(output_csv_path, 'w', newline='') as output_csv_file:
    csv_writer = csv.writer(output_csv_file)
    
    # Write header
    csv_writer.writerow(['Filename', 'OCR Result'])

    for filename in tqdm(image_files, desc="Processing Images"):
        image_path = os.path.join(folder_path, filename)
        result = perform_ocr(api_key, image_path)
        
        output=re.findall(parsed_text_pattern,result)
        csv_writer.writerow([filename, result])
                
print(f"OCR results written to: {output_csv_path}")
