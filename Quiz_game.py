import random

# Add question and answers here as key : value pairs

question_and_answers = {
    "what does the cpu stands for" : "central processing unit",
    "what does the gpu stands for" : "graphics processing unit",
    "5 x 8 = "                     : "40",
    "12 x 4 = "                    : "48",

}

point = 0
total_points = 0

def play(qna):
    score = 0
    questions = list(qna.items())
    random.shuffle(questions)


    for question, answer in questions:
        ans = input(question + "? : ")
        if ans.lower().strip() == answer.lower():
            print("The answer is correct")
            score += 1
            print(score)

        else:
            print(f"You entered the wrong answer\nThe correct answer is {answer}\n ")

        play_again = input("Press 'Enter' to continue ('q' to quit) \n")

        if play_again.lower().strip() != "q":
            continue
        else:
            break
    return score
            
            
        


# Main
start = input("Do You want to play the game? (Yes / No)")
if start.lower().strip() != "yes":
    print ("You Exited")
else:
    while True:
        point = play(question_and_answers)
        total_points += point
        print(f" Total Score = {total_points}")

        play_again = input("Do you want to play agian ? (Yes / No) ")
        if play_again.strip().lower() != "yes":
            break
print("Game over! Final score is", total_points)






