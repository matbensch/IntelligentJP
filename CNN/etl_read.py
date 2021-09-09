import struct
from PIL import Image
import numpy as np
from skimage import filters
import jis_decode

def read_record_ETL1(file,offset):
    file.seek(offset)
    raw_data = struct.unpack('>H2sH6BI4H4B4x2016s4x',file.read(2052))
    character_code = raw_data[3]
    character = jis_decode.decode_jisx0201(character_code)
    raw_image_data = raw_data[18]
    image = Image.frombytes('F',(64,63),raw_image_data,'bit',4).convert('L')
    image = image.resize((64,64))
    threshold = filters.threshold_otsu(np.array(image))
    binarization_function = lambda x: 255 if x > threshold else 0
    image = image.point(binarization_function,mode='1')
    return (character,image)

def read_record_ETL8(file,offset):
    file.seek(offset)
    raw_data = struct.unpack('>2H8sI4B4H2B30x8128s11x',file.read(8199))
    character_code = raw_data[1]
    character = jis_decode.decode_jisx0208(character_code)
    raw_image_data = raw_data[14]
    image = Image.frombytes('F',(128,127),raw_image_data,'bit',4).convert('L')
    image = image.resize((64,64))
    threshold = filters.threshold_otsu(np.array(image))
    binarization_function = lambda x: 255 if x > threshold else 0
    image = image.point(binarization_function, mode='1')
    return (character,image)

def read_record_ETL9(file,offset):
    file.seek(offset)
    raw_data = struct.unpack('>2H8sI4B4H2B34x8128s7x', file.read(8199))
    character_code = raw_data[1]
    character = jis_decode.decode_jisx0208(character_code)
    raw_image_data = raw_data[14]
    image = Image.frombytes('F', (128, 127), raw_image_data, 'bit', 4).convert('L')
    image = image.resize((64, 64))
    threshold = filters.threshold_otsu(np.array(image))
    binarization_function = lambda x: 255 if x > threshold else 0
    image = image.point(binarization_function, mode='1')
    return (character, image)
