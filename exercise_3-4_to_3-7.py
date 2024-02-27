'''
The following exercises are a bit more complex than those in Chapter 2, but 
they give you an opportunity to use lists in all of the ways described.
3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who 
would you invite? Make a list that includes at least three people you’d like to 
invite to dinner. Then use your list to print a message to each person, inviting 
them to dinner.
3-5. Changing Guest List: You just heard that one of your guests can’t make the 
dinner, so you need to send out a new set of invitations. You’ll have to think of 
someone else to invite.
•	 Start with your program from Exercise 3-4. Add a print statement at the 
end of your program stating the name of the guest who can’t make it.
•	 Modify your list, replacing the name of the guest who can’t make it with 
the name of the new person you are inviting.
•	 Print a second set of invitation messages, one for each person who is still 
in your list.
3-6. More Guests: You just found a bigger dinner table, so now more space is 
available. Think of three more guests to invite to dinner.
•	 Start with your program from Exercise 3-4 or Exercise 3-5. Add a print
statement to the end of your program informing people that you found a 
bigger dinner table.
•	 Use insert() to add one new guest to the beginning of your list.
•	 Use insert() to add one new guest to the middle of your list.
•	 Use append() to add one new guest to the end of your list.
•	 Print a new set of invitation messages, one for each person in your list.
'''
#3-4
guess_list = ["Lester","Erico","Olga"]
message="Come join us, "+guess_list[0]+"."
print(message)
message="Come join us, "+guess_list[1]+"."
print(message)
message="Come join us, "+guess_list[2]+"."
print(message)
print('\n')

#3-5
print(guess_list[0]+" can't join us.")
guess_list[0] = 'Jun'
message="Come join us, "+guess_list[0]+"."
print(message)
message="Come join us, "+guess_list[1]+"."
print(message)
message="Come join us, "+guess_list[2]+"."
print(message)
print('\n')

#3-6
print("I found a bigger table for us.")
guess_list.insert(0,"Cora")
guess_list.insert(2,"Liza")
guess_list.append("Teresita")
message="Come join us, "+guess_list[0]+"."
print(message)
message="Come join us, "+guess_list[1]+"."
print(message)
message="Come join us, "+guess_list[2]+"."
print(message)
message="Come join us, "+guess_list[3]+"."
print(message)
message="Come join us, "+guess_list[4]+"."
print(message)
message="Come join us, "+guess_list[5]+"."
print(message)
print('\n')

#3-7
print("Sorry I can\'t invite you all.")
popped_guess = guess_list.pop()
print("Sorry "+popped_guess+". We can\'t invite you anymore.")
popped_guess = guess_list.pop()
print("Sorry "+popped_guess+". We can\'t invite you anymore.")
popped_guess = guess_list.pop()
print("Sorry "+popped_guess+". We can\'t invite you anymore.")
popped_guess = guess_list.pop()
print("Sorry "+popped_guess+". We can\'t invite you anymore.")
print("You are still invited, "+guess_list[0]+".")
print("You are still invited, "+guess_list[1]+".")
del guess_list[0]
del guess_list[0]
print(guess_list)
print('\n')



