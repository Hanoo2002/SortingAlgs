from quicksort import partitioning


def find_kth_smallest_element_imp(arr, first, last, k):
    """
    Implementation of Quick sort
    :param k:
    :param arr:
    :param first:
    :param last:
    :return:
    """
    if first < last:
        pivot_index = partitioning(arr, first, last)
        if pivot_index == k:
            return arr[pivot_index]
        elif pivot_index > k:
            return find_kth_smallest_element_imp(arr, first, pivot_index - 1, k)
        else:
            return find_kth_smallest_element_imp(arr, pivot_index + 1, last, k)


def find_kth_element(arr, k):
    return find_kth_smallest_element_imp(arr, 0, len(arr) - 1, k)


ls = [12, 34, 5, 1, 62, 23, 56, 45, 356, 82, 7623]
print(find_kth_element(ls, 6))
