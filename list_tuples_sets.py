my_variable = "hello"

#grade_one = 77
#grade_two = 80
#grade_three = 90

#print((grade_one + grade_two + grade_three) / 3)

#list
grades = [77, 80, 90, 95, 100]
#tuple immutable
tuple_grades = (77, 80, 90, 95, 100)
#set unique and unordered
set_grades = {77, 80, 90, 100, 100}

set_grades.add(60)
set_grades.add(60)
#print(set_grades)

## Set operations

your_lottery_numbers = {1, 2, 3, 4, 5}
winning_numbers = {1, 3, 5, 7, 9, 11}

#print(your_lottery_numbers.intersection(winning_numbers))
print(your_lottery_numbers.union(winning_numbers))
