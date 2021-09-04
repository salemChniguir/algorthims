from random import randint
from math import log2

def binary_search (element, list):
    # if list is empty return None
    print("element to search = {}".format(element))
    if not len(list):
        return None
    low = 0
    high = len(list)-1
    while(low<=high):
        
        mid = (low + high) // 2
        print( "search in list[{},{}] , mid = {}".format(low,high,mid))
        if (element == list[mid]):
            return mid
        elif( element < list[mid]):
            high = mid - 1
        else:
            low  = mid + 1
    # if element not found return None
    return None

if __name__ == "__main__":
    random_size = randint(1,1000000)
    print("Max number of steps = {}".format(log2(random_size)))
    l = [randint(1,random_size) for i in range(random_size)]
    print(binary_search(randint(1,random_size),sorted(l)))