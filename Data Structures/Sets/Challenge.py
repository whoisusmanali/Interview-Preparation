def unique_check(data):
    set1 = set(data)
    return len(set1) == len(data)

print(unique_check("Simple"))
print(unique_check("hello"))