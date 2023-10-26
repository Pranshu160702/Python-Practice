import random

# d for draw, w for win and l for lose
results = [["d","w","l"],["l","d","w"],["w","l","d"]]
computer_choices = [1,2,3]
choices_c = ["Computer chooses Snake","Computer chooses Water","Computer chooses Gun"]
choices_p = ["You chose Snake","You chose Water","You chose Gun"]

print("Welcome to Stone Paper Scissor!")
print("Choices are as follows : \n1: Snake\n2: Water\n3: Gun")
while(True):
    player_choice = int(input("Enter A Choice : "))
    print(choices_p[player_choice-1])
    if(player_choice in range(1,4)):
        computer_choice = int(random.choice(computer_choices))
        print(choices_c[computer_choice-1])
        result = results[player_choice-1][computer_choice-1]
        if(result == "w"):
            print("You Won")
        elif(result == "d"):
            print("You Drew") 
        else:
            print("You Lost")
    else:
        print("Please Enter A Valid Choice!")