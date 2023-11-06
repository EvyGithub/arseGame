import time
import sys

# variables
episodeChoice = 1 # which episode is selected, and this will be used throughout the code
episodes = ["Season 1, Episode 1: Attempting the Arrest", "Season 1, Episode 2: Locating the Fortress", "Season 1, Episode 3: Defending the Base", "Season 1, Episode 4: Fleeing the Vault", "Season 1, Episode 5: Completing the Job", "Season 2, idk"] # just for episode names
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

def fail(flavorText="You failed!", allowRestart=True):
    global FAIL, episodeChoice

    print("\n" * 69)
    print(FAIL)

    temp = choice(["ragequit", "retry", "main menu"], "What do you want to do? (retry; main menu; ragequit)")
    if temp == "retry":
        if episodeChoice == 1:
            ata()
        elif episodeChoice == 2:
            ltf()
        elif episodeChoice == 3:
            dtb()
        elif episodeChoice == 4:
            ftv()
        elif episodeChoice == 5:
            ctj()

    elif temp == "main menu":
        startMenu()

    elif temp == "ragequit":
        sys.exit() # my dumbass self would to raise an exception to crash it or something
    
    else:

        temp = "3b6n3698nboin4ybon8b"
        
def win():
    temp = choice(["quit", "restart episode", "main menu"], "")
    if temp == "restart episode":
        if episodeChoice == 1:
            ata()
        elif episodeChoice == 2:
            ltf()
        elif episodeChoice == 3:
            dtb()
        elif episodeChoice == 4:
            ftv()
        elif episodeChoice == 5:
            ctj()

    elif temp == "main menu":
        startMenu()

    elif temp == "quit":
        sys.exit()
        
    else:

        temp = "sddfwebrq25b235b2345b23456b2345b23456nb234567n3567nj467eruyertnyenrtyenrty"

    print("Type anything to exit.")
    while len(temp) == "sddfwebrq25b235b2345b23456b2345b23456nb234567n3567nj467eruyertnyenrtyenrty":
        temp = input("> ").strip().lower()

    sys.exit()

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

# episode 1: Attempting the Arrest
def ata():
    print("\n" * 69)
    write("F: Oh no! Eli is robbing the Wankopolis bank!")
    write("F (thinking): What should I do?")

    temp = choice(["get backup", "nothing"], "\n(get backup; nothing)")

    if temp == "nothing":
        print("\n" * 69)

        write("Eli: Mmm, wow, that sweet sweet muney.")
        write("Eli (thinking): That was so easy.")
        write("F (thinking): Why did I do nothing. We just lost like $200k.")
        write("F: *Takes out phone*", 1)
        write("F (in guilt): Uh, yeah, Eli just stole $200k from the local bank...")
        write("Cheif of the Wankopolis Police Force: WHAT!? HOW DID YOU LET HIM DO THAT!?!? YOU'RE FIRED!!!")

        write("F is now fired from the Wankopolis Police Force.", 2)

        fail("Why did you choose to do nothing? Do you even want to play the game? Now you're fired from the police force. You know what? I'm not even gonna allow you to retry.", False)

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

            write("The car pulls up, and the duo both get in, with RW driving.")
            write("It takes F so long and he is having trouble with the seatbelt.")
            write("F ended up losing track of Eli's car because he couldn't see and RW thought F was watching.", 3)

            fail("Ok, this one isn't really your fault, this is more of RW's fault. He should've been looking. Either way, Eli is now gone and you can't find him.")

        elif temp == "grenade":
            print("\n" * 69)

            write("RW gives F the grenade while Eli is desperatly trying to get into the car and escape.", 2)
            write("F throw the grenade at Eli's car.")
            write("Eli's car explodes into flames.")
            write("F and RW try to chase after him, but Eli has some backup.", 2)
            write("Eli: ITC!! HELP ME!! SPRAY SMOKE OR SOMETHING!!!")
            write("ITC comes over with his helicopter and sprays smoke on the two.", 2)
            write("...")
            write("F: Ok, what was that?")
            write("F: But more importantly, WHERE DID ELI GO!?!?")
            write("RW: Uh, I don't know.")
            write("RW: But I do have two cat search teams I could call.")
            write("F: Uhm, why?")
            write("RW: Cats are just good at smelling, I guess?")
            write("RW: I don't know which one I should call though.")
            
            temp = choice(["green", "blue"], "Which cat team do you want to call? Green Team - Has knives; Blue Team - Has belts. (green; blue)")
            
            if temp == "green":
                write("F calls the green team.")
                write("However, the green team wasn't properly trained on how to use knives responsibly.")
                write("They end up stabbing each other because they thought their team allies were Eli or his goons.", 3)
                
                fail("Ooh, that must suck. I at least thought the cats would be trained.")
                
            if temp == "blue":
                write("The blue team, with their 3 years of training, try to sniff out Eli's stinky smell.")
                write("They do find him, and take out their belts.")
                
                write("The cats LASH Eli until he's on the floor.")
                write("Eli (in fear): STOP! PLEASE! JUST STOP LASHING ME! (screaming really loudly in pain) AAAAAAAAAAAAAAAAAAAAAA")
                
                # the end of episode 1
                
                write("Rank Achieved: Beginner Asian Dad")
                
                write("What do you want to do? (restart episode; main menu; quit)")
                win()


