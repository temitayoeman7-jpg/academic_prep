import random
number=random.randint(1,100)
count=0
while True:
    try :
        user_num=int(input("guess a number:"))
        count+=1
    except ValueError:
        print("enter a valid number")
        continue
    if user_num>number:
        print("Too high , Please try again")
    elif user_num<number:
        print("Too low please try again")
    else:
        print("Correct")
        break
print(f"you guessed {count} times")

