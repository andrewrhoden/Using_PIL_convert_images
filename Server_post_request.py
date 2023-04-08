#!/usr/bin/env python3

import os
import requests

# Set the URL for the API endpoint
url = "http://<external-IP>/feedback"

# Define the path to the feedback directory
file_path = "/data/feedback"

# Iterate over each file in the feedback directory
for file in os.listdir(file_path):
    # Check if the file is a text file
    if file.endswith(".txt"):
        # Open the file and read its contents
        with open(os.path.join(file_path, file), "r") as f:
            # Create a dictionary with the feedback data
            feedback = {"title": f.readline().strip(),
                        "name": f.readline().strip(),
                        "date": f.readline().strip(),
                        "feedback": f.readline().strip()}
            # Make a POST request to the API endpoint with the feedback data
            response = requests.post(url, json=feedback)
            # Print the status code and text of the response object
            print("Status code:", response.status_code)
            print("Response text:", response.text)
