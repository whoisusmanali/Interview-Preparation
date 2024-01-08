seating_chart = [
    ["Sarah", "CLaire", "Ben", "Taylor", "Eva"],
    ["Frankie", "George", "Lindsey", "Izzy", "Jack"],
    ["Katherine", "Lauren", "Mary", "Nathan", "Olive"],
    ["Chad", "April", "Matt", "Thomas", "Penny"]
]

#How is on row 3 and seat 2
print(seating_chart[2][1])

#What if I have to show the all the students with row number
"""for i ,row in enumerate(seating_chart):
    print(f"Students {row} are in {i+1} row")"""


#Similarly for to find the seat number as well
for row, values in enumerate(seating_chart):
    for seat, name in enumerate(values):
        print(f"Student: {name} is in {row+1} row and at {seat+1} seat number")