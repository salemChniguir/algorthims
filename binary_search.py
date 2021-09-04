from random import randint

def binary_search (element, list):
    # if list is empty return None
    print("List = {}, element = {}".format(list,element))
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
    l = [randint(1,100) for i in range(100)]
    print(binary_search(randint(1,100),sorted(l)))