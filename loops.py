#my_variable = "hello"

#for character in my_variable: #iterables are strings, lists tuples, and more...
#    print(character)
#
#for blah in my_variable: #iterables are strings, lists tuples, and more...
#    print(blah)
#
#my_list = [1, 3, 5, 7, 9]
#
#for number in my_list:
#    print(number ** 2)

user_wants_number = True
while user_wants_number == True:
    print(10)

    user_input = input("Should we print again (y/n)")
    if user_input == 'n':
        user_wants_number = False
