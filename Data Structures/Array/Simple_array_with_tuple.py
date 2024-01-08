# a simple tuple to get the values from a function
def total_marks (marks, extra_marks, bonus, Special_marks):
    marks = marks + extra_marks
    marks = marks + bonus
    marks = marks + Special_marks
    total_extra_marks = extra_marks + bonus + Special_marks
    return (marks, total_extra_marks)

result = total_marks(9, 50, 10, 5)
print("Total Marks", result[0])
print("Extra Marks", result[1])