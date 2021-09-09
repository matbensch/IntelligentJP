import numpy as np
from sklearn.model_selection import train_test_split

print('Loading Labels and Images...')
labels = np.load('all_labels.npz')['arr_0'].astype(int)
images = np.load('all_images.npz')['arr_0'].astype(int)
print('Finished Loading')

print('Train/Test Splitting...')
train_images,test_images,train_labels,test_labels = train_test_split(images,labels,test_size=0.2)
print('Finished Splitting')

print('Saving Train/Test Images and Labels...')
np.savez_compressed('train_images.npz',train_images)
np.savez_compressed('train_labels.npz',train_labels)
np.savez_compressed('test_images.npz',test_images)
np.savez_compressed('test_labels.npz',test_labels)
print('Finished Saving')