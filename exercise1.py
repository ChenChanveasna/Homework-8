def replace_last(numbers):
    
    results = numbers[-1:] + numbers[:-1]
     
    return results

print(replace_last([2, 3, 4, 1]))