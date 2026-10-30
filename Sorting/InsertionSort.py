def insertion_sort(numbers: list):
    for i in range(1, len(numbers)):
        number = numbers[i]
        j = i-1
        while j >= 0 and number < numbers[j]:
            numbers[j+1] = numbers[j]
            j -= 1
        numbers[j+1] = number
    return numbers