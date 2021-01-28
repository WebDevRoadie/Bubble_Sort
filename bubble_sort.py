arr = [1,5,3,4,2,0,8,6,7]

def bubbleSort(arr):
    for j in range(len(arr)-1):
        print("\n\n", "-"*50, "Iteration", j)
        for i in range(len(arr)-1-j):
            print("\n","*"*80, "\nComparing", arr[i], arr[i+1])
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] =arr[i+1], arr[i]
                print("Swapped", arr[i], arr[i+1])
                print("Array is now", arr)
            else:
                print("No need to swap", arr[i], arr[i+1])

bubbleSort(arr)