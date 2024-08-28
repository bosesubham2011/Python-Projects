print("Welcome to the Quiz!")

play = input("Do you want to play this game? Y/N (Anything other than Y or y will be considered as No) ")

if play.lower() != 'y':
    quit()

print("Okay! Let's play")

score = 0

ans = input("What does CPU stand for? ")
if ans.lower() == "central processing unit":
    print("Correct!")
    score+=1
else:
    print("Incorrect! Try again!")

ans = input("What does GPU stand for? ")
if ans.lower() == "graphics processing unit":
    print("Correct!")
    score+=1
else:
    print("Incorrect! Try again!")

ans = input("What does RAM stand for? ")
if ans.lower() == "random access memory":
    print("Correct!")
    score+=1
else:
    print("Incorrect! Try again!")

ans = input("What does PSU stand for? ")
if ans.lower() == "power supply unit":
    print("Correct!")
    score+=1
else:
    print("Incorrect! Try again!")


print("You got "+str(score)+" questions correct!")
print("You got "+str((score/4)*100)+"%.")


