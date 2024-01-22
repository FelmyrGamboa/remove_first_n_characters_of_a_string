# Exercise 4: Remove first n characters from a string
# Write a program to remove characters from a string starting from zero up to n and return a new string.

#Let user type something
string_input = input("Please type something: ")

#Let user decide how many characters will be removed from the input
remove_charac = int(input("\nHow many characters do you want to remove? "))

#Create the condition to remove n characters fron the string
removed_charac = string_input[remove_charac:]

#Display the result
print("\nThe output is", removed_charac)