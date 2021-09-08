def binarySearch_recur(arr, start, end, x):
    if start <= end:
        mid = start + (end - start) // 2

        if arr[mid] == x:
            return mid
        
        elif arr[mid] > x:
            return binarySearch_recur(arr, start, mid-1, x)

        else:
            return binarySearch_recur(arr, mid + 1 , end, x)

    else:
        return -1

def binarySearch_iter(arr, start, end, x):
    while (start <= end):
        mid = start + (end - start) // 2

        if arr[mid] == x:
            return mid
        
        elif arr[mid] < x:
            start = mid + 1

        else:
            end = mid -1

    return -1


if __name__ == '__main__':
    arr = [1, 3, 5, 10, 30, 60, 75]
    x = 60

    # result = binarySearch_recur(arr, 0, len(arr)-1, x)
    result = binarySearch_iter(arr, 0, len(arr)-1, x)

    print('arr : {}'.format(arr))
    print('x : {}'.format(x))

    if result != -1:
        print('Element is present at index {}'.format(result))
    else:
        print('Element is not present in array')