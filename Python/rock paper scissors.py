import random
rock = """
      ________  
______|       )
        ------
        (--------)
        (---------)
        (--------)  
---|_____(--------)

 """
paper = """

       ___________
------(   _________)______
           _______________)
            ________________)
__________  _______________)
          (_____________)
        
                 """
scissors = """

       __________
_______|   ______)______
             ___________)
             _____________)
_____   (_________)
    '_(________)      """
choices = [rock, paper, scissors]


while True:
    try:
        user = int(input("Enter 0 for Rock, 1 for Paper, 2 for Scissors: "))

        if user not in [0, 1, 2]:
            print("Invalid input! Please enter 0, 1, or 2.")
            continue

        computer = random.randint(0, 2)

        print("\nYou chose:")
        print(choices[user])

        print("Computer chose:")
        print(choices[computer])

        
        if user == computer:
            print("you win!")
        elif (user == 0 and computer == 2) or \
             (user == 1 and computer == 0) or \
             (user == 2 and computer == 1):
            print("you win!")
        else:
            print("You win!")

        
        again = input("\nDo you want to play again? (y/n): ").lower()
        if again != 'y':
            print("Thanks for playing!")
            break

    except ValueError:
        print("Please enter a valid number (0, 1, or 2).")