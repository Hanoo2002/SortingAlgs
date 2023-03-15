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


def merge_sort_implementation(arr, first, last, threshold):
    """
    Implements merge sort algorithm
    :param threshold:
    :param arr:
    :param first:
    :param last:
    :return:
    """
    if last - first <= threshold:  # starts selection sort at threshold
        selection_sort(arr, first, last)
    else:
        mid = (first + last) // 2
        merge_sort_implementation(arr, first, mid, threshold)
        merge_sort_implementation(arr, mid + 1, last, threshold)
        merge(arr, first, mid, last)


def hybrid_merge_sort(arr, threshold):
    """
    interface with hybrid_merge_sort_implementation
    :param threshold:
    :param arr:
    :return:
    """
    merge_sort_implementation(arr, 0, len(arr) - 1, threshold)


def selection_sort(arr, first, last):
    """
    selection sort algorithm
    :param arr:
    :param first:
    :param last:
    :return:
    """
    n = (first + last + 1)//2
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]


ls = [12, 34, 5, 1, 62, 23, 56, 45, 356, 82, 7623]
hybrid_merge_sort(ls, 3)
print(ls)
