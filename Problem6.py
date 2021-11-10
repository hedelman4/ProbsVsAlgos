def get_min_max(ints):
    min = None
    max = None

    for _ in ints:
        if min == None or _ < min:
            min = _
        if max == None or _ > max:
            max = _

    return min, max

## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

m = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(m)

n = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(n)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
print ("Pass" if ((0, 9) == get_min_max(m)) else "Fail")
print ("Pass" if ((0, 9) == get_min_max(n)) else "Fail")
