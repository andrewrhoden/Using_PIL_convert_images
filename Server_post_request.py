#! /usr/bin/env python3

import os
import requests

# Set directory path and URL
dir_path = "/data/feedback/"
url = "http://104.154.51.98/feedback/"

# Loop through each file in directory
for file_name in os.listdir(dir_path):
    # Define keys and dictionary to store feedback data
    keys = ["title", "name", "date", "feedback"]
    feedback_dict = {}
    
    # Open file and read each line to store in dictionary
    with open(dir_path + file_name, "r") as file:
        lines = file.readlines()
        for i in range(len(keys)):
            feedback_dict[keys[i]] = lines[i].strip()

    # Send feedback dictionary as JSON in POST request to URL
    response = requests.post(url, json=feedback_dict)

    # Check if request was successful and print error message if not
    if response.status_code == 201:
        print(f"Feedback {file_name} posted successfully!")
    else:
        print(f"Error posting feedback {file_name}: Status code {response.status_code}")
