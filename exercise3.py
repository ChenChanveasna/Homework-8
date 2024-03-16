def remove_all_after(numbers, n):
    # create a new empty list
    new_list = []

    # loop in list of numbers
    for x in numbers:

        # if numbers not equal to n, then append it to new list
        if x != n:
            new_list.append(x)
        
        # if we found x equal to n where we need to stop, append x to list and break the loop, which mean we don't take any number after that x
        elif x == n:
            new_list.append(x)
            break
    
    # return the new list
    return new_list