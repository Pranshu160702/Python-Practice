questions = [
    "Who is the prime minister of India?",
    "What is schrizophenia?",
    "How many continents are there in the world?"             
]

answers = [
    "Narendra Modi",
    "Disease",
    "7"
]

prize = [
    1000,
    5000,
    10000
]

prize_money = 0

for i in range(0,3):
    print(questions[i])
    user_ans = str(input("Your Answer : "))
    if(user_ans == answers[i]):
        prize_money = prize[i]
    else:
        print("Better Luck Next Time")
        break
    
print("You won a total of : ", prize_money)