#Printing nth largest and nth smallest from list
import heapq
l=[1,2,4,5,10,20,30,11,44]
n = int(input("Enter the nth number which you want largest and smallest number"))
heapq.heapify(l)
nth_maximum = heapq.nlargest(n,l)
nth_minimum = heapq.nsmallest(n,l)
print(nth_maximum,nth_minimum)


def find_nth_largest_smallest(arr, n):
    for i in range(n):  
        smallest = float('inf')  
        for num in arr:
            if num < smallest and (i == 0 or num > prev_smallest):  
                smallest = num
        prev_smallest = smallest

    for i in range(n):  
        largest = float('-inf') 
        for num in arr:
            if num > largest and (i == 0 or num < prev_largest):  
                largest = num
        prev_largest = largest

    return prev_smallest, prev_largest
numbers = [10, 25, 14, 3, 45, 99, 77]
n = 2
smallest, largest = find_nth_largest_smallest(numbers, n)
print(f"{n}th Smallest: {smallest}, {n}th Largest: {largest}")