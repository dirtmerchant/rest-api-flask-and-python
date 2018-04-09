#should_continue = True
#if asdf:
#    print("Hello")

known_people = ["John", "Anna", "Mary"]
person = input("Enter the person you know: ")

#if person in known_people:
#    print("You know this person!")
#
#if person not in known_people:
#    print("You don't know this person!")

if person in known_people:
    print("You know {}!".format(person))
else:
    print("You don't know {}!".format(person))
