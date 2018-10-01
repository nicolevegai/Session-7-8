string = input("Please input some letters of the alphabet: ")
abc = "abcdefghijklmnopqrstuvwxyz"
substring = ""
submax = ""
counter = 1
for letter in string:
    if len(submax) < len(substring):
        submax = substring




print("The longest string of characters in alphabetical order is: " + submax)
