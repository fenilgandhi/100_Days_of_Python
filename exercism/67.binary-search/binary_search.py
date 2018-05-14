def binary_search(list_of_numbers, number):
    if not list_of_numbers:
        raise ValueError("Empty list")
    # 2 end of the search list
    left, right = 0, len(list_of_numbers) - 1
    while (right - left) > 1:
        # Find mid of two ends and check number exists
        # in which sub-list and discard the remaining sublist
        mid = (left + right) // 2
        if list_of_numbers[mid] == number:
            return mid
        elif list_of_numbers[mid] < number:
            left = mid
        else:
            right = mid
    if list_of_numbers[right] == number:
        return right
    elif list_of_numbers[left] == number:
        return left
    raise ValueError("Value not found")
