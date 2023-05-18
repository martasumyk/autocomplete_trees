"""Module to get uploaded images"""

import os

def get_image():
    """Get images"""
    images = os.listdir("client/images")
    return images

print(get_image())
