print("*****Welcome to my Computer Quiz!*****")

# Taking user input
playing = input("Do you want to play? ").lower().strip()

# Quiz start or exit
if playing != "yes":
    print("Good Bye!")
    quit()
else:
    print("Quiz Start!!!")


# declare score for showing final score of Quiz
score = 0

# score increment and checking user answer is right or wrong
answer = input("What does CPU stand for? ").lower().strip()
if answer == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does GPU stand for? ").lower().strip()
if answer == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ").lower().strip()
if answer == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does ROM stand for? ").lower().strip()
if answer == "read only memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# display the final score and percentage
print("Your final score is : "+str(score))
print("You got"+str((score/4)*100)+"%.")
