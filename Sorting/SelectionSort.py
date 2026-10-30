def selection_sort(numbers: list):
    length = len(numbers)
    for i in range(length - 1):
        selection = i
        for j in range(i+1, length):
            if numbers[selection] > numbers[j]:
                selection = j
        temp = numbers[i]
        numbers[i] = numbers[selection]
        numbers[selection] = temp
    return numbers

                


                
