def selection_sort(arr):
    # this function finds the index of the smallest element in a given range
    
    def find_smallest_index(a, b):
        min_value = arr[a]
        for i in range(a, b):
            if arr[i] < min_value:
                min_value = arr[i]
        return arr.index(min_value)
    
    #this function swaps the values stored in two indices 
    def swap(a, b):
        temp = arr[a]
        arr[a] = arr[b]
        arr[b] = temp

    if arr is []:
      return arr
    for i in range(0, len(arr) ):
        smallest_index = find_smallest_index(i, len(arr))
        swap(i, smallest_index)       
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    def is_sorted(arr):
        for i in range(0, len(arr)-1):
            if arr[i] > arr[i+1]:
                return False
        return True

    def swap(a, b):
      temp = arr[a]
      arr[a] = arr[b]
      arr[b] = temp

    while True:
        for i in range(0, len(arr)-1):
            if arr[i] > arr[i+1]:
                swap(i, i+1)
        if is_sorted(arr):
          break
    return arr

  
    

'''
STRETCH: implement the Count Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here


    return arr
