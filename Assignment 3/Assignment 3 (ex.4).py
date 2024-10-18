def new_sorted_list(sorted_list, value):

    index = 0
    while index < len(sorted_list) and sorted_list[index] < value:
        index += 1
    

    sorted_list.insert(index, value)
    return sorted_list

# example:
list1 = [1, 34, 56, 78, 89]
val = 77
print(new_sorted_list(list1, val)) 

list1 = [1, 3, 56, 234, 789]
val = -99
print(new_sorted_list(list1, val)) 

list1 = [1, 3, 56, 234, 789]
val = 789
print(new_sorted_list(list1, val)) 
