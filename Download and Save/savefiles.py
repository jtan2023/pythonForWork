import os
import requests
from urllib.parse import unquote

url = 'https://clientcentral.yardi.com/cloud_file_manager.aspx?path=h%252fVmntTUHJSv6hjyBbv0jFAKTMmTY%252fUaZOV3DSQ%252fLdtrdlcTwIb2bKAO3cPlhNxp0VGhiECLOVCRBrVvt08QyQtlGITWXzi%252fB95m41pDjw5s%252b9FIgG1p%252f5SqowAX3naQ%252fUfrSvbbPtlakGo4uruxrgONgB68%252b0utdDROgNc8xw0%253d&webID=BFQBnMgiE5YzjrzUQBrk%252fw%253d%253d'
download_dir = 'C:\Users\jtan\OneDrive - Beacon Communities LLC\Desktop\IT\IT Ticket\2023\3\move to TEST\my_new_folder'

if not os.path.exists(download_dir):
    os.makedirs(download_dir)

response = requests.get(url)
content = response.text
lines = content.split('\n')

for line in lines:
    if 'class="name"' in line:
        file_url = line.split('href="')[1].split('"')[0]
        file_name = unquote(file_url.split('/')[-1])
        file_path = os.path.join(download_dir, file_name)
        with open(file_path, 'wb') as f:
            response = requests.get(file_url)
            f.write(response.content)
            print(f'Downloaded {file_name} to {download_dir}')
