
def save(path,my_dict):
    file = open(path,'w',encoding='utf8')
    file.write(str(len(my_dict)))
    file.write('\n')
    for key in my_dict:
        file.write(str(key))
        file.write('\t')
        file.write(str(my_dict[key]))
        file.write('\n')

def load(path,key_type,value_type):
    file = open(path,'r',encoding='utf8')
    num_entries = int(file.readline())
    my_dict = {}
    for i in range(num_entries):
        line = file.readline()[:-1].split('\t')
        key = key_type(line[0])
        value = value_type(line[1])
        my_dict[key] = value
    return my_dict