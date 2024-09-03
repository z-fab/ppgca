from random import randrange
import random
from util import timer

# https://github.com/TheAlgorithms/Python
# https://www.programiz.com/dsa/bubble-sort


@timer
def bubble_sort(collection: list[int]) -> list[int]:
    # https://www.programiz.com/dsa/bubble-sort
    collection = collection.copy()
    n = len(collection)
    for i in range(n):
        for j in range(0, n - i - 1):
            if collection[j] > collection[j + 1]:
                collection[j], collection[j + 1] = collection[j + 1], collection[j]
    return collection


@timer
def optimized_bubble_sort(collection: list[int]) -> list[int]:
    # https://www.programiz.com/dsa/bubble-sort
    collection = collection.copy()
    for i in range(len(collection)):
        # keep track of swapping
        swapped = False

        # loop to compare collection elements
        for j in range(0, len(collection) - i - 1):
            # compare two adjacent elements
            # change > to < to sort in descending order
            if collection[j] > collection[j + 1]:
                # swapping occurs if elements
                # are not in the intended order
                temp = collection[j]
                collection[j] = collection[j + 1]
                collection[j + 1] = temp

                swapped = True

        # no swapping means the array is already sorted
        # so no need for further comparison
        if not swapped:
            break
    return collection


@timer
def selection_sort(collection: list[int]) -> list[int]:
    # https://github.com/TheAlgorithms/Python/blob/master/sorts/selection_sort.py
    collection = collection.copy()
    length = len(collection)
    for i in range(length - 1):
        min_index = i
        for k in range(i + 1, length):
            if collection[k] < collection[min_index]:
                min_index = k
        if min_index != i:
            collection[i], collection[min_index] = collection[min_index], collection[i]
    return collection


@timer
def insertion_sort(collection: list[int]) -> list[int]:
    # https://github.com/TheAlgorithms/Python/blob/master/sorts/insertion_sort.py
    collection = collection.copy()
    for insert_index in range(1, len(collection)):
        insert_value = collection[insert_index]
        while insert_index > 0 and insert_value < collection[insert_index - 1]:
            collection[insert_index] = collection[insert_index - 1]
            insert_index -= 1
        collection[insert_index] = insert_value
    return collection


@timer
def merge_sort(collection: list[int]) -> list[int]:
    # https://github.com/TheAlgorithms/Python/blob/master/divide_and_conquer/mergesort.py
    collection = collection.copy()

    def merge(left_half: list, right_half: list) -> list:
        sorted_array = [None] * (len(right_half) + len(left_half))

        pointer1 = 0  # pointer to current index for left Half
        pointer2 = 0  # pointer to current index for the right Half
        index = 0  # pointer to current index for the sorted array Half

        while pointer1 < len(left_half) and pointer2 < len(right_half):
            if left_half[pointer1] < right_half[pointer2]:
                sorted_array[index] = left_half[pointer1]
                pointer1 += 1
                index += 1
            else:
                sorted_array[index] = right_half[pointer2]
                pointer2 += 1
                index += 1
        while pointer1 < len(left_half):
            sorted_array[index] = left_half[pointer1]
            pointer1 += 1
            index += 1

        while pointer2 < len(right_half):
            sorted_array[index] = right_half[pointer2]
            pointer2 += 1
            index += 1

        return sorted_array

    if len(collection) <= 1:
        return collection
    # the actual formula to calculate the middle element = left + (right - left) // 2
    # this avoids integer overflow in case of large N
    middle = 0 + (len(collection) - 0) // 2

    # Split the collection into halves till the collection length becomes equal to One
    # merge the collections of single length returned by mergeSort function and
    # pass them into the merge collections function which merges the collection
    left_half = collection[:middle]
    right_half = collection[middle:]

    return merge(merge_sort(left_half)[0], merge_sort(right_half)[0])


@timer
def quick_sort(collection: list[int]) -> list[int]:
    # https://github.com/TheAlgorithms/Python/blob/master/sorts/quick_sort.py
    collection = collection.copy()
    random.seed(42)

    # Base case: if the collection has 0 or 1 elements, it is already sorted
    if len(collection) < 2:
        return collection

    # Randomly select a pivot index and remove the pivot element from the collection
    pivot_index = randrange(len(collection))
    pivot = collection.pop(pivot_index)

    # Partition the remaining elements into two groups: lesser or equal, and greater
    lesser = [item for item in collection if item <= pivot]
    greater = [item for item in collection if item > pivot]

    # Recursively sort the lesser and greater groups, and combine with the pivot
    return [*quick_sort(lesser)[0], pivot, *quick_sort(greater)[0]]
