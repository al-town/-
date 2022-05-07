import random


def qsort_r(_list, left, right):  # quicksort algorithm
    p = random.choice(_list[left:right + 1])  # the leading element is chosen as random among the subarray
    i, j = left, right
    while i <= j:
        while _list[i] < p:
            i += 1
        while _list[j] > p:
            j -= 1
        if i <= j:
            _list[i], _list[j] = _list[j], _list[i]
            i += 1
            j -= 1

    if j > left:
        qsort_r(_list, left, j)
    if right > i:
        qsort_r(_list, i, right)


# the algorithm has been modified:it looks for the index of the first occurrence of the entered number(:28)
def binary_search(_list, element, left, right):
    if left > right:
        return False
    middle = (right + left) // 2
    if _list[middle] == element and _list[middle-1] != element:
        return middle
    elif element <= _list[middle]:
        return binary_search(_list, element, left, middle - 1)
    else:
        return binary_search(_list, element, middle + 1, right)


# checking the correctness of the entered sequence
def right_input():
    while True:
        _str = input("Enter a sequence of numbers separated by a space: ")
        r_str = False
        for i in _str:
            if not (i.isdigit() or i == " "):
                r_str = True
        if r_str:
            print("Invalid input. Try again")
        else:
            _str = list(map(int, _str.split()))
            break
    return _str


# checking the correctness of the entered number
def right_input_num():
    while True:
        dig = input("Enter any number: ")
        if dig.isdigit():
            dig = int(dig)
            break
        else:
            print("Invalid input. Try again")
    return dig


num_list = right_input()
num = right_input_num()
num_list.append(num)
qsort_r(num_list, 0, len(num_list) - 1)
num_idx = binary_search(num_list, num, 0, len(num_list)-1) - 1
if num_idx < 0:
    print('There is no number less than the entered number in the sequence')
elif num_idx == len(num_list) - 2:
    print('There is no number greater than or equal to the entered number in the sequence')
else:
    print(num_idx)