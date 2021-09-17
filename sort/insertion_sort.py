def insertionSort(arr):
    for i in range(1, len(arr)):
        j = i - 1
        key = arr[i]

        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = key

def binaryInsertionSort(arr):
    for i in range(1, len(arr)):
        j = i - 1
        key = arr[i]

        loc = 0
        end = j
        
        # use Binary Search to find where arr[i]'s place
        while loc <= end:
            mid = loc + (end - loc) // 2
            if key == arr[mid]:
                loc = mid + 1
                break
            elif key > arr[mid]:
                loc = mid + 1
            else:
                end = mid - 1

        while j >= loc:
            arr[j+1] = arr[j]
            j -= 1
        arr[j + 1] = key


if __name__ == '__main__':
    arr = [2, 34, 56, 3, 1, 2, 45]
    print('arr : {}'.format(arr))

    insertionSort(arr)
    print(f'Insertion Sorted Array is: {arr}')

    arr = [2, 34, 56, 3, 1, 2, 45]
    print('arr : {}'.format(arr))

    binaryInsertionSort(arr)
    print(f'Binary Insertion Sorted Array is: {arr}')


## OUTPUT
# arr : [2, 34, 56, 3, 1, 2, 45]
# Insertion Sorted Array is: [1, 2, 2, 3, 34, 45, 56]
# arr : [2, 34, 56, 3, 1, 2, 45]
# Binary Insertion Sorted Array is: [1, 2, 2, 3, 34, 45, 56]
