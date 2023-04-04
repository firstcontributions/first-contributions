def bubble_sort(numbers):
    for i in range(len(numbers)-1):
        for j in range(i,len(numbers)):
            if numbers[i] > numbers[j]:
                numbers[i],numbers[j] == numbers[j],numbers[i]
    return numbers

print(bubble_sort([1,2,3,2,2,3,2,2,4,3,567,5,4,7,96,4,34]))
