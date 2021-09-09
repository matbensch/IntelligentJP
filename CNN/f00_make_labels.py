import numpy as np

image_labels = np.zeros(225875)

katakana_samples = [1411]*51
katakana_samples[20] = 1410
katakana_samples[41] = 1410

current_katakana_image = 0
for i in range(51):
    for j in range(katakana_samples[i]):
        image_labels[current_katakana_image] = i
        current_katakana_image+=1

for i in range(161):
    for j in range(956):
        image_labels[71959+i*956+j] = 51+j

np.savez_compressed('image_labels.npz',image_labels)