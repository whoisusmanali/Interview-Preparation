#Find the second smallest number from an array
# Return None if the list has zero or one element

values = [1,4,2,7,3,9,6]

def second_smallest_number(list_of_values):
    if len(list_of_values) == 0 or len(list_of_values) == 1:
        return None
    else:
        sorted_list = sorted(list_of_values)
        return sorted_list[1]
    
Second_smallest_number = second_smallest_number(values)
print(Second_smallest_number)



#Or we can do this without sorting it
# [1,4,2,7,3,9,6]
def second_smallest_number1(list_of_values):
    if len(list_of_values) < 2:
        return None
    smallest = float('inf')
    second_smallest = float('inf')

    for i in values:
        if i<smallest:
            second_smallest = smallest
            smallest = i
        elif i<second_smallest:
            second_smallest = i
    return second_smallest
    
Second_smallest_number1 = second_smallest_number1(values)
print(Second_smallest_number1)
