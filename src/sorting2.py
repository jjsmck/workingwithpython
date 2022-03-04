import random


def sortData(data_list):
    new_list = []

    while data_list:
        minimum = data_list[0]
        for x in data_list:
            if x < minimum:
                minimum = x
        new_list.append(minimum)
        data_list.remove(minimum)

    return new_list

list = [random.randint(0,100) for i in range(5)]
print (sortData(list))