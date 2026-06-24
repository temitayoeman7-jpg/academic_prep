state = "red"

while True:
    if state == "red":
        print("red")
        state = "green" 
    elif state == "green":
        print("green")
        state = "yellow"
    else:
        print("yellow")
        state = "red"
        
    # Indented to be inside the while loop
    user_input = input("type quit to stop: ")
    if user_input == "quit":
        break
