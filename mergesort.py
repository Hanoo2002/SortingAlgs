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
