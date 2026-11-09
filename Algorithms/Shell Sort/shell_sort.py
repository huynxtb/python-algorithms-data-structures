def shell_sort(arr):
    n = len(arr)
    # Start with a big gap, then reduce the gap
    gap = n // 2  
    # Do a gapped insertion sort for this gap size.
    while gap > 0:
        for i in range(gap, n):
            # Save arr[i] in temp and make a hole at position i
            temp = arr[i]
            # Shift earlier gap-sorted elements up until the correct location for arr[i] is found
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            # Put temp (the original arr[i]) in its correct location
            arr[j] = temp
        gap //= 2  # Reduce the gap for the next element
    return arr
