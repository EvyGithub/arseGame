import time
from datetime import datetime
import random

# variables
episodeChoice = 1 # which episode is selected, and this will be used throughout the code
episodes = [f"Season 1, Episode 1: Attempting the Arrest", f"Season 1, Episode 2: Locating the Fortress", f"Season 1, Episode 3: Defending the Base", f"Season 1, Episode 4: Fleeing the Vault", f"Season 1, Episode 5: Completing the Job", "Season 2, Episode 1: idk"] # just for episode names
episode = episodes[0] # for display only
FAIL = f"""
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

RANK = """
           _____             _
          |  __ \           | |     _
  ______  | |__) |__ _ _ __ | | __ (_)  ______
 |______| |  _  // _` | '_ \| |/ /     |______|
          | | \ \ (_| | | | |   <   _
          |_|  \_\__,_|_| |_|_|\_\ (_)
"""

# functions
def write(text="Huh?", hold=1, interval=1/42) -> None:
	print("\n" * 69)
	text += " " # so the cursor doesn't look stupid (idk I like the space)

	for letter in text:
		print(letter, end="", flush=True)
		time.sleep(interval/999)

	time.sleep(hold/999)
	print("\n" * 69)

def dotdotdot(hold=2) -> None:
	print("\n" * 69 + "...", end=" ", flush=True)
	time.sleep(hold)

def choice(validOptions, prompt="") -> str:
	temp = "honestly this string is a very nice placeholder that I spent a long time writing for absolutely no reason at all" # lol idk I like to have fun with placeholder variables
	print(prompt)
	while temp not in validOptions:
		try:
			temp = input("> ").strip().lower()
		except EOFError:
			continue

	print("\n" * 69)

	return temp

def fail(flavorText="You failed!", allowRestart=True) -> None:
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
		match episodeChoice:
			case 1: ata()
			case 2: ltf()
			case 3: dtb()
			case 4: ftv()
			case 5: ctj()

	elif temp == "main menu":
		startMenu()

	elif temp == "ragequit":
		print("\n" * 69)
		exit() # my dumbass self would to raise an exception to crash it or something
	
	else:
		temp = "3b6n3698nboin4ybon8b"

def win(rank="What? Idk what the rank is.") -> None:
	global RANK

	print(RANK)
	time.sleep(1)
	print(rank)
	time.sleep(2)

	print() # just one blank line

	temp = choice(["quit", "restart", "main menu"], "What do you want to do? (restart; main menu; quit)")
	if temp == "restart":
		match episodeChoice:
			case 1: ata()
			case 2: ltf()
			case 3: dtb()
			case 4: ftv()
			case 5: ctj()

	elif temp == "main menu":
		startMenu()

	elif temp == "quit":
		print("\n" * 69)
		exit()

def tutorial() -> None:
	print("\n" * 69 + TUTORIAL)
	time.sleep(1)
	write("Welcome to Wankopolis!")
	write("This the luxury destination for stick figures!")
	write("I heard you wanted to be a police officer here, right?")
	write("Here's the police station!")
	write("I'll have you introducted to the Chief.")
	write("Chief: Welcome to the Wankopolis police force!", 1.5)
	write("Chief: Everyone! Welcome our new recruit, F!", 1.5)
	write("(You are playing as F.)", 1.5)
	write("Chief: Your goal is to prevent Eli and his goons from carrying out his evil plans.", 2)
	write("Chief: You really look like you need a buddy...", 2)
	write("Chief: Hey, RW! Come over here! Meet your new partner!", 1.5)
	write("RW: Oh, hi there! How's your day?", 1.5)
	write("F: Hi! My day's going great, and I just got here! *chuckles*", 1.5)
	write("RW: I'm excited to be your new partner!", 1.5)
	write("F: I am too!", 1.5)
	
	choice(["done"], "Type \"done\" when you're done.")
	
# episode 1: Attempting the Arrest
def ata() -> None:
	print("\n" * 69)
	write("F: Oh no! Eli is robbing the Wankopolis bank!")
	write("F (thinking): What should I do?")

	temp = choice(["get backup", "nothing"], "\n(get backup; nothing)")

	if temp == "nothing":
		write("Eli: Mmm, wow, that sweet sweet muney.")
		write("Eli (thinking): That was so easy.")
		write("F (thinking): Why did I do nothing. We just lost like $200k.")
		write("F: *Takes out phone*", 1)
		write("F (in guilt): Uh, yeah, Eli just stole $200k from the local bank...")
		write("Cheif of the Wankopolis Police Force: WHAT!? HOW DID YOU LET HIM DO THAT!?!? YOU'RE FIRED!!!")

		write("F is now fired from the Wankopolis Police Force.", 2)

		fail("Why did you choose to do nothing? Do you even want to play the game? Now you're fired from the police force! You know what? I'm not even gonna allow you to retry.", False)

	elif temp == "get backup":
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
		write("He brought one nail and a grenade which explodes anything lands on when thrown forcefully.")
		write("He also has some other stuff.")
		write("You have three options.")

		temp = choice(["nail", "grenade", "car"], "\n(nail; grenade; car)")

		if temp == "nail":
			write("F tries to throw the one nail at Eli's car's tire, hoping the nail would puncture the tire.")
			write("But, F ends up missing.")
			write("Since he missed, he gets away.")

			fail("So, you had one nail. Correct? Its purpose was to hit the tire and puncture it. Am I right? And you missed it. That's kinda sad.")

		elif temp == "car":
			write("The car pulls up, and the duo both get in, with RW driving.")
			write("It takes F so long and he is having trouble with the seatbelt.")
			write("F ended up losing track of Eli's car because he couldn't see and RW thought F was watching.", 3)

			fail("Ok, this one isn't really your fault, this is more of RW's fault. He should've been looking. Either way, Eli is now gone and you can't find him.")

		elif temp == "grenade":
			write("RW gives F the grenade while Eli is desperatly trying to get into the car and escape.", 2)
			write("F throw the grenade at Eli's car.")
			write("Eli's car explodes into flames.")
			write("F and RW try to chase after him, but Eli has some backup.", 2)
			write("Eli: ITC!! HELP ME!! SPRAY SMOKE OR SOMETHING!!!")
			write("ITC comes over with his helicopter and sprays smoke on the two.", 2)
			dotdotdot(2)
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
				
				print("\n" * 69 + "What do you want to do? (restart episode; main menu; quit)")
				win("Beginner Asian Dad") # beginner asian dad


def ltf() -> None:
	write("The Failure Force (F and RW) are outside of their house, eating sandwhiches and sitting outside their house. Next to their house, there is a sign saying \"Welcome to the Middle of Nowhere!\"")
	write("F (to RW): We to to find the Fortress of Arses if we want to have a singular chance at serving justice.")
	write("The two go inside their house.")
	write("RW: Hey, wait! I know a map which leads to the fortress!")
	write("RW: It's located inside a vault guarded by the Arses!")
	write("F: Alright then, let's break in!")
	write("F and RW both get into the car and drive off toward the vault in the jungle.")
	
	dotdotdot(1.5)
	
	write("F and RW approach the vault and they see JB and JI are guarding the entrance.", 2)
	write("RW: Yo, how do we get in?")
	
	temp = choice(["bust in", "sneak in"], "\nWhat's your method of getting in? (bust in; sneak in)")
	
	if temp == "sneak in": # Path 2A
		write("F and RW decide to sneak in together.")
		write("RW equips a radar which will make beeping sounds if a guard gets suspicious.")
		write("F (whispering to RW): Ok, which way should we go?")
		
		temp = choice(["around the back", "tunnel under", "walk straight through"], "\nHow would you like to sneak in? (around the back; tunnel under; walk straight through)")
		
		if temp == "around the back": # Path 2AA
			write("The duo walk around to the back without any of the guards seeing them.", 2)
			write("F: Shoot, how do we get in?")
			
			temp = choice(["knife", "mega drill", "open the door"], "What do you want to do? (knife; mega drill; open the door)")
			
			if temp == "knife": # Fail
				write("F equis a knife to try and dig through the door.")
				write("F: Ugh, *intense effort noises and grunts*")
				write("F: Finally! Got it!--", 0.5)
				write("F: AAAAAAAAAHHHHH!!!", 2)
				write("RW: Did you really just stab yourself?", 2)
				
				fail("Probably should've thought that through.")
				
			elif temp == "mega drill":
				write("F: Alright, here's a mega drill I have.")
				write("F: I just have to hold on to it...", 2)
				write("\n...\n")
				write("F: WAHHHH!!", 2)
				write("RW (thinking): Damn.", 2)
				
				fail("Refrence?")
				
			elif temp == "open the door":
				write("F opens the door and they both go in.")
				write("F: Alright, let's get to the vault room.")
				write("F: That's where the map is, right?")
				write("RW: Mhm.", 0.75)
				write("F (whispering): We have to get past the main hub.", 2)
				write("F (whispering): Right... CA and EI are there.", 2)
				write("F: How should I defeat them?")
				
				temp = choice(["grenade throw", "super bomb", "laser blaster"], "What do you want to use to defeat the guards? (grenade throw; super bomb; laser blaster)")
				
				if temp == "grenade throw": # fail
					write("F throws a grenade into the main hub.")
					write("However, it bounces against the wall back to where he is.", 2.5)
					
					fail("...")
					
				elif temp == "super bomb": # fail
					write("F throws a super bomb into the main hub.")
					write("F: Alright, it should explode in 3 seconds...", 3)
					write("BOOM!")
					write("The bomb was way to super and blew up F and RW in the process.", 2)
					
					fail("Really should've nerfed the bomb.")
				
				elif temp == "laser blaster":
					write("F equips a laser gun and quickly blastes the two guards.", 2)
					write("They go to the map room straight afterwards.", 2)
					write("F: Alright! I got the map!")
					write("However, their excitment was short-lived.", 0.5)
					write("Oscar (holding taser): STOP RIGHT THERE!", 0.5)
					write("F manages to kick Oscar before he tases him.")
					
					write("RW: Nice! Now how do we get out?\n")
					
					temp = choice(["cheese", "rocket"], "How should F and RW get out? (rocket; cheese)")
					
					if temp == "cheese": # Fail
						write("F and RW eat cheese.", 3)
						
						fail("Really? I'm literally confused on why you chose this. Were you expecting this to actually do something?")

					elif temp == "rocket":
						write("RW blasts the wall out and they escape.", 2)

						write("\nRANK ACHIEVED: Beginner Gadget Abuser", 2)

						print("\n" * 69 + "What would you like to do? (restart episode; main menu; quit)")
						win() # beginner gadget abuser
		
		elif temp == "tunnel under": # Path 2AB
			write("RW: Here's this drill you can use to go under.")
			write("F: Alright, thanks, now time to power this up!")

			write("The guards then realize F and RW are there, and the radar starts beeping.")

			write("JB starts yelling at F to get out,", 1)
			write("and JI pulls out a shovel.")

			write("RW: Uhh, so, what should I use? I have a long-ranged taser and a sniper rifle.\n")

			temp = choice(["taser", "sniper"], "What should RW equip? (taser; sniper)")

			if temp == "sniper": # fail
				write("RW pulls out his sniper rifle.")
				write("He shoots JB, but then JI shoots F when that happens.", 2.5)

				fail("This one's kinda fair, and at the same time not.")

			if temp == "taser":
				write("RW uses his taser and shoots JB with it.")
				write("Somehow, JI also gets shocked in the crossfire and they both lie unconscious.", 2)

				write("F continues drilling and then he gets directly to the map room.", 2)

				write("But, CA, OW, and EI all notice F and threaten to shoot him if he doesn't drop the map.\n")

				temp = choice(["spear", "karate", "pause button"], "What should F use? (spear; karate; pause button)")

				if temp == "spear": # fail
					write("F spears OW but then EI shoots him.", 2)

					fail("Should've thought of that.")

				elif temp == "karate": # fail
					write('F yells out "HIYAAH!" but then immediatly gets shot.', 2)

					fail("I don't think you really had to do that. I meant the \"HIYAAH!\" part.") # Im a doulbe quote user, don't mind my inconsistency

				elif temp == "pause button":
					write("F takes out the pause button and presses it.")
					write("Time gets paused for 1 minute for everyone, except F and RW.")
					write("F takes out the belt and attaches it to a lowering device.")
					write("He then sets the device to lower in 1 minute.")

					write("Then, F and RW decide to make a getaway while you still can.")
					write("They get back to RW's car and drive away as you hear some whipping noises.", 2)

					write("\nRANK ACHIEVED: Amateur Asian Dad", 2)

					print("\n" * 69 + "What would you like to do? (restart episode; main menu; quit)")
					win() # amateur asian dad


		elif temp == "walk straight through": # Fail
			write("F walks right through the door,", 1)
			write("the guards see him,", 1)
			write("RW thinks F is an idiot,", 1)
			write("and F gets shot.", 2.5)
			
			fail("You really shouldn't have picked this option. Did you really expect it to work?")
	
	elif temp == "bust in": # Path 2B
		write("RW: So, here's a scooter I modified in my mom's garage when I was 7.")
		write("F: And why are you giving it to me?")
		write("RW: Oh, I made it to be super.")
		write("F: Ooh!", 1)
		write("RW: It has buttons to control all the car's weapons.")
		write("F: Nice!", 2)

		write("F (to himself): Alright, let's do this!")
		write("F charges through, knocking both JB and JI out, as well as breaking down the door.")

		write("On the other side, EI and CA are both pointing guns at F.\n")

		temp = choice(["shield", "laser"], "What should F use? He has a super shield and a super laser. (shield; laser)")
		
		if temp == "laser": # fail
			write("F shoots CA with the laser.")
			write("But, EI is still alive and shoots F.", 2)

			fail("Always plan ahead.")

		elif temp == "shield":
			write("F holds up his shield.", 1)
			write("CA and EI both try to shoot him.", 1)
			write("Lucky for F, both bullets bounce back, killing both guards.", 2)

			write("F: Alright! I'm in the main control room!")
			write("F (thinking): Now what should I do?")
			write("He sees three buttons he can press.")
			write("The first says \"Self Destruct\", the second \"Eject Chair\", and the final says \"Open All Doors\".\n")

			temp = choice(["self destruct", "eject chair", "open all doors"], "Which button should F press? (self destruct; eject chair; open all doors)")

			if temp == "self destruct": # fail
				write("F presses the self destruct button.")
				write("It explodes the whole vault,", 1)
				write("including F and RW.", 2)

				fail("That was way too powerful.")

			elif temp == "eject chair": # fail
				write("F presses the eject chair button.")
				write("The chair ejects him and he smashes into the ceiling.", 2)

				fail("Did you really think this would make F a large boulder so he can fly right through the ceiling?")
			
			elif temp == "open all doors":
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
					write("F shoots the wall and then OW shoots him.", 2)

					fail("Yeah, I thought so too. This definetly wasn't fair.")

				elif temp == "gun right":
					write("F shoots OW.", 2)

					write("F gets back onto his scooter, and then zooms through the back door.")
					write("He realizes he has to loop around a road to get to RW's car.")

					write("However, JB and JI are both in a car (concious again) and are chasing you down the road.\n")

					temp = choice(["trick", "missile", "fight"], "What do you do? (trick; missile; fight)")

					if temp == "missile": # fail
						write("F (over the radio): RW, can you send a missile to JB's car? Thanks in advance. *chuckles*")
						write("RW: Alright.")
						write("He sends a missile, but it takes too long for it to get there and F gets shot before it lands.", 2)

						fail("Pretty unlucky, am I right? I don't know.")

					elif temp == "fight": # fail
						write("F stops the scooter to fistfight JB and JI but then he gets run over.", 2)

						fail("That's really stupid if you tell me.")

					elif temp == "trick":
						write("F rides his scooter into the tree forest nearby and JB follows.")
						write("For that exact reason, JB crashes her car.")

						write("F continues along the path to RW's car,", 1)
						write("with the map in possession.", 2)
				
						win("Aggressive Scooter Rider") # aggresive scooter rider



def dtb() -> None:
	write("F is studying the map he stole from the Arses while outside his house.")
	write("F: Oh, so that's where their base is.")
	write("F: Guess they're called the Arses for a reason.")
	write("F goes into the house to get a sandwich.")
	write("F: Uhm, why are there helicopter noises outside?")
	write("He then notices the words \"thE arseS\" on the side of the helicopter.")
	write("F: Fuuuu--", 2, 1/8)
	
	temp = choice(["fight alone", "sandwich", "robot gang", "gadget box", "rw"], "F: Ok, what should I do? (fight alone; sandwich; robot gang; gadget box; RW)")
	
	if temp == "fight alone": # fail
		write("F gets onto the roof with a gun.")
		write("But, a mini gatling gun appears under the helicopter and shoots him.", 2)

		fail("Eh...?")
	
	elif temp == "sandwich": # fail
		write("F eats a sandwich.", 5)

		fail("What? Why? Seriously, why?")
	
	elif temp == "robot gang": # path 3A
		pass
	
	elif temp == "gadget box": # 3B (started in class for fedex friday 12/1/23)
		write("F: Alright! Time to get my huge box of stuff!")
		write("F decides to bust open his huge box of weird stuff he made lately.")
		write("However, OE is using a gatling gun and bullets are continously zooming through the living room, so F is stuck in the kitchen.")
		write("F: Now, what do I do here...?")
		
		temp = choice(["sandwich", "duplicate sprite", "ender pearl"], "What should F do? (ender pearl; duplicate sprite; sandwich)")
		
		if temp == "sandwich": # fail
			write("F ate SANDWICH!", 1.5, 0)
			write("He is satisfied!", 1.5, 0)
			write("+15 Satisfication!", 1.5, 0)
			write("+10 HP!", 1.5, 0)
			write("+15 Saturation!", 1.5, 0)
			write("+200 EXP!", 1.5, 0)
			write("You are now level 38!", 1.5, 0)
			
			fail("STOP ALREADY!!!")
		
		elif temp == "duplicate sprite": # fail
			print(f'[{datetime.now().strftime("%H:%M:%S")}] [main/INFO]: Duplicated \'Failure\' sprite at {hex(random.randint(286331153, 4294967295))}')
			time.sleep(5/8)
			for _ in range(7):
				print(f'[{datetime.now().strftime("%H:%M:%S")}] [main/INFO]: Duplicated \'Failure\' sprite at {hex(random.randint(286331153, 4294967295))}')
				time.sleep(1/13)
			for _ in range(69):
				print(f'[{datetime.now().strftime("%H:%M:%S")}] [main/INFO]: Duplicated \'Failure\' sprite at {hex(random.randint(286331153, 4294967295))}')
				time.sleep(1/31)
				
			print(f'[{datetime.now().strftime("%H:%M:%S")}] [main/WARN]: \'Failure\' clones are trying to run through the bullets, this may cause issues!')
			time.sleep(1.5)
			print(f'[{datetime.now().strftime("%H:%M:%S")}] [main/FATAL]: All instances of \'Failure\' have been hit by bullets, causing all instances to die!')
			time.sleep(3)

			fail("Minecraft log, anyone?")
		
		elif temp == "ender pearl":
			write("F throws an ender and he lands on the more accesible part of his house.")
			write("OE and his goons don't know F is on the other side of his house.")
			write("F then gets on his roof.")
			write("He has multiple weapons he can use.")
			
			temp = choice(["sniper rifle", "laser blaster", "grenade"], "Which one does he fire? (sniper rifle; laser blaster; grenade)")
			
			if choice == "sniper rifle": # fail
				pass

			if choice == "grenade": # fail
				pass

			if choice == "laser blaster":
				write("F shoots the laser into the helicopter,", 3/4)
				write("but OJ jumps out and sacrifices himself to block the shot.", 1.5)
				write("He has succesfully blocked the shot, however he is now dead.", 2)
				write("ITC goes out of the helicopter to get the corpse.")
				write("However, OE says they need to fire the missiles.")
				write("Five heat-seeking missiles are then fired toward your house.")
				write("One spare helicopter with a piercing laser pulls up to shoot at you too.")

	elif temp == "rw": # 3C
		pass

def ftv() -> None:
	pass

def ctj() -> None: # ok I somehow need to do combine endings
	pass

# choose episode
def startMenu() -> None:
	global episodeChoice, episodes, episode

	episode = episodes[episodeChoice - 1]

	episodeChoice = 1
	temp = "WOLOLOLO"
	while temp.lower() != "start":
		while temp.lower() not in [">", "<", "start", "tutorial", "quit"]:
			print("\n" * 69 + f"What would you like to do? (Enter '>', '<', 'start', 'tutorial', or 'quit' (next & previous episode, respectively))\n\nSelected episode: [{episode}]\n")
			try:
				temp = input("> ").strip()
			except EOFError:
				continue
		
		match temp.lower():
			case ">":
				episodeChoice += 1

			case "<":
				episodeChoice -= 1
			
			case "start":
				break

			case "tutorial":
				tutorial()

			case "quit":
				print("\n" * 69)
				exit()

		if episodeChoice < 1:
			episodeChoice = 5
		
		if episodeChoice > 5:
			episodeChoice = 1

		episode = episodes[episodeChoice - 1]
		
		temp = ".-- - .. ..... -.. -- -. .... ...- -. .-.. .--- .-. .---- .--. --- -.-- ...- -.. ....- -... ..-. .--. -.. --.- .--- -... .. . ..- .--- -.... -.-- .-.. -.. --. . -- ..-. -.. --.- -. .-. .-.. ..- ----- .--- -.-- .-- .-.. .... ... .- .-- .. -.-- .-. -. .-.. .- --.- ----- .--- -.... -.-- -. .-.. -.-. -... .---- .--. -.-- ... -- -..- .--- .-. .-- - -. .-- ...- -.-. .-- .--. --.- -...- -...-"

	match episodeChoice:
		case 1: ata()
		case 2: ltf()
		case 3: dtb()
		case 4: ftv()
		case 5: ctj()

	temp = "23470985h036nb234n5n302457n7g32670v8gn237g34687g04563mn34657gvn3456780345678b90n3456" # kek

# Ok real code
if __name__ == "__main__":
	print("\n" * 69 + "- Welcome to The Arse Game! -\n")
	time.sleep(0)
	startMenu()
	print("\n" * 69)
