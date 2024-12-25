

import requests

# URL of the raw Python file in GitHub
url = "https://raw.githubusercontent.com/Pirathayinie5/hello-python/refs/heads/main/hello.py"

# Fetch the content of the file
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Print the content of the Python file
    print("Successfully fetched the file content:")
    print(response.text)
else:
    print("Failed to fetch the file. Status code:", response.status_code)
