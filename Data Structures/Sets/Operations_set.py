set1 = {10, 20, 30, 40, 50}
set2 = {10, 30, 50, 70, 90}

#Sum of both
intercetion = set1.intersection(set2)
print(intercetion)

union = set1.union(set2)
print(union)

difference = set1.difference(set2)
print(difference)

sysmetric = set1.symmetric_difference(set2)
print(sysmetric)