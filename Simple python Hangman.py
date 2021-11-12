import random #brings in random function
#Made By Blake McCullough
#Discord - Spoiled_Kitten#4911
#Github - https://github.com/Blake-McCullough/
#Email - privblakemccullough@protonmail.com

print("Random dice roller by Blake McCullough") #displays creators name
print("Would you like the dice to")#asks what the user would like the program to do
print("(1) Multiply")
print("(2) Add")
print("(3) Display all roles")

option = int(input(""))#takes the input as an integer for what user has decided the program to do

sides = int(input("Pick a number of sides:  ")) #takes the input as an integer for how many sides the dice will have

dice = int(input("Pick a number of dice:  ")) #takes the input as an integer for how many dice rolls there will be


i = 1 #sets variable for loop
total = 0   #sets variable for the total

if option == 1: #if the option was multiply then it runs this
    while i <= dice: #while the number of dice are lower then how many loops has run it will multiply to the total score
        total=total+(random.randint(1, sides))# multiplys a random number from 1 to how many sides the user has decided to the total
        i=i+1#adds 1 to the loop so it can see how many times it has run
    print(total)#displays the total score
    
elif option == 2: #if the option was multiply then it runs this
    while i <= dice:#while the number of dice are lower then how many loops has run it will add to the total score
        total=total+(random.randint(1, sides)) # adds a random number from 1 to how many sides the user has decided to the total
        i=i+1 #adds 1 to the loop so it can see how many times it has run
    print(total)#displays the total score
        
elif option == 3: #if the option was multiply then it runs this
    while i <= dice:#while the number of dice are lower then how many loops has run it will show all the rolls run by the dice
        i=i+1#adds 1 to the loop so it can see how many times it has run
        total=(random.randint(1, sides)) #sets the random number from 1 to how many sides the user has decided, so it can be displayed
        print(total)#displays the total score
else: #if the option wasn't anything then it runs this
    print("error") #displays error to let user know that there option was invalid
print("Thanks for using my program")#thanks user for using the program




