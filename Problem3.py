def rearrange_digits(input_list):
    sortedList = mergesort(input_list)
    sum1String = ''
    sum2String = ''
    output_list = [0,0]
    if len(sortedList) % 2 == 0:
        while sortedList:
            sum1String = str(sortedList.pop(0)) + sum1String
            sum2String = str(sortedList.pop(0)) + sum2String
        output_list[0] = int(sum1String)
        output_list[1] = int(sum2String)
    else:
        large_digit = sortedList.pop(len(sortedList)-1)
        while sortedList:
            sum1String = str(sortedList.pop(0)) + sum1String
            sum2String = str(sortedList.pop(0)) + sum2String
        sum1String = str(large_digit) + sum1String
        output_list[0] = int(sum1String)
        output_list[1] = int(sum2String)
    return  output_list

def mergesort(items):

    if len(items) <= 1:
        return items

    mid = len(items) // 2
    left = items[:mid]
    right = items[mid:]

    left = mergesort(left)
    right = mergesort(right)

    return merge(left, right)

def merge(left, right):

    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] > right[right_index]:
            merged.append(right[right_index])
            right_index += 1
        else:
            merged.append(left[left_index])
            left_index += 1

    merged += left[left_index:]
    merged += right[right_index:]

    return merged

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_case1 = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_case2 = [[1, 2, 3], [32, 1]]
test_function(test_case1)
test_function(test_case2)
#Edge cases
test_case3 = [[0,0], [0, 0]]
test_case4 = [[1, 1, 1, 1, 1, 1, 1], [1111, 111]]
test_function(test_case3)
test_function(test_case4)
