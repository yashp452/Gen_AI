def find_largest_number(array):
    if not array:
        return None
    largest = array[0]
    for num in array:
        if num > largest:
            largest = num
    return largest

# Example usage:
print(find_largest_number([3, 1, 4, 1, 5, 9]))