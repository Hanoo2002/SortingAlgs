import random


# ======================== QUICK SORT ===================================


def choose_pivot(first, last):
    """
    Chooses a random index as a pivot
    :param last:
    :param first:
    :return:
    """
    random_pivot_index = random.randrange(first, last)
    return random_pivot_index


def partitioning(arr, first, last):
    """
    Partitions the array into 2 partitions 1 larger and other smaller than the pivot
    :param arr:
    :param first:
    :param last:
    :return:
    """
    pivot_index = choose_pivot(first, last)
    pivot_value = arr[pivot_index]
    arr[first], arr[pivot_index] = arr[pivot_index], arr[first]
    last_s1 = first
    first_unknown = first + 1
    while first_unknown <= last:
        if arr[first_unknown] < pivot_value:
            last_s1 += 1
            (arr[first_unknown], arr[last_s1]) = (arr[last_s1], arr[first_unknown])
        first_unknown += 1

    (arr[first], arr[last_s1]) = (arr[last_s1], arr[first])
    pivot_index = last_s1
    return pivot_index


def quick_sort_implementation(arr, first, last):
    """
    Implementation of Quick sort
    :param arr:
    :param first:
    :param last:
    :return:
    """
    if first < last:
        pivot_index = partitioning(arr, first, last)
        quick_sort_implementation(arr, first, pivot_index - 1)
        quick_sort_implementation(arr, pivot_index + 1, last)


def quick_sort(arr):
    """
    Interface with quick_sort_implementation function
    :param arr:
    :return:
    """
    quick_sort_implementation(arr, 0, len(arr) - 1)


ls = [12, 34, 5, 1, 62, 23, 56, 45, 356, 82, 7623]
quick_sort(ls)
print(ls)

