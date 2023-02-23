from pprint import pprint

def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k

with open('4.txt', 'w', encoding='utf-8') as file:
    lenghts = []
    names = []
    lenght_sorted = []
    dic = {}

    with open('1.txt', 'rt', encoding='utf-8') as file_1:
        lenghts.append(len(file_1.readlines()))
        names.append(file_1.name)

    with open('2.txt', 'r', encoding='utf-8') as file_2:
        lenghts.append(len(file_2.readlines()))
        names.append(file_2.name)

    with open('3.txt', 'r', encoding='utf-8') as file_3:
        lenghts.append(len(file_3.readlines()))
        names.append(file_3.name)

    for item in range(len(lenghts)):
        dic[names[item]] = lenghts[item]

    dic_sorted = {}
    dic_sorted = sorted(dic.values())

    for num in dic_sorted:
        if num in dic.values():
            file.write(get_key(dic, num))
            file.write('\n')
            file.write(str(num))
            file.write('\n')
            with open(str(get_key(dic, num)), 'rt', encoding='utf-8') as file_buffer:
                for line in file_buffer:
                    file.write(line)
                file.write('\n')
