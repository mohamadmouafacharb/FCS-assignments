def recursive_binary_search(sorted_list, target, start, end):
    if start > end:
        return -1

    mid = (start + end) // 2

    if sorted_list[mid] == target:
        return mid

    elif sorted_list[mid] > target:
        return recursive_binary_search(sorted_list, target, start, mid - 1)

    else:
        return recursive_binary_search(sorted_list, target, mid + 1, end)
    

# example:
sorted_list = [1, 3, 5, 7, 9, 11, 13, 15]
target = 3

index = recursive_binary_search(sorted_list, target, 0, len(sorted_list) - 1)

if index != -1:
    print(f"Target value {target} found at index {index}.")
else:
    print(f"Target value {target} not found in the list.")