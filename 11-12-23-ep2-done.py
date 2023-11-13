import time
import sys

# variables
episodeChoice = 1 # which episode is selected, and this will be used throughout the code
episodes = ["Season 1, Episode 1: Attempting the Arrest", "Season 1, Episode 2: Locating the Fortress", "Season 1, Episode 3: Defending the Base", "Season 1, Episode 4: Fleeing the Vault", "Season 1, Episode 5: Completing the Job", "Season 2, Episode 1: idk"] # just for episode names
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
    time.sleep(1/8)
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
    print(flavorText, end="\n\n")

    if allowRestart:
        choiceText = "What do you want to do? (retry; main menu; ragequit)"
        retryOption = "retry"
    else:
        choiceText = "What do you want to do? (main menu; ragequit)"
        retryOption = "TWpWaU5uazNPRGt6TWpSaUTWpWaU5uazNPRGt6TWpSaU5XaHVPV0l3TnpJek5HSTFOamx1TnpBM2R6TTBZalU1TURkM00ySTJNRGs0ZDJWaU5EVjBhRzg1Ym5WM1ltVnlkSGs92002972n3650m7892h365m89023650987234560897w3456089h7.-,/./-,=/.-=/.=-][./[]/\.;[]\;././]\[;/;./;.5XaHVPV0l3TnpJek5HTWpWaU5uazNPRGt6TWpSaU5XaHVPV0l3TnpJek5HSTFOamx1TnpBM2R6TTWpWaU5uazNPRGt6TWpSaU5XaHVPV0l3TnpJek5HSTFOamx1TnpBM2R6TTBZalU1TURkM00ySTJNRGs0ZDJWaU5EVjBhRzg1Ym5WM1ltVnlkSGs9TBZalU1TURkM00ySTJNRGs0ZDJWaU5EVjBhRzg1Ym5WM1ltVnlkSGs9STFOamx1TnpBM2R6TTBZalU1TURkM00ySTJNRGs0ZDJWaU5EVjBhRzg1Ym5WM1ltVnlkSGs9"

    temp = choice(["ragequit", retryOption, "main menu"], choiceText)
    if temp == "retry" and allowRestart:
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
    
def typeTimer(time=1.5):
    return
    
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
                
                write("\nRANK ACHIEVED: Beginner Asian Dad")
                
                write("What do you want to do? (restart episode; main menu; quit)")
                win() # beginner asian dad


