def quick_sort(numbers: list, left, right):
    if(left < right):
        partition_index = find_partition_index(numbers, left, right)

        # quick sort the left and right splits
        quick_sort(numbers, left, partition_index-1)
        quick_sort(numbers, partition_index+1, right)

    return numbers


def find_partition_index(numbers, left, pivot):
    pivot_value = numbers[pivot]
    partition_index = left

    for i in range(left, pivot):
        if numbers[i] < pivot_value:
            numbers[i], numbers[partition_index] = numbers[partition_index], numbers[i]
            partition_index += 1
    # Final Swap to Input the pivot_value at partition_index
    numbers[pivot], numbers[partition_index] = numbers[partition_index], pivot_value
    return partition_index
