#Here the list of tuples is sorted based on the last element in the each tuple.

tp_list=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
def last(n):
    return n[-1]
def sort_list(list1):
    return sorted(list1,key=last)
result=sort_list(tp_list)
print(result)
    