def ltf():
    print("\n" * 69)
    
    write("The Failure Force (F and RW) are outside of their house, eating sandwhiches and sitting outside their house. Next to their house, there is a sign that says \"Welcome to the Middle of Nowhere!\"")
    write("F (to RW): We to to find the Fortress of Arses if we want to have a singular chance at serving justice.")
    write("The two go inside their house.")
    write("RW: Hey, wait! I know a map that leads to the fortress!")
    write("RW: It's located inside a vault guarded by the Arses!")
    write("F: Alright then, let's break in!")
    write("F and RW both get into the car and drive off toward the vault in the jungle.")
    
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
            print("\n" * 69)
            
            write("The duo walk around to the back without any of the guards seeing them.", 2)
            write("F: Shoot, how do we get in?\n")
            
            temp = choice(["knife", "mega drill", "open the door"], "What do you want to do? (knife; mega drill; open the door)")
            
            if temp == "knife": # Fail
                print("\n" * 69)
                
                write("F equis a knife to try and dig through the door.")
                write("F: Ugh, *intense effort noises and grunts*")
                write("F: Finally! Got it!--", 0.5)
                write("F: OWWWWWWWWW", 2)
                write("RW: Did you really just stab yourself?", 2)
                
                fail("Probably should've thought that through.")
                
            elif temp == "mega drill":
                print("\n" * 69)
                
                write("F: Alright, here's a mega drill that I have.")
                write("F: I just have to hold on to it...", 2)
                write("\n...\n")
                write("F: WAHHHH!!", 2)
                write("RW (thinking): Damn.", 2)
                
                fail("Refrence?")
                
            elif temp == "open the door":
                print("\n" * 69)
                
                write("F opens the door and they both go in.")
                write("F: Alright, let's get to the vault room.")
                write("F: That's where the map is, right?")
                write("RW: Mhm.", 0.75)
                write("F (whispering): We have to get past the main hub.", 2)
                write("F (whispering): Right... CA and EI are there.", 2)
                write("F: How should I defeat them?\n")
                
                temp = choice(["grenade throw", "super bomb", "laser blaster"], "What do you want to use to defeat the guards? (grenade throw; super bomb; laser blaster)")
                
                if temp == "grenade throw": # fail
                    print("\n * 69")
                    
                    write("F throws a grenade into the main hub.")
                    write("However, it bounces against the wall back to where he is.", 2.5)
                    
                    fail("...")
                    
                elif temp == "super bomb": # fail
                    print("\n * 69")
                    
                    write("F throws a super bomb into the main hub.")
                    write("F: Alright, it should explode in 3 seconds...", 3)
                    write("BOOM!")
                    write("The bomb was way to super and blew up F and RW in the process.", 2)
                    
                    fail("Really should've nerfed the bomb.")
                
                elif temp == "laser blaster":
                    print("\n" * 69)
                    
                    write("F equips a laser gun and quickly blastes the two guards.", 2)
                    write("They go to the map room straight afterwards.", 2)
                    write("F: Alright! I got the map!")
                    write("However, their excitment was short-lived.", 0.5)
                    write("Oscar (holding taser): STOP RIGHT THERE!", 0.5)
                    write("F manages to kick Oscar before he tases him.")
                    
                    write("RW: Nice! Now how do we get out?\n")
                    
                    temp = choice(["cheese", "rocket"], "How should F and RW get out? (rocket; cheese)")
                    
                    if temp == "cheese": # Fail
                        print("\n" * 69)
                        
                        write("F and RW eat cheese.", 3)
                        
                        fail("Really? I'm literally confused on why you chose this. Were you expecting this to actually do something?")

                    elif temp == "rocket":
                        print("\n" * 69)

                        write("RW blasts the wall out and they escape.", 2)

                        write("\nRANK ACHIEVED: Beginner Gadget Abuser", 2)

                        write("What would you like to do? (restart episode; main menu; quit)", 0)
                        win() # beginner gadget abuser
        
        elif temp == "tunnel under": # Path 2AB
            print("\n" * 69)

            write("RW: Here's this drill you can use to go under.")
            write("F: Alright, thanks, now time to power this up!")

            write("The guards then realize that F and RW are there, and the radar starts beeping.")

            write("JB starts yelling at F to get out,", 1)
            write("and JI pulls out a shovel.")

            write("RW: Uhh, so, what should I use? I have a long-ranged taser and a sniper rifle.\n")

            temp = choice(["taser", "sniper"], "What should RW equip? (taser; sniper)")

            if temp == "sniper": # fail
                print("\n" * 69)

                write("RW pulls out his sniper rifle.")
                write("He shoots JB, but then JI shoots F when that happens.", 2.5)

                fail("This one's kinda fair, and at the same time not.")

            if temp == "taser":
                print("\n" * 69)

                write("RW uses his taser and shoots JB with it.")
                write("Somehow, JI also gets shocked in the crossfire and they both lie unconscious.", 2)

                write("F continues drilling and then he gets directly to the map room.", 2)

                write("But, CA, OW, and EI all notice F and threaten to shoot him if he doesn't drop the map.\n")

                temp = choice(["spear", "karate", "pause button"], "What should F use? (spear; karate; pause button)")

                if temp == "spear": # fail
                    print("\n" * 69)

                    write("F spears OW but then EI shoots him.", 2)

                    fail("Should've thought of that.")

                elif temp == "karate": # fail
                    print("\n" * 69)

                    write('F yells out "HIYAAH!" but then immediatly gets shot.', 2)

                    fail("I don't think you really had to do that. I meant the \"HIYAAH!\" part.") # Im a doulbe quote user, don't mind my inconsistency

                elif temp == "pause button":
                    print("\n" * 69)

                    write("F takes out the pause button and presses it.")
                    write("Time gets paused for 1 minute for everyone, except F and RW.")
                    write("F takes out the belt and attaches it to a lowering device.")
                    write("He then sets the device to lower in 1 minute.")

                    write("Then, F and RW decide to make a getaway while you still can.")
                    write("They get back to RW's car and drive away as you hear some whipping noises.", 2)

                    write("\nRANK ACHIEVED: Amateur Asian Dad", 2)

                    write("What would you like to do? (restart episode; main menu; quit)", 0)
                    win() # amateur asian dad


        elif temp == "walk straight through": # Fail
            print("\n" * 69)
        
            write("F walks right through the door,", 1)
            write("the guards see him,", 1)
            write("RW thinks F is an idiot,", 1)
            write("and F gets shot.", 3)
            
            fail("You really shouldn't have picked this option. Did you really expect it to work?")
    
    elif temp == "bust in": # Path 2B
        print("\n" * 69)
        
        write("RW: So, here's a scooter that I modified in my mom's garage when I was 7.")
        write("F: And why are you giving that to me?")
        write("RW: Oh, I made it to be super.")
        write("F: Ooh!", 1)
        write("It has buttons to control all the car's weapons.")
        write("F: Nice!", 2)

        write("F (to himself): Alright, let's do this!")
        write("F charges through, knocking both JB and JI out, as well as breaking down the door.")

        write("On the other side, EI and CA are both pointing guns at F.\n")

        temp = choice(["shield", "laser"], "What should F use? He has a super shield and a super laser. (shield; laser)")
        
        if temp == "laser": # fail
            print("\n" * 69)

            write("F shoots CA with the laser.")
            write("But, EI is still alive and shoots F.", 2)

            fail("Always plan ahead.")

        elif temp == "shield":
            print("\n" * 69)

            write("F holds up his shield.", 1)
            write("CA and EI both try to shoot him.", 1)
            write("Lucky for F, both bullets bounce back, killing both guards.", 2)

            write("F: Alright! I'm in the main control room!")
            write("F (thinking): Now what should I do?")
            write("He sees three buttons that he can press.")
            write("The first says \"Self Destruct\", the second \"Eject Chair\", and the final says \"Open All Doors\".\n")

            temp = choice(["self destruct", "eject chair", "open all doors"], "Which button should F press? (self destruct; eject chair; open all doors)")

            if temp == "self destruct": # fail
                print("\n" * 69)
                
                write("F presses the self destruct button.")
                write("It explodes the whole vault,", 1)
                write("including F and RW.", 2)

                fail("That was way too powerful.")

            elif temp == "eject chair": # fail
                print("\n" * 69)
                
                write("F presses the eject chair button.")
                write("The chair ejects him and he smashes into the ceiling.", 2)

                fail("Did you really think this would make F a large boulder so he can fly right through the ceiling?")
            
            elif temp == "open all doors":
                print("\n" * 69)
                
                write("F presses the open all doors button.")

                write("It opens all the doors in the vault.")

                write("F gets onto his scooter,", 1)
                write("zooms through the map room's main door,", 1)
                write("steals the map,", 1)
                write("exits through the peripheral map room,", 1)
                write("and comes face to face with OW, who is pointing a gun at F.", 2)

                write("F manages to dodge his bullets and get him onto the floor, where he is temporarily disabled.\n")

                temp = choice(["gun left", "gun right"], "How should F get rid of OW? (gun left; gun right)")

                if temp == "gun left": # fail
                    print("\n" * 69)

                    write("F shoots the wall and then OW shoots him.", 2)

                    fail("Yeah, I thought so too. This definetly wasn't fair.")

                elif temp == "gun right":
                    print("\n" * 69)
                    
                    write("F shoots OW.", 2)

                    write("F gets back onto his scooter, and then zooms through the back door.")
                    write("He realizes that he has to loop around a road to get to RW's car.")

                    write("However, JB and JI are both in a car (concious again) and are chasing you down the road.\n")

                    temp = choice(["trick", "missile", "fight"], "What do you do? (trick; missile; fight)")

                    if temp == "missile": # fail
                        print("\n" * 69)

                        write("F (over the radio): RW, can you send a missile to JB's car? Thanks in advance. *chuckles*")
                        write("RW: Alright.")
                        write("He sends a missile, but it takes too long for it to get there and F gets shot before it lands.", 2)

                        fail("Pretty unlucky, am I right? I don't know.")

                    elif temp == "fight": # fail
                        print("\n" * 69)

                        write("F stops the scooter to fistfight JB and JI but then he gets run over.", 2)

                        fail("That's really stupid if you tell me.")

                    elif temp == "trick":
                        print("\n" * 69)

                        write("F rides his scooter into the tree forest nearby and JB follows.")
                        write("For that exact reason, JB crashes her car.")

                        write("F continues along the path to RW's car,", 1)
                        write("with the map in possession.")

                        write("\nRANK ACHIEVED: Aggresive Scooter Rider", 2)
                
                        write("What do you want to do? (restart episode; main menu; quit)")
                        win() # aggresive scooter rider

    
def dtb():
    pass


def ftv():
    pass


def ctj():
    pass


# choose episode
def startMenu():
    global episodeChoice, episodes, episode

    episode = episodes[episodeChoice - 1]

    episodeChoice = 1
    temp = "WOLOLOLO"
    while temp.lower() != "start":
        while temp.lower() not in [">", "<", "start", "tutorial", "quit"]:
            print("\n" * 69 + f"What would you like to do? (Enter '>', '<', 'start', 'tutorial', or 'quit' (next & previous episode, respectively))\n\nSelected episode: [{episode}]\n")
            temp = input("> ").strip()

        if temp.lower() == "start":
            break
        
        elif temp.lower() == ">":
            episodeChoice += 1

        elif temp.lower() == "<":
            episodeChoice -= 1

        elif temp.lower() == "tutorial":
            tutorial()

        elif temp.lower() == "quit":
            sys.exit()

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
