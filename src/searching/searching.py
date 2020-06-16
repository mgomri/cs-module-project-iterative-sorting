import math
# linear search

def linear_search(arr, target):
    for el in arr:
        if el is target:
            return arr.index(el)
    return -1   # not found


# Write an iterative implementation of Binary Search

def binary_search(arr, target):    
    low = 0
    high = len(arr)-1
    mid = math.floor((high - low)/2) + low 
    while low < high:
        if target < arr[mid]:
            low = low
            high = mid
            mid = math.floor((high - low)/2) + low  
        elif target > arr[mid]:
            low = mid
            high = high
            mid = math.ceil((high - low)/2) + low
        else:
            return mid
    return -1 

