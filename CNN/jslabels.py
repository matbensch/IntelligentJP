

fin = open('label_to_character.txt','r',encoding='utf8')

n = int(fin.readline())

for i in range(n):
    label,char = fin.readline().split()
    label = int(label)
    print('label_to_character['+str(label)+'] = \"'+char+'\";')