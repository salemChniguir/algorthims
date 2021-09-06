from random import randint
def smallest_element_index(list):
    if not len(list):
        return None
    index_smallest = 0
    l = len(list)
    for i in range(1,l):
        if list[i] < list[index_smallest]:
            index_smallest = i
    return index_smallest
if __name__ == "__main__": 
    list = [randint(1,10) for i in range(10)]
    print("list before sorting = {}".format(list))
    sorted_list = []
    l = len(list)
    for i in range(l):
        s = smallest_element_index(list)
        if s != None:
            sorted_list.append(list[s])
            list.pop(s)
    print("list after sorting = {}".format(sorted_list))