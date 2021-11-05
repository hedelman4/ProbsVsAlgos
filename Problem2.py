def rotated_array_search(input_list, number):
    start_index = 0
    end_index = len(input_list) - 1
    mid_index = (start_index + end_index)//2

    if number < min(input_list) or number > max(input_list):
        return -1

    else:
        return recursive_array_search(input_list, number, start_index, end_index, mid_index)

def recursive_array_search(input_list, number, start_index, end_index, mid_index):
    if input_list[start_index] == number:
        return start_index

    elif input_list[end_index] == number:
        return end_index

    elif input_list[mid_index] == number:
        return mid_index

    else:
        if  input_list[start_index] < input_list[mid_index]:
            if number > input_list[start_index] and number < input_list[mid_index]:
                return binary_search(input_list[:mid_index], number)
            else:
                return recursive_array_search(input_list, number, mid_index + 1, end_index, (mid_index + end_index)//2)
        elif input_list[mid_index] < input_list[end_index]:
            if number > input_list[mid_index] and number < input_list[end_index]:
                return binary_search(input_list[mid_index:], number)
            else:
                return recursive_array_search(input_list, number, start_index, mid_index, (start_index + mid_index)//2)

def binary_search(array, target):
    start_index = 0
    end_index = len(array) - 1

    while start_index <= end_index:
        mid_index = (start_index + end_index)//2

        mid_element = array[mid_index]

        if target == mid_element:
            return mid_index

        elif target < mid_element:
            end_index = mid_index - 1

        else:
            start_index = mid_element + 1

    return -1

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
