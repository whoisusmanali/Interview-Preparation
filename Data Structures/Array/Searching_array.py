#simple list
values = [90, 9, 3, 80, 60, 30, 48, 558]

def search_array(value, list_of_values):
    for i in list_of_values:
        if i == value:
            return True
    return False

search_array_item = search_array(80, values)
#print(search_array_item)
#Time complexity is O(N)

#We can use the pre-defined function as well to find

values.index(90) 