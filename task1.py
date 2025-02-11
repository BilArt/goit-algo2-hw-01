def find_min_max(arr):
    if len(arr) == 1:
        return arr[0], arr[0]  # На випадок, якщо мінімум і максимум однакові

    if len(arr) == 2:
        return (arr[0], arr[1]) if arr[0] < arr[1] else (arr[1], arr[0])

    mid = len(arr) // 2
    left_min, left_max = find_min_max(arr[:mid])
    right_min, right_max = find_min_max(arr[mid:])

    return min(left_min, right_min), max(left_max, right_max)
