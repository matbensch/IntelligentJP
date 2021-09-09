import tensorflow as tf
from tensorflow.keras import datasets,layers,models
import matplotlib.pyplot as plt
import numpy as np
from tensorflow import keras
from keras import backend as K
from keras.preprocessing.image import ImageDataGenerator
from PIL import Image
import skimage.transform
from skimage import filters
import time
import array_center
import dict_save
import jis_decode

def load_image():
    image = Image.open('test-image.png').convert('L')
    threshold = filters.threshold_otsu(np.array(image))
    binarization_function = lambda x: 255 if x > threshold else 0
    image = image.point(binarization_function, mode='1')
    return image

character_to_label = dict_save.load('character_to_label.txt',str,int)
label_to_character = dict_save.load('label_to_character.txt',int,str)
model = keras.models.load_model('japanese-modelv4.h5')
print(label_to_character)

for entry in character_to_label:
    print(entry)

while 1 == 1:
    test_images = np.zeros((1, 64, 64))
    test_images[0] = load_image()
    test_images[0] = array_center.center(test_images[0])

    if K.image_data_format() == "channels_first":  # reshape the image to be able to go through 2D CNN
        test_images = test_images.reshape(test_images.shape[0], 1, 64, 64)
    else:
        test_images = test_images.reshape(test_images.shape[0], 64, 64, 1)

    pred = model.predict(test_images)[0]

    best_preds = np.argsort(pred)[-4:][::-1]

    for label in best_preds:
        print(label_to_character[label])
        print(pred[label])
    print('\n\n\n')
    time.sleep(5)