def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2

        L = arr[:mid]
        R = arr[mid:]

        mergeSort(L)
        mergeSort(R)

        i = j = k = 0
    
        # compare left Half and right Half, then sort!
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        
        # handling remain elements
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


if __name__ == '__main__':
    arr = [38, 27, 43, 3, 9, 82, 10]
    print('arr : {}'.format(arr))

    mergeSort(arr)
    print(f'Merge Sorted Array is: {arr}')

## OUTPUT
# arr : [38, 27, 43, 3, 9, 82, 10]
# Merge Sorted Array is: [3, 9, 10, 27, 38, 43, 82]