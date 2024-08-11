import random
name = ["rock", "paper", "scissor"]
user_choice = input("Enter choice name: ")
cmp_choice = random.choice(name)

print(f"User choice {user_choice}, computer choice {cmp_choice}")

if user_choice == cmp_choice:
    print("Match draw")
elif user_choice == "rock":
    if cmp_choice == "paper":
        print("computer Win")
    else:
        print("You win")
elif user_choice == "paper":
    if cmp_choice == "scissor":
        print("Computer win")
    else:
        print("you win")
elif user_choice == "scissor":
    if cmp_choice == "paper":
        print("You win")
    else:
        print("Computer win")
else:
    print("Game Over")