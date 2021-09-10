def bubbleSort(arr):
    n = len(arr)

    # Number of step
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n-i-1):

            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

                
def bubbleSort_opt(arr):
    n = len(arr)

    # Number of step
    for i in range(n):
        swapped = False

        # Last i elements are already in place
        for j in range(0, n-i-1):

            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True

            if swapped == False:
                break

if __name__ == '__main__':
    arr = [2, 34, 56, 3, 1, 2, 45]
    print('arr : {}'.format(arr))

    bubbleSort(arr)
    # bubbleSort_opt(arr)
    print(f'Bubble Sorted Array is: {arr}')

## OUTPUT
# arr : [2, 34, 56, 3, 1, 2, 45]
# Bubble Sorted Array is: [1, 2, 2, 3, 34, 45, 56]
