import time
def type_out(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
def dream():
    time.sleep(2)
    print("it was all a dream.")

def loop():
    start = input("You wake up in your bed. Do you get up or go back to sleep?\n 1- Get up\n 2- Go back to sleep\n")
    if start == "1":
        type_out("You get out of bed and look around. You see a balcony, a door, and a cat sitting in the corner. What do you do?\n 1- Open the door\n 2- Pick up the cat\n 3- Walk onto the balcony\n")
        getup = input()
        if getup == "1":
            print("You see yourself laying in bed and you finally realize that you're trapped in a loop. You then die from shock.")
            dream()
        elif getup == "2":
            print("The cat hisses before jumping at you and scratching you. Somehow you bleed out from the tiny scratch and die.")
            dream()
        elif getup == "3":
            balcony = input("You walk outside and see your house is floating in space. What do you do?\n 1- Look out at space\n 2- Walk back inside\n")
            if balcony == "1":
                print("You sit down on a chair and stare out at space before suddenly dying from lack of oxygen.")
                input("You reawake in a room with no windows and a single door. You hear a voice say 'Welcome to the afterlife.' You have two choices: go to heaven or hell.\n 1- Heaven\n 2- Hell\n")
                afterlife = input()
                if afterlife == "1":
                    print("You walk through a bright light and see a beautiful place. You see Scooby Doo. He offers you a glass of water.\n 1- Accept\n 2- Decline\n")
                    water = input()
                    if water == "1":
                        print("The water was very dirty and you die from dysentery.")
                    elif water == "2":
                        print("Scooby Doo is offended. He hits you with the Mystery Machine and you die.")
                    else:
                        print("Invalid input. Please enter 1 or 2.")
                    dream()
                elif afterlife == "2":
                    print("You walk into a room and get crushed by a giant Tetris block over and over for eternity.")
                    dream()
                else:
                    print("Invalid input. Please enter 1 or 2.")
                    dream()
            elif balcony == "2":
                print("As you're walking back inside, you trip and get sucked into endless space. You drift for years and get run over by a space car because you drifted onto a space highway and die.")
            else:
                print("Invalid input. Please enter 1 or 2.")
        elif getup != "1" and getup != "2" and getup != "3":
            pass
        else:
            print("Invalid input. Please enter 1, 2, or 3.")
    elif start == "2":
        print("You lay in bed. You stare at your ceiling. Time passes: seconds, minutes, hours, days, weeks, months, years. You watch as your house is overtaken by nature, the roof collapses and you can finally see the sky. Rain falls, finally a branch falls from a tree. Your final thoughts: finally at peace, no longer trapped in your own mind. Then you wake up—it was all a dream. Would you like to get up or go back to sleep?")
        dream()
    else:
        print("Invalid input. Please enter 1 or 2")

while True:
    loop()
