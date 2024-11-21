########RESIZE IMAGE #######
import cv2


def calculate_size(scale_percentage, width, height):
  new_width = int(width * scale_percentage / 100)
  new_height = int(height * scale_percentage / 100)
  print("New Dim:", new_width, new_height)
  return (new_width, new_height)


def resize(image_path, scale_percentage, resized_path):
  image = cv2.imread(image_path)
  new_dim = calculate_size(scale_percentage, image.shape[1], image.shape[0])
  resized_image = cv2.resize(image, new_dim)
  cv2.imwrite(resized_path, resized_image)

resize('galaxy.jpeg', 10, 'resized-galaxy.jpeg')

######## RESIZE MULTIPLE IMAGES ############

import cv2
import os


def calculate_size(scale_percentage, width, height):
  new_width = int(width * scale_percentage / 100)
  new_height = int(height * scale_percentage / 100)
  print("New Dim:", new_width, new_height)
  return (new_width, new_height)


def resize(image_path, scale_percentage, resized_path):
  image = cv2.imread(image_path)
  new_dim = calculate_size(scale_percentage, image.shape[1], image.shape[0])
  resized_image = cv2.resize(image, new_dim)
  cv2.imwrite(resized_path, resized_image)

images = os.listdir('images')
for image in images:
  resize(f'images/{image}', 10, f'resized/resized-{image}')

####### DETCT FACE IN IMAGE#############

import cv2

image = cv2.imread('humans.jpeg', 1)
face_cascade = cv2.CascadeClassifier('faces.xml')

faces = face_cascade.detectMultiScale(image, 1.1, 4)
print(faces)

for (x, y, w, h) in faces:
  cv2.rectangle(image, (x, y), (x+w, y+h), (255, 255, 255), 4)

cv2.imwrite('human_faces.jpeg', image)
