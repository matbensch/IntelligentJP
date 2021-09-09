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

def load_image(index):
    file_url = "my_test_images/test-image{:02d}.png".format(index)
    image = Image.open(file_url).convert('L')
    threshold = filters.threshold_otsu(np.array(image))
    binarization_function = lambda x: 255 if x > threshold else 0
    image = image.point(binarization_function, mode='1')
    return image

character_to_label = dict_save.load('character_to_label.txt',str,int)
label_to_character = dict_save.load('label_to_character.txt',int,str)
model = keras.models.load_model('japanese-modelv4.h5')
print(label_to_character)

test_label_file = open('my_test_images/my-test-characters.txt','r',encoding='utf8')
num_tests_s = test_label_file.readline()
print(num_tests_s)
num_tests = int(num_tests_s)
test_images = np.zeros((num_tests,64,64))
test_labels = np.zeros((num_tests))

for i in range(num_tests):
    test_images[i] = load_image(i)
    test_images[i] = array_center.center(test_images[i])
    test_labels[i] = character_to_label[test_label_file.readline()[:-1]]

if K.image_data_format() == "channels_first":
  test_images = test_images.reshape(test_images.shape[0], 1,64,64)
else:
  test_images = test_images.reshape(test_images.shape[0], 64, 64, 1)

print(model.evaluate(test_images,test_labels))