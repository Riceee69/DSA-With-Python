def merge_sort(numbers: list):
    length = len(numbers)
    if(length == 1):
        return numbers

    mid = length // 2
    left = numbers[:mid]
    right = numbers[mid:]

    return merge(merge_sort(left), merge_sort(right))

def merge(array1: list, array2: list):
    result = []
    i, j = 0, 0

    while i < len(array1) and j < len(array2):
        if array1[i] < array2[j]:
            result.append(array1[i])
            i += 1
        else:
            result.append(array2[j])
            j += 1            

    result.extend(array1[i:])
    result.extend(array2[j:])
    return result