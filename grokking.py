#%%
def findSmallest(arr):
    smallest = arr[0]
    smallestIndex = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallestIndex = i
    return smallestIndex

def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

arrayTest = [1, 3, 8, 4, 7, 0]
print ("Raw Array \n", arrayTest)

x = findSmallest(arrayTest)
print ('Min Index:', x) 

y = selectionSort(arrayTest)
print ("Sorted Array \n", y)

    