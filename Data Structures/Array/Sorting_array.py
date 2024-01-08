
#simple list 
values = [2,4,5,7,9,2,3,4,5,6,12,3,4,5]
print(sorted(values))

values = [('Usman', 90), ('Ali', 43), ('Zahid', 80)]
#It sort by using names 
print(sorted(values))
#Sorting by using score
print(sorted(values, key=lambda x : x[1]))