import random


def print_lines(number):
    line = 1
    while line <= number:
        print("*" * line)
        line += 1
    print()


def factorize_number(x):
    divisor = 2
    while x > 1:
        if x % divisor == 0:
            print(divisor)
            x //= divisor
        else:
            divisor += 1


def array_search(A: int, N: int, x: int):
    """
    Search number x in array A
    if in array have a same numbers - return first element in array
    :param A: numbers array
    :param N:
    :param x:
    :return: index element x in array A, or -1 if not found
    """
    for index in range(N):
        if A[index] == x:
            return index
    return -1


def invert_array(A, N):
    """
    ivert array(back - to - first element)
    :param A:
    :return:
    """
    # B = [0] * N
    # for i in range(N):
    #     B[N - 1 - i] = A[i]
    # return B
    for k in range(N // 2):
        A[k], A[N - 1 - k] = A[N - 1 - k], A[k]
    return A


def test_invert_array():
    A1 = [1, 2, 3, 4, 5]

    invert_array(A1, 5)

    if A1 == [5, 4, 3, 2, 1]:
        print("test - ok")
    else:
        print("test - fail")


def test_array_search():
    A1 = [1, 2, 3, 4, 5]
    m = array_search(A1, 5, 8)
    if m == -1:
        print("test - ok")
    else:
        print("test - fail")

    A2 = [-1, -2, -3, -4, -5]
    m = array_search(A2, 5, 8)
    if m == -1:
        print("test - ok")
    else:
        print("test - fail")

    A3 = [10, 20, 30, 40, 50]
    m = array_search(A3, 5, 8)
    if m == -1:
        print("test - ok")
    else:
        print("test - fail")


def cicle_move(A):
    """
    move first to last and move elements between first and last 1 element back
    :param A: list to execute cicle move
    :return:
    """
    tmp = A[0]
    for i in range(len(A) - 1):
        A[i] = A[i + 1]
    A[len(A) - 1] = tmp
    return A


def insert_sort(arr):
    """
    sort list arr by insert sort
    :param arr:
    :return:
    """
    array_length = len(arr)
    for top in range(1, array_length):
        k = top
        while k > 0 and arr[k - 1] > arr[k]:
            arr[k], arr[k - 1] = arr[k - 1], arr[k]
            k -= 1
    return arr


def selection_sort(arr):
    """
    sort list arr by selection sort
    :param arr: unsorted list
    :return: sorted list arr
    """
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


def bubble_sort(arr: list):
    """
    bubble sort
    :param arr: unsorted list
    :return: sorted list
    """
    for i in range(len(arr) - 1, -1, -1):
        flag_sorted = True
        for k in range(i):
            if arr[k] > arr[k + 1]:
                flag_sorted = False
                arr[k], arr[k + 1] = arr[k + 1], arr[k]
        if flag_sorted:
            return arr
    return arr


def count_sort(arr: list):
    pass


def test_sort(sort_algorithm):
    print("Testing: ", sort_algorithm.__doc__)
    print("test case #1: ", end="")
    arr = [3, 5, 6, 3, 1]
    arr_sorted = [1, 3, 3, 5, 6]
    sort_algorithm(arr)
    print("ok" if arr == arr_sorted else "Fail")

    print("test case #2: ", end="")
    arr = list(range(10, 20)) + list(range(0, 10))
    arr_sorted = list(range(0, 20))
    sort_algorithm(arr)
    print("ok" if arr == arr_sorted else "Fail")

    print("test case #3: ", end="")
    arr = [3, 5, 6, 10, 1]
    arr_sorted = [1, 3, 5, 6, 10]
    sort_algorithm(arr)
    print("ok" if arr == arr_sorted else "Fail")


# recursion functions



length_array = int(input("Enter number of array"))
A, B = [0] * length_array, [0] * length_array

A1 = [True] * length_array
for n in range(length_array):
    A[n] = random.randint(1, 50)
    B[n] = random.randint(1, 50)

print(A)
# print(cicle_move(A))
# test_array_search()
# test_invert_array()

# A2 = []
# for k in range(10):
#     A2.append(random.randint(1, 100))
# print(A2)
# A3 = [x ** 2 for x in range(10)]
# print(A3)
# B = [x ** 2 if x % 2 == 0 else 0 for x in A3]
print(B)
print(selection_sort(A))
print(bubble_sort(B))

test_sort(insert_sort)
test_sort(bubble_sort)
test_sort(selection_sort)
