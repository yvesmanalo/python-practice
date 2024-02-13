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
'''

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
