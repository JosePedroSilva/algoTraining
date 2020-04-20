list_1 = [4, 5, 2, 5 ,1 ,6 ,2 ,9, 9, 3, 7]
list_2 = [787, 677, 391, 318, 543, 717, 180, 113, 795, 19, 202, 534, 201, 370, 276, 975, 403, 624, 770, 595, 571, 268, 373]
list_3 = [860, 380, 151, 585, 743, 542, 147, 820, 439, 865, 924, 387]

def merge_sort(items):
    if len(items) <= 1:
        return items

    middle_index = len(items) // 2
    left_split = items[:middle_index]
    right_split = items[middle_index:]

    left_sorted = merge_sort(left_split)
    right_sorted = merge_sort(right_split)

    return merge(left_sorted, right_sorted)

def merge(left, right):
    result = []

    while (left and right):
        if left[0] < right[0]:
            result.append(left[0])
            left.pop(0)
        else:
            result.append(right[0])
            right.pop(0)

    if left:
        result += left
    if right:
        result += right

    return result
    
order1 = merge_sort(list_1)
order2 = merge_sort(list_2)
order3 = merge_sort(list_3)

print(order1)
print(order2)
print(order3)