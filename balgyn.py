def find_max_negative(arr):
    negative_elements = [x for x in arr if x < 0]
    if negative_elements:
        return max(negative_elements)
    else:
        return None
arr = [5, -3, 2, -7, -1, 4, 9]
result = find_max_negative(arr)
print(f"Максимум среди отрицательных чисел: {result}")
