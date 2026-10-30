def bubble_sort(numbers: list):
    numbers_length = len(numbers)
    for j in range(1, numbers_length):
        for i in range(numbers_length - j):
            if numbers[i] > numbers[i+1]:
                hold = numbers[i]
                numbers[i] = numbers[i+1]
                numbers[i+1] = hold
    return numbers

        
