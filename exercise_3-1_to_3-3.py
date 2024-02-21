'''
Try these short programs to get some firsthand experience with Python’s lists.
You might want to create a new folder for each chapter’s exercises to keep 
them organized.
3-1. Names: Store the names of a few of your friends in a list called names. Print 
each person’s name by accessing each element in the list, one at a time.
3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just 
printing each person’s name, print a message to them. The text of each message should be the same, but each message should be personalized with the 
person’s name.
3-3. Your Own List: Think of your favorite mode of transportation, such as a 
motorcycle or a car, and make a list that stores several examples. Use your list 
to print a series of statements about these items, such as “I would like to own a 
Honda motorcycle.”
'''

#3-1
names=['Gio','Frank','Joshua']
print(names[0])
print(names[1])
print(names[-1])

#3-2
names=['Gio','Frank','Joshua']
print('Hi '+names[0]+'! How you doing?')
print('Hi '+names[1]+'! How\'s your career?')
print('Hi '+names[-1]+'! What\'s up?')

#3-3
mode_of_transportation = ['train', 'motorcycle','car']
print('Someday, I\'ll own a Yamaha '+mode_of_transportation[1].title()+'.')
print('I want to try Japan\'s famous Bullet'+mode_of_transportation[0].title()+'.')
print('When I become rich, I\'ll buy a limited edition super'+mode_of_transportation[-1]+'.')
