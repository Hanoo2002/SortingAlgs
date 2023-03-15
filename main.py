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


# ===========================MERGE SORT ================================


def merge(arr, left, mid, right):
    """
    merges 2 sorted arrays together
    :param arr:
    :param left:
    :param mid:
    :param right:
    :return:
    """
    left_arr = arr[left:mid+1]
    right_arr = arr[mid+1:right+1]
    len_right = len(right_arr)
    len_left = len(left_arr)
    i = 0
    j = 0
    k = left
    while i < len_left and j < len_right:
        if left_arr[i] < right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
            k += 1
        else:
            arr[k] = right_arr[j]
            j += 1
            k += 1

    while i < len_left:
        arr[k] = left_arr[i]
        i += 1
        k += 1
    while j < len_right:
        arr[k] = right_arr[j]
        j += 1
        k += 1


def merge_sort_implementation(arr, first, last):
    """
    Implements merge sort algorithm
    :param arr:
    :param first:
    :param last:
    :return:
    """
    if first < last:
        mid = (first + last) // 2
        merge_sort_implementation(arr, first, mid)
        merge_sort_implementation(arr, mid + 1, last)
        merge(arr, first, mid, last)


def merge_sort(arr):
    """
    interface with merge_sort_implementation
    :param arr:
    :return:
    """
    merge_sort_implementation(arr, 0, len(arr) - 1)

# ==========================Selection SORT ===================================


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]



ls = [12, 34, 5, 1, 62, 23]
# heap_sort(ls)
selection_sort(ls)
print(ls)
