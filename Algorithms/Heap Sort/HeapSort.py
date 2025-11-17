def heapify(arr, n, i):
    """
    Helper function to maintain the max-heap property for a subtree rooted at index i,
    assuming the subtrees are already heaps.

    Args:
        arr (list of int): The list to heapify.
        n (int): The size of the heap within arr.
        i (int): The root index of the subtree to heapify.
    """
    largest = i  # Initialize largest as root
    left = 2 * i + 1  # left child index
    right = 2 * i + 2  # right child index

    # See if left child exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # See if right child exists and is greater than current largest
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Change root if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap

        # Heapify the root that was changed
        heapify(arr, n, largest)


def build_max_heap(arr):
    """
    Converts an array into a max heap.

    Args:
        arr (list of int): The array to build the max heap.
    """
    n = len(arr)

    # Start from the last internal node and heapify
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)


def heap_sort(arr):
    """
    Perform heap sort on the given array in-place.

    Args:
        arr (list of int): The array to be sorted.
    """
    n = len(arr)

    build_max_heap(arr)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # Swap current root to the end
        heapify(arr, i, 0)  # Heapify the reduced heap
