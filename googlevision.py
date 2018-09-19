
import io
import os
from google.cloud import vision
from google.cloud.vision import types

def detect_labels(file_name):
    """Detects labels in the file."""
    client = vision.ImageAnnotatorClient()

# 
#    file_name = os.path.join(
 #       os.path.dirname('_file_'),
 #       'img000.jpg')
    # for file in os.listdir():
    #     if file.endswith(".jpg"):
    #         file_name=os.path.join(os.listdir(),file)

    # file_name='./img000.jpg'
    
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.label_detection(image=image)
    labels = response.label_annotations
    print('Labels:')

    for label in labels:
        print(label.description)



if __name__ == '__main__':
    for i in range(4):
        detect_labels('./img00'+str(i)+'.jpg')
