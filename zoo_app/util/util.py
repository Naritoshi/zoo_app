import base64
import os

def create_image_data(img):
    encoded = base64.b64encode(img).decode()
    mime = "image/jpg"
    mime = mime + ";" if mime else ";"
    input_image = "data:%sbase64,%s" % (mime, encoded)  
    return input_image

def get_extntion(filepath):
    _, ext = os.path.splitext(filepath)
    return ext