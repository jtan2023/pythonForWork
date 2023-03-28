import os
import zipfile

# Define the path to the folder containing the zip files
zip_folder_path = r'C:\Users\jtan\OneDrive - Beacon Communities LLC\Desktop\IT\IT Ticket\2023\3\move to TEST\my_new_folder'

# Define the path to the folder where you want to save the extracted files
extract_folder_path = r'C:\Users\jtan\OneDrive - Beacon Communities LLC\Desktop\IT\IT Ticket\2023\3\move to TEST\my_new_folder2'

# Loop through all the files in the zip folder
for file_name in os.listdir(zip_folder_path):
    # Check if the file is a zip archive
    if file_name.endswith('.zip'):
        # Open the zip archive
        with zipfile.ZipFile(os.path.join(zip_folder_path, file_name), 'r') as zip_file:
            # Extract all the files from the archive to the extract folder
            zip_file.extractall(extract_folder_path)
