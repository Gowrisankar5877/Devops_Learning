fruits=['Mango','Apple','Banana','Custard']
print(sorted(fruits))
print(fruits)
fruits.sort()
print(fruits)
fruits.sort(reverse=True)
print(fruits)
l=[1,10,80,1000,90,300,0]
print(max(l))
print(min(l))

#Printing nth largest and nth smallest from list
import heapq
n = int(input("Enter the nth number which you want largest and smallest number"))
heapq.heapify(l)
nth_maximum = heapq.nlargest(n,l)
nth_minimum = heapq.nsmallest(n,l)
print(nth_maximum,nth_minimum)


def find_nth_largest_smallest(arr, n):
    if n > len(arr) or n < 1:
        return "N is out of range"

    # Find the Nth smallest
    for i in range(n):  
        smallest = float('inf')  # Initialize smallest to infinity
        for num in arr:
            if num < smallest and (i == 0 or num > prev_smallest):  
                smallest = num
        prev_smallest = smallest

    # Find the Nth largest
    for i in range(n):  
        largest = float('-inf')  # Initialize largest to negative infinity
        for num in arr:
            if num > largest and (i == 0 or num < prev_largest):  
                largest = num
        prev_largest = largest

    return prev_smallest, prev_largest

# Example usage
numbers = [10, 25, 14, 3, 45, 99, 77]
n = 2
smallest, largest = find_nth_largest_smallest(numbers, n)
print(f"{n}th Smallest: {smallest}, {n}th Largest: {largest}")

