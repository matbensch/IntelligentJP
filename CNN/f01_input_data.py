import numpy as np
import array_center
import etl_read
import dict_save

number_of_examples = 71959 + 153916 + 607200

all_images = np.zeros((number_of_examples, 64, 64))
all_labels = np.zeros(number_of_examples)
label_to_character = {}
character_to_label = {}

def read_files_ETL1(starting_index):
    number_of_files = 13
    images_per_file = [11288] * number_of_files
    images_per_file[0] = 11560
    images_per_file[1] = 11560
    images_per_file[2] = 11560
    images_per_file[3] = 11560
    images_per_file[4] = 11560
    images_per_file[5] = 11560
    images_per_file[8] = 11287
    images_per_file[11] = 11287
    images_per_file[12] = 4233

    current_index = 0
    for file_number in range(7,number_of_files+1):
        file_url = "C:/Users/matth/Desktop/ETL/ETL1/ETL1/ETL1C_{:02d}".format(file_number)
        file = open(file_url,'rb')
        for image_number in range(images_per_file[file_number-1]):
            record = etl_read.read_record_ETL1(file, image_number * 2052)
            if record[0] not in character_to_label:
                character_to_label[record[0]] = len(character_to_label)
                label_to_character[character_to_label[record[0]]] = record[0]
            all_labels[starting_index + current_index] = character_to_label[record[0]]
            all_images[starting_index + current_index] = record[1]
            current_index += 1

def read_files_ETL8(starting_index):
    number_of_files = 33
    images_per_file = [4780] * number_of_files
    images_per_file[32] = 956

    current_index = 0
    for file_number in range(1,number_of_files+1):
        file_url = "C:/Users/matth/Desktop/ETL/ETL8G/ETL8G/ETL8G_{:02d}".format(file_number)
        file = open(file_url,'rb')
        for image_number in range(images_per_file[file_number-1]):
            record = etl_read.read_record_ETL8(file, image_number * 8199)
            if record[0] not in character_to_label:
                character_to_label[record[0]] = len(character_to_label)
                label_to_character[character_to_label[record[0]]] = record[0]
            all_labels[starting_index + current_index] = character_to_label[record[0]]
            all_images[starting_index + current_index] = record[1]
            current_index += 1

def read_files_ETL9(starting_index):
    number_of_files = 50
    images_per_file = [12144] * number_of_files

    current_index = 0
    for file_number in range(1, number_of_files + 1):
        file_url = "C:/Users/matth/Desktop/ETL/ETL9G/ETL9G/ETL9G_{:02d}".format(file_number)
        file = open(file_url, 'rb')
        for image_number in range(images_per_file[file_number - 1]):
            record = etl_read.read_record_ETL9(file, image_number * 8199)
            if record[0] not in character_to_label:
                character_to_label[record[0]] = len(character_to_label)
                label_to_character[character_to_label[record[0]]] = record[0]
            all_labels[starting_index + current_index] = character_to_label[record[0]]
            all_images[starting_index + current_index] = record[1]
            current_index += 1

print('Reading ETL1...')
read_files_ETL1(0)
print('Finished ETL1')

print('Reading ETL8...')
read_files_ETL8(71959)
print('Finished ETL8')

print('Reading ETL9...')
read_files_ETL9(71959 + 153916)
print('Finished ETL9')

print('Saving Dictionaries...')
dict_save.save('label_to_character.txt',label_to_character)
dict_save.save('character_to_label.txt',character_to_label)
print('Finished Dictionaries')

print('Centering Images...')
for i in range(len(all_images)):
    all_images[i] = array_center.center(all_images[i])
print('Finished Centering')

print('Saving Labels and Images...')
np.savez_compressed('all_labels.npz', all_labels)
np.savez_compressed('all_images.npz', all_images)
print('Finished Saving')
