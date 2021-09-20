def selectionSort(arr):
    for i in range(len(arr)):
        
        min_idx = i
        # find the minimum element idx
        # in remaining unsorted array
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        
        # Swap
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def stableSelectionSort(arr):
    for i in range(len(arr)):
        
        min_idx = i
        # find the minimum element idx
        # in remaining unsorted array
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        
        # instead Swapping, insert min to right place
        key = arr[min_idx]
        while min_idx > i:
            arr[min_idx] = arr[min_idx - 1]
            min_idx -= 1
        arr[i] = key


if __name__ == '__main__':
    arr = [2, 34, 56, 3, 1, 2, 45]
    print('arr : {}'.format(arr))

    selectionSort(arr)
    print(f'Slection Sorted Array is: {arr}')

    arr2 = [2, 34, 56, 3, 1, 2, 45]
    print('arr2 : {}'.format(arr2))

    stableSelectionSort(arr2)
    print(f'Stable Slection Sorted Array is: {arr2}')

## OUTPUT
# arr : [2, 34, 56, 3, 1, 2, 45]
# Selection Sorted Array is: [1, 2, 2, 3, 34, 45, 56]
# arr2 : [2, 34, 56, 3, 1, 2, 45]
# Stable Selection Sorted Array is: [1, 2, 2, 3, 34, 45, 56]
