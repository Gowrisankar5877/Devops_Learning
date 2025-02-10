def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:  
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def sort_dict_keys_and_values(d):
    keys = list(d.keys())
    keys = bubble_sort(keys)
    sorted_dict = {}
    for key in keys:
        sorted_dict[key] = bubble_sort(d[key])  
    return sorted_dict

data = {
    "banana": [5, 3, 8, 1, 2],
    "apple": [90, 85, 92, 88, 76],
    "cherry": ["z", "m", "a", "k", "b"]
}
sorted_data = sort_dict_keys_and_values(data)
print(sorted_data)