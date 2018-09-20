#Author Anqi Guo
import io
import os
from google.cloud import vision
from google.cloud.vision import types

def detect_labels(file_name):
#Dtects labels in the file
    client = vision.ImageAnnotatorClient()

#extract the image file    
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()
#use google api to detect the labels of image
    image = vision.types.Image(content=content)

    response = client.label_detection(image=image)
    labels = response.label_annotations
    print('Labels:')

    for label in labels:
        print(label.description)


#because I downlad 4 images so I used a for loop
if __name__ == '__main__':
    for i in range(4):
        detect_labels('./img00'+str(i)+'.jpg')
