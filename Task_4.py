import random

player = ['Rock', 'Paper', 'Scissors']
computer = ['Rock', 'Paper', 'Scissors']

print("********** ROCK, PAPER, SCISSORS GAME **********")
print("1. Rock\n2. Paper\n3. Scissors")
p = int(input("Enter your choice : "))
c = random.randint(0, 2)

choice1 = player[p-1]
choice2 = computer[c]

print()
print("\nYour Choice : " + choice1)
print("Bot's Choice : " + choice2)
print()

if choice1 == 'Rock' and choice2 == 'Rock' : print("It's Draw")
elif choice1 == 'Rock' and choice2 == 'Paper' : print("Bot Win..!!")
elif choice1 == 'Rock' and choice2 == 'Scissors' : print("You Win..!!")
elif choice1 == 'Paper' and choice2 == 'Rock' : print("You Win..!!")
elif choice1 == 'Paper' and choice2 == 'Paper' : print("It's Draw")
elif choice1 == 'Paper' and choice2 == 'Scissors' : print("Bot Win..!!")
elif choice1 == 'Scissors' and choice2 == 'Rock' : print("Bot Win..!!")
elif choice1 == 'Scissors' and choice2 == 'Paper' : print("You Win..!!")
elif choice1 == 'Scissors' and choice2 == 'Scissors' : print("It's Draw")