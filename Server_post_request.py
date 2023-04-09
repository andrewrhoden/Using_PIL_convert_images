#!/usr/bin/env python3

import os
import requests

 

# Set the directory containing the feedback files
feed_path = "/data/feedback"

# Get a list of all .txt files in the feedback directory
feedback_files = [file for file in os.listdir(feed_path) if file.endswith(".txt")]

# Iterate over each file and extract the information
for file in feedback_files:
    with open(os.path.join(feed_path, file)) as f:
        lines = f.readlines()
        feedback = {
            "title": lines[0].strip(),
            "name": lines[1].strip(),
            "date": lines[2].strip(),
            "feedback": lines[3].strip(),
        }
        response = requests.post("http://<url>/feedback", json=feedback)
        if response.status_code != 201:
            print(f"Error posting feedback for {file}: {response.status_code} {response.text}")
            
            
             