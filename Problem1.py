def sqrt(number):

    sqrtArray = [0 for i in range(number)]
    for _ in range(0,number):
        sqrtArray[_] = _ + 1

    start_index = 0
    end_index = len(sqrtArray) - 1

    if number < 0:
        return None

    elif number == 0 or number == 1:
        return number

    else:
        while start_index <= end_index:
            mid_index = (start_index + end_index)//2

            if sqrtArray[mid_index - 1] * sqrtArray[mid_index - 1] < number and sqrtArray[mid_index + 1] * sqrtArray[mid_index + 1] > number:
                return sqrtArray[mid_index]

            elif sqrtArray[mid_index] * sqrtArray[mid_index] > number:
                end_index = mid_index - 1

            else:
                start_index = mid_index + 1

print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")
