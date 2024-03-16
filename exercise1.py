def replace_last(numbers):
    
    result = numbers[-1:] + numbers[:-1]
     
    return result

print(replace_last([2, 3, 4, 1]))