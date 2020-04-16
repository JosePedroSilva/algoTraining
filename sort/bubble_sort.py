nums = [4, 5, 2, 5 ,1 ,6 ,2 ,9, 9, 3, 7]
print(f'Unordered list {nums}')

def bubble_sort(arr):
    for i in range(len(arr)):
        for idx in range(len(arr)-i-1):
            if arr[idx] > arr[idx + 1]:
                arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]
                print(f"Swapped {arr[idx]} for {arr[idx + 1]}")

bubble_sort(nums)
print (f'Ordered list {nums}')