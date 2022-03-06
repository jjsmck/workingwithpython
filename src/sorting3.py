import random



l = [random.randint(0,100) for i in range(5)]
def sortSmallToHigh(listNumbers):
    listNumbers.sort()
    
    return listNumbers

print(sortSmallToHigh(l))
