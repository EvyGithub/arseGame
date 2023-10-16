import time

# variables
episodeChoice = 1 # which episode is selected, and this will be used throughout the code
episodes = ["Episode 1: Attempting the Arrest", "Episode 2: Locating the Fortress", "Episode 3: Defending the Base", "Episode 4: Fleeing the Vault", "Episode 5: Completing the Job"] # just for episode names
episode = episodes[0] # cosmetic purposes only
FAIL = """
 ______      _____ _      _ 
|  ____/\   |_   _| |    | |
| |__ /  \    | | | |    | |
|  __/ /\ \   | | | |    | |
| | / ____ \ _| |_| |____|_|
|_|/_/    \_\_____|______(_)
"""

TUTORIAL = """
           _______    _             _       _          
          |__   __|  | |           (_)     | |         
  ______     | |_   _| |_ ___  _ __ _  __ _| |  ______ 
 |______|    | | | | | __/ _ \| '__| |/ _` | | |______|
             | | |_| | || (_) | |  | | (_| | |         
             |_|\__,_|\__\___/|_|  |_|\__,_|_|         
"""
# these choice nubmers are seperate for each episode because why not
choiceNumber1 = 1
choiceNumber2 = 1
choiceNumber3 = 1

# functions
def write(txt="", delay=1.5):
    print(txt)
    time.sleep(delay)
    return

def choice(validOptions, prompt=""):
    temp = "2389054g72398b523975bn0932b509650892305b2345b"
    print(prompt)
    while temp not in validOptions:
        temp = input("> ").strip().lower()

    return temp

def fail(flavorText="You failed!"):
    global FAIL

    print("\n" * 69)

    print(FAIL)
    print(flavorText + "\n")

def tutorial():
    write(TUTORIAL, 1)
    write("Chief: Welcome to the Wankopolis police force!", 1.5)
    write("Chief: Everyone! Welcome our new recruit, F!", 1.5)
    write("(You are playing as F.)", 1.5)
    write("Chief: Your goal is to prevent Eli and his goons from carrying out his evil plans.", 2)
    write("Chief: You really look like you need a buddy...", 2)
    write("Chief: Hey, RW! Come over here! Meet your new partner!", 1.5)
    write("RW: Oh, hi there! How's your day?", 1.5)
    write("F: Hi! My day's going great, as I just got here, *chuckles*.", 1.5)
    write("RW: I'm excited to be your new partner!", 1.5)
    write("F: I am too!", 1.5)
    
    write("\nHave fun playing! (type 'done' when you're done reading)", 0)

    temp = "q1g6qgewr2395qbw8476wertn12q24395485768369qwe284r5b7qn254226b5e4,m6789an2t19.85b23495ethiorubgioybqrweghiowberteqrwgybioewrtyewbrti"
    while temp != 'done':
        temp = choice(["done"])
    return

# choose episode
def startMenu():
    global episodeChoice, episodes, episode

    write("\n" * 69 + "Welcome!", 1)

    episodeChoice = 1
    temp = "WOLOLOLO"
    while temp.lower() != "start":
        while temp.lower() not in [">", "<", "start", "tutorial"]:
            print("\n" * 69 + f"What would you like to do? (Enter '>', '<', 'start', or 'tutorial' (next & previous episode, respectively))\nSelected episode: [{episode}]\n")
            temp = input("> ").strip()

        if temp.lower() == "start":
            break
        
        elif temp.lower() == ">":
            episodeChoice += 1

        elif temp.lower() == "<":
            episodeChoice -= 1

        elif temp.lower() == "tutorial":
            tutorial()

        if episodeChoice < 1:
            episodeChoice = 5
        
        if episodeChoice > 5:
            episodeChoice = 1

        episode = episodes[episodeChoice - 1]

        temp = "23470985h036nb234n5n302457n7g32670v8gn237g34687g04563mn34657gvn3456780345678b90n3456" # kek

    return None

# episode 1: Attempting the Arrest
def ata():
    write("F: Oh no! Eli is robbing the Wankopolis bank!")
    write("F (thinking): What should I do?")

    temp = choice(["get backup", "nothing"], "\n(get backup; nothing)")

    if temp == "nothing":
        print("\n" * 69)

        write("Eli: Mmm, wow, that sweet sweet muney.")
        write("Eli (thinking): That was so easy.")
        write("F (thinking): Why did I do nothing. We just lost like $200k.")
        write("F: *Takes out phone*", 1)
        write("F: Uh, yeah, Eli just stole $200k from the local bank")
        write("Cheif of the Wankopolis Police Force: WHAT!? HOW DID YOU LET HIM DO THAT!?!? YOU'RE FIRED!!!")

        write("F is now fired from the Wankopolis Police Force.", 3)

        fail("Why did you choose to do nothing? Do you even want to play the game? Now you're fired from the police force. You know what? I'm not even gonna allow you to retry.")

    elif temp == "get backup":
        print("\n" * 69)

        write("F: *Pulls out phone*")
        write("F: Hey chief, we need some backup here.")
        write("Chief: Ok, I'll reconnect you to RW. Remember, he's your partner!")
        write("RW: Uh, yeah? What is it?", 1)
        write("F: Eli is robbing the bank!", 1)
        write("F: Please come over and bring, uh, everything, just in case.", 2)
        write("RW: Uhh, ok then...", 2)

        write("A few minutes pass and RW comes over with a police car and a bunch of stuff.")
        write("However, the car makes too much noise, and Eli hears it.")

        write("Eli: Oh no, oh no, oh no!")
        write("Eli (thinking): Gotta get out of here!")

        write("Eli gets into his car, and tries to drive away.")
        write("F said to bring everything, so RW did.")
        write("He brought one nail and a grenade that explodes anything that is lands when thrown forcefully.")
        write("He also has some other stuff.")
        write("You have three options.")

        temp = choice(["nail", "grenade", "car"], "\n(nail; grenade; car)")

        if temp == "nail":
            print("\n" * 69)

            write("F tries to throw the one nail at Eli's car's tire, hoping the nail would puncture the tire.")
            write("But, F ends up missing.")
            write("Since he missed, he gets away.")

            fail("So, you had one nail. Correct? Its purpose was to hit the tire and puncture it. Am I right? And you missed it. That's kinda sad.")

        elif temp == "car":
            print("\n" * 69)

            write("The car pulls up, and you both get in, with RW driving.")
            write("It takes F so long and he is having trouble with the seatbelt.")
            write("You end up losing track of Eli's car because you couldn't see and RW thought you were watching.", 3)

            fail("Ok, this one isn't really your fault, this is more of RW's fault. He should've been looking. Either way, Eli is now gone and you can't find him.")


def ltf():
    pass


def dtb():
    pass


def ftv():
    pass


def ctj():
    pass


startMenu()
print("\n" * 69)

match episodeChoice:
    case 1:
        ata()
    case 2:
        ltf()
    case 3:
        dtb()
    case 4:
        ftv()
    case 5:
        ctj()
    case _:
        print("AYOO!??!?!??!?")
