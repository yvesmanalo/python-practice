
'''
print("hello world")

#variables
message = "hello world"
print(message)

#methods
name="ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())


#concatenation
first_name="ada"
last_name="lovelace"
full_name=first_name+" "+last_name
#print(full_name)
#print("Hello, "+full_name.title()+"!")
message="Hello, "+full_name.title()+"!"
print(message)


#whitespaces
#tab
print("\tPython")
#newline
print("Languages:\nPython\nC\nJavaScript")
#tab and newline combine
print("Languages\n\tPython\n\tC\n\tJavaScript")


#stripping whitespaces
#temporarily remove
favorite_language = "python "
print(favorite_language.rstrip())
print(favorite_language)
#permanently remove
favorite_language = favorite_language.rstrip()
print(favorite_language)
#remove white space on the left side
favorite_language = " python"
favorite_language = favorite_language.lstrip()
print(favorite_language)
#remove white space on both side
favorite_language = " python "
favorite_language = favorite_language.strip()
print(favorite_language)


#syntax error
#message='One of Python's strengths is its diverse community.'  ---not valid python code
#print(message)

#numbers
#add(+)
#subtract(-)
#multiply(*)
#divide(/)
#exponention(**)
#Python also follows order of operation

#floats - any number with decimal point
#Python tries to find a way to represent the result as precisely as possible, which is sometimes difficult given how computers have to represent numbers internally
#>>> 0.2 + 0.1 
#0.30000000000000004 

#type errors with str() function - integer + string lead to error
#TypeError: Can't convert 'int' object to str implicitly
#str() function - to specify explicitly that you want Python to use the integer as a string of characters.

age = 23
message = "Happy " + str(age) + "rd Birthday!"
print(message)
'''

#Lists
#Accessing Element in a List
#    index - element position
#    syntax: name_of_list[index]
#    1st element of a list has index of 0
#    can also be combined with methods
#    example: bicycles = ['trek', 'cannondale', 'redline', 'specialized']
#    print(bicycles[0].title())  ---> output: 'Trek'
#    inversed indexing : name_of_list[-1] ---> returns last element in a list

#Modifying Elements in a List
#    changing value in a list
#         name_of_list[index_number] = 'new value'

#Adding ELements in a List
#    adding elements at the end of the list (Appending)
#         name_of_list.append('new value to be added')

#Inserting Elements in a List
#    for any position on a list
#         names_of_list.insert(index position, value to be inserted)

#Removing Elements in a List
#     using del statement
#         del name_of_list[0] ---> removes the first element of the list
#     using pop() method -- removes the last element in a list but lets you work with that item after moving it
#     popping items from any position in a list
#         new_variable = name_of_list.pop(index number)
#     when you want to delete an item from a list and not use that item in any way, use the del statement; if you want to use an item as you remove it, use the pop() method.
#     removing elements by value using remove() method
#         name_of_list.remove(value)
#     You can also use the remove() method to work with a value that’s being removed from a list.
#     The remove() method deletes only the first occurrence of the value you specify. If there’s a possibility the value appears more than once in the list, you’ll need to use a loop to determine if all occurrences of the value have been removed




