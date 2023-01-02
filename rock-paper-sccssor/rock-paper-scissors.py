from random import randint

choice = ["rock", "paper", "scissor"]

while True:
    computer = choice[randint(0,2)]
    person = input("\nEnter Choice:\n 1.rock \t 2.paper \t 3.scissor \t 4.end\n::")
    if person == "end":
        print("Ending the game!")
        break
    elif person == computer:
        print(" Match Tie! ")
    elif person == "rock":  
        if computer == "scissor":
            print(f"{person} >> {computer} Person Won!!")
        else:
            print(f"{computer} >> {person} Computer Won!!")
    elif person == "paper":  
        if computer == "rock":
            print(f"{person} >> {computer} Person Won!!")
        else:
            print(f"{computer} >> {person} Computer Won!!")   
    elif person == "scissor":  
        if computer == "paper":
            print(f"{person} >> {computer} Person Won!!")
        else:
            print(f"{computer} >> {person} Computer Won!!")
    else:
        print("Enter Valid Choice!!")