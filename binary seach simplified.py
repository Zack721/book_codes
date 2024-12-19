List = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]  # Sorted list
target = 71  # Target value to search for

left, right = 0, len(List) - 1  # Set initial boundaries

while left <= right:  # Continue while there are elements to search
    mid = (left + right) // 2  # Find the middle index

    if List[mid] == target:  # If the middle element is the target
        print(f"Target found at index {mid + 1}")
        break
    elif List[mid] < target:  # If the target is larger, ignore the left half
        left = mid + 1
    else:  # If the target is smaller, ignore the right half
        right = mid - 1
else:
    print("Target not found")