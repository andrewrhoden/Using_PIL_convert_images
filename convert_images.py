#!/usr/bin/env python3

from PIL import Image
import os

source_path = "edit_sourceImage_path/images/"
save_path = "/opt/icons/"

for filename in os.listdir(source_path):
    if not filename.startswith('.'):
        with Image.open(os.path.join(source_path, filename)) as image:
            # Rotate the image 90 degrees clockwise
            rotated_image = image.rotate(-90, expand=True)
            # Resize the image from 192x192 to 128x128
            resized_image = rotated_image.resize((128, 128))
            # Save the image to a new folder in JPEG format
            new_filename = os.path.splitext(filename)[0] + ".jpeg"
            resized_image.convert('RGB').save(os.path.join(save_path,new_filename), "JPEG")