def ltf():
    print("\n" * 69)
    
    write("The Failure Force (F and RW) are outside of their house, eating sandwhiches and sitting outside their house. Next to their house, there is a sign that says \"Welcome to the Middle of Nowhere!\"", 2)
    write("F (to RW): We to to find the Fortress of Arses if we want to have a singular chance at serving justice.", 2)
    write("The two go inside their house.", 2)
    write("RW: Hey, wait! I know a map that leads to the fortress!")
    write("RW: It's located inside a vault guarded by the Arses!")
    write("F: Alright then, let's break in!")
    write("F and RW both get into the car and drive off toward the vault in the jungle.", 2)
    
    write("\n...\n", 2)
    
    write("F and RW approach the vault and they see that JB and JI are guarding the entrance.", 2)
    write("RW: Yo, how do we get in?")
    
    temp = choice(["bust in", "sneak in"], "\nWhat's your method of getting in? (bust in; sneak in)")
    
    if temp == "sneak in": # Path 2A
        print("\n" * 69)
        
        write("F and RW decide to sneak in together.")
        write("RW equips a radar that will make beeping sounds if a guard gets suspicious.")
        write("F (whispering to RW): Ok, which way should we go?")
        
        temp = choice(["around the back", "tunnel under", "walk straight through"], "\nHow would you like to sneak in? (around the back; tunnel under; walk straight through)")
        
        if temp == "around the back": # Path 2AA
            write("\n" * 69)
            
            write("The duo walk around to the back without any of the guards seeing them.", 2)
            write("F: Shoot, how do we get in?")
            
            temp = choice(["knife", "mega drill", "open the door"], "What do you want to do? (knife; mega drill; open the door)")
            
            if temp == "knife":
                write("\n" * 69)
                
            elif temp == "mega drill":
                write("\n" * 69)
                
            elif temp == "open the door":
                write("\n" * 69)
        
        elif temp == "tunnel under": # Path 2AB
            write("\n" * 69)
        
        elif temp == "walk straight through": # Fail
            print("\n" * 69)
        
            write("F walks right through the door,", 1)
            write("the guards see him,", 1)
            write("RW thinks F is an idiot,", 1)
            write("and F gets shot.", 3)
            
            fail("You really shouldn't have picked this option. Did you really expect it to work?")
    
    elif temp == "bust in": # Path 2B
        write("\n" * 69)
        # insert more

    
def dtb():
    pass


def ftv():
    pass


def ctj():
    pass


# choose episode
def startMenu():
    global episodeChoice, episodes, episode

    episodeChoice = 1
    temp = "WOLOLOLO"
    while temp.lower() != "start":
        while temp.lower() not in [">", "<", "start", "tutorial"]:
            print("\n" * 69 + f"What would you like to do? (Enter '>', '<', 'start', or 'tutorial' (next & previous episode, respectively))\n\nSelected episode: [{episode}]\n")
            temp = input("> ").strip()
            
        print(temp)

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
        
        temp = ".-- - .. ..... -.. -- -. .... ...- -. .-.. .--- .-. .---- .--. --- -.-- ...- -.. ....- -... ..-. .--. -.. --.- .--- -... .. . ..- .--- -.... -.-- .-.. -.. --. . -- ..-. -.. --.- -. .-. .-.. ..- ----- .--- -.-- .-- .-.. .... ... .- .-- .. -.-- .-. -. .-.. .- --.- ----- .--- -.... -.-- -. .-.. -.-. -... .---- .--. -.-- ... -- -..- .--- .-. .-- - -. .-- ...- -.-. .-- .--. --.- -...- -...-"

    if episodeChoice == 1:
        ata()

    elif episodeChoice == 2:
        ltf()

    elif episodeChoice == 3:
        dtb()

    elif episodeChoice == 4:
        ftv()

    elif episodeChoice == 5:
        ctj()

        temp = "23470985h036nb234n5n302457n7g32670v8gn237g34687g04563mn34657gvn3456780345678b90n3456" # kek

    return None


# Ok real code
startMenu() # WHOA WHOA WHOA WHOA WHOA WHOA WHOA
print("\n" * 69)