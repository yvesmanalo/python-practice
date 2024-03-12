
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
#     The remove() method deletes only the first occurrence of the value you specify. If there’s a possibility the value appears more than once in the list, you’ll need to use a # #     loop to determine if all occurrences of the value have been removed


#Organizing a List
#     Sorting a List Permanently with the sort() Method
#           name_of_list.sort() ---> change the order of the list to store them alphabetically.
#           for reverse alphabetical order:
#           name_of_list.sort(reverse=True)
#     Sorting a List Temporarily with the sorted() Function
#           sorted(name_of_list) ---> display your list in a particular order but doesn’t affect the actual order of the list.
#           for reverse alphabetical order(temporarily):
#           sorted(name_of_list,reverse=True)
#     Sorting a list alphabetically is a bit more complicated when all the values are not in lowercase. There are several ways to interpret capital letters when you’re deciding on  
#     a sort order, and specifying the exact order can be more complex than we want to deal with at this time. However, most approaches to sorting will build directly on what you 
#     learned in this section.
#
#     Printing a List in Reverse Order
#     To reverse the original order of a list, you can use the reverse() method.
#           name_of_list.reverse() ---> reverse() doesn’t sort backward alphabetically; it simply reverses the order of the list
#      reverse() method changes the order of a list permanently, but you can revert to the original order anytime by applying reverse() to the same list a second time.
#
#     Finding the Length of a List
#           len() function
#           len(name_of_list)
#     Python counts the items in a list starting with one, so you shouldn’t run into any off by-one errors when determining the length of a list.


#Avoiding Index Errors When Working with Lists
#     An index error means Python can’t figure out the index you requested. If an index error occurs in your program, try adjusting the index you’re asking for by one.
#     Keep in mind that whenever you want to access the last item in a list you use the index -1
#             name_of_list[-1] --> last item in the list
#     If an index error occurs and you can’t figure out how to resolve it, try printing your list or just printing the length of your list. Your list might look much different than #     you thought it did, especially if it has been managed dynamically by your program. Seeing the actual list, or the exact number of items in your list, can help you sort out #     such logical errors.

#Working with Lists
#Looping Through an Entire List
#     When you want to do the same action with every item in a list, you can use Python’s for loop.
#     for items in name_of_lists:
#          print(items)
#Doing Something after a "for" Loop
#     Any lines of code after the for loop that are not indented are executed once without repetition.
#     for items in name_of_lists:
#          print(items)
#     print("this will be printed after looping in the items in name_of_lists")
'''

#Making Numerical Lists
#Using the range() Function
#     The range() function causes Python to start counting at the first value you give it, and it stops when it reaches the second value you provide. Because it stops at that
#     second value, the output never contains the end value
#     If your output is different than what you expect when you’re using range(), try adjusting your end value by 1.
#Using range() to Make a List of Numbers
#     If you want to make a list of numbers, you can convert the results of range() directly into a list using the list() function. When you wrap list() around a call to the 
#     range() function, the output will be a list of numbers
#             numbers = list(range(1,6))
#             print(numbers)
#             output ----> [1, 2, 3, 4, 5]
#     We can also use the range() function to tell Python to skip numbers in a given range.
#      





