from docx import Document
import re

file_path = r"C:\Users\jtan\OneDrive - Beacon Communities LLC\Desktop\IT\IT Ticket\2023\7\Test\y_brm_1st_Rent_ ReminderALLStates.docx"

# Load the Word document
doc = Document(file_path)

# Find all tokens using regex pattern
tokens = []
pattern = r"<<(.*?)>>"
for paragraph in doc.paragraphs:
    matches = re.findall(pattern, paragraph.text)
    tokens.extend(matches)

# Print the tokens
print("Tokens found:")
for token in tokens:
    print(token)
