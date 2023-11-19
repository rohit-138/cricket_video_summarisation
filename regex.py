import re

# Define your regular expression
pattern = r'\b\s*\d+\s*-\s*\d+\b'

    # runs_match = re.search(r'(\d+)(\s)+-(\d+)', content)
    # wickets_match = re.search(r'(\d+)\s+wickets', content)
    # team_name_match = re.search(r'(\w+)\s+\(\d+-\d+', content)
# Open the input file for reading
with open('./ocroutput.txt', 'r') as input_file:
    # Read the content of the file
    content = input_file.read()

    # Use the regular expression to extract text
    matches = re.findall(pattern, content)

# Open the output file for writing
with open('output1.txt', 'w') as output_file:
    # Write the extracted text to the output file
    for match in matches:
        output_file.write(match + '\n')
