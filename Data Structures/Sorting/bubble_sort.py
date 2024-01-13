def bubblesort(elements):
    swap = False

    for i in range(len(elements)-1):
        for j in range(0, len(elements)-i-1):
            if elements[j] > elements[j+1]:
                swap = True
                elements[j], elements[j+1] = elements[j+1], elements[j]

        if not swap:
            return
        

arr = [1, 65, 90, 32, 60, 40, 33]
print("List before sorted:",arr)
Bubblesort = bubblesort(arr)
print("List after sorted:",arr)

