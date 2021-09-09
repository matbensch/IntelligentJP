import numpy as np
import tensorflow as tf
from tensorflow import keras
from keras.preprocessing.image import ImageDataGenerator
from keras import backend as K
import dict_save

label_to_character = dict_save.load('label_to_character.txt',int,str)
num_classes = len(label_to_character)
print(num_classes)
print(label_to_character)

print('Loading Images and Labels...')
train_images = np.load('train_images.npz')['arr_0']
train_labels = np.load('train_labels.npz')['arr_0']
test_images = np.load('test_images.npz')['arr_0']
test_labels = np.load('test_labels.npz')['arr_0']
print('Finished Loading')

if K.image_data_format() == "channels_first":
  train_images = train_images.reshape(train_images.shape[0], 1,64,64)
  test_images = test_images.reshape(test_images.shape[0], 1,64,64)
  shape = (1,64,64)
else:
  train_images = train_images.reshape(train_images.shape[0], 64, 64, 1)
  test_images = test_images.reshape(test_images.shape[0], 64, 64, 1)
  shape = (64,64,1)

datagen = ImageDataGenerator(rotation_range=15,zoom_range=0.2)
datagen.fit(train_images)
model = keras.Sequential([
    keras.layers.Conv2D(64, (3,3), activation='tanh', input_shape=shape),
    keras.layers.MaxPooling2D(2,2),
    keras.layers.Conv2D(128, (3,3), activation='tanh'),
    keras.layers.MaxPooling2D(2,2),
    keras.layers.Flatten(),
    keras.layers.Dropout(0.5),
    keras.layers.Dense(7200, activation='tanh'),
    keras.layers.Dense(num_classes, activation="softmax")
])

print('Training Model...')
with tf.device('gpu:0'):
    model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])
    model.fit_generator(datagen.flow(train_images,train_labels,shuffle=True),epochs=30,validation_data=(test_images,test_labels),callbacks = [keras.callbacks.EarlyStopping(patience=8,verbose=1,restore_best_weights=True),keras.callbacks.ReduceLROnPlateau(factor=0.5,patience=3,verbose=1)])
print('Finished Training')

print('Saving Model...')
model.save('japanese-modelv5.h5')
print('Finished Saving')

#v3
# keras.layers.Conv2D(64, (3,3), activation='relu', input_shape=shape),
# keras.layers.MaxPooling2D(2,2),
# keras.layers.Conv2D(64, (3,3), activation='relu'),
# keras.layers.MaxPooling2D(2,2),
# keras.layers.Flatten(),
# keras.layers.Dropout(0.5),
# keras.layers.Dense(2048, activation='relu'),
# keras.layers.Dense(1007, activation="softmax")
# 0.9790

#v4
#     keras.layers.Conv2D(32, (3,3), activation='relu', input_shape=shape),
#     keras.layers.MaxPooling2D(2,2),
#     keras.layers.Conv2D(64, (3,3), activation='relu'),
#     keras.layers.MaxPooling2D(2,2),
#     keras.layers.Conv2D(64, (3, 3), activation='relu'),
#     keras.layers.MaxPooling2D(2, 2),
#     keras.layers.Flatten(),
#     keras.layers.Dropout(0.5),
#     keras.layers.Dense(2048, activation='relu'),
#     keras.layers.Dense(num_classes, activation="softmax")