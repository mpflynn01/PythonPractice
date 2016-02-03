import time
from sys import exit

# all lists
player_inventory = []
items_1 = ["lantern", "pamphlet"]
items_2 = ["book of spells", "bronze key"]
items_3 = []
items_4 = ["silver key"]
items_5 = []
items_6 = []
items_7 = ["gold key"]
items_8 = ["flint and steel"]
items_9 = ["staff"]
items_10 = []
items_11 = []
items_12 = []
items_13 = ["skeleton key"]

def command_list(command):
	print command_list
	
# drop function
# def drop():

	
	
# Dungeon descriptions
	
def dungeon_locked(dungeon_a, dungeon_b, dungeon_c, dungeon_d):
	print "The door is locked."
	
def dungeon_a():
	print """
You descend the staircase.
A glowing ball of blue energy sits at the middle of the dungeon.
"""

	choice == raw_input("> ")
	
	if choice == "u":
		print "Which staircase? n or e?"
		stairs = raw_input("> ")
	else:
		print "Your incoherance has cost you."
		chamber_1()
		
	if stairs == "n":
		chamber_3()
	elif stairs == "e":
		chamber_10()		
	else:
		chamber_1()
	
# Chamber descriptions
	
def chamber_13():
	print """
You are in Chamber 13.
There is nowhere to go North or South.
There is a small window to the East.
"""

	choice = raw_input("> ")
	
	if choice == "n":
		print "There is only a wall."
	elif choice == "e":
		print "You peer out the window and see a vast forest of tall trees with white trunks."
	elif choice == "s":
		print "There is only a wall."
	elif choice == "w":
		chamber_8()	
	elif choice == "look out window" or choice == "look":
		print "You peer out the window and see a vast forest of tall trees with white trunks."
		chamber_13()
	else:
		print "I don't understand that command"
		chamber_13()	
	
def chamber_12():
	print """
You are in Chamber 12.
The West and East walls have doors that are locked.
"""
	choice = raw_input("> ")
	
	if choice == "n":
		print "There is only a wall."
		chamber_12()
	elif choice == "e":
		dungeon_c()
	elif choice == "s":
		chamber_6()
	elif choice == "w":
		dungeon_b()	
	else:
		print "I don't understand that command"
		chamber_12()

def chamber_11():
	print """
You are in Chamber 11.
The air feels thin in here.
The chamber is surrounded by walls except a passage to the West.
"""
	choice = raw_input("> ")
	
	if choice == "n":
		print "There is only a wall."
		chamber_11()
	elif choice == "w":
		print "There is only a wall."
		chamber_11()
	elif choice == "s":
		print "There is only a wall."
		chamber_11()
	elif choice == "e":
		chamber_4()	
	else:
		print "I don't understand that command"
		chamber_11()

def chamber_10():
	print """
You are in Chamber 10.
There are locked doors to the East and West.
"""
	choice = raw_input("> ")
	
	if choice == "n":
		chamber_2()
	elif choice == "e":
		dungeon_d()
	elif choice == "s":
		print "There is only a wall."
	elif choice == "w":
		dungeon_a()	
	else:
		print "I don't understand that command"
		chamber_10()

def chamber_9():
	print """
You are in Chamber 9.
Two levers are in middle positions.
"""
	choice = raw_input("> ")
	
	if choice == "n":
		chamber_8()
	elif choice == "e":
		print "There is only a wall."
	elif choice == "s":
		dungeon_d()
	elif choice == "w":
		chamber_2()
	elif choice == "up up" or "up down" or "down down":
		print "A jolt of electricity runs through your body."
		chamber_4()	
	elif choice == "down up":
		print "A trap door opens below."
		unchosen("Not all levers are good levers.")	
	else:
		print "I don't understand that command"
		chamber_9()
	
def chamber_8():
	print """
You are in Chamber 8.
"""
	choice = raw_input("> ")
	
	if choice == "n":
		chamber_7()
	elif choice == "e":
		chamber_13()
	elif choice == "s":
		chamber_9()
	elif choice == "w":
		chamber_1()
	
	else:
		print "I don't understand that command"
		chamber_8()

def chamber_7():
	print """
You are in Chamber 7.
A key hangs from a string but it is just out of reach.
The door to the North is locked.
"""
	choice = raw_input("> ")
	
	if choice == "n":
		dungeon_c()
	elif choice == "e":
		print "There's just a wall there."
		chamber_7()
	elif choice == "s":
		chamber_8()
	elif choice == "w":
		chamber_6()
	
	else:
		print "I don't understand that command"
		chamber_7()

def chamber_6():
	print """
You are in Chamber 6.
"""
	choice = raw_input("> ")
	
	if choice == "n":
		chamber_12()
	elif choice == "e":
		chamber_7()
	elif choice == "s":
		chamber_5()
	elif choice == "w":
		chamber_1()
	
	else:
		print "I don't understand that command"
		chamber_6()
	
def chamber_5():
	print """
You are in Chamber 5.
You step in a puddle. There is a red button on a table.
There is a door to the North but it is locked.
"""
	choice = raw_input("> ")
	
	if choice == "n":
		dungeon_b()
	elif choice == "e":
		chamber_6()
	elif choice == "s":
		chamber_4()
	elif choice == "w":
		print "There is only a wall that direction."
		chamber_5()
	elif choice == "press button" or "press" or "red button" or "red":
		print "Are you sure"
		red_button = raw_input("> ")
		if red_button == "yes":
			chamber_1()
		elif red_button == "no":
			chamber_5()
		else:
			print "That isn't a thing."
			chamber_5()
			
	else:
		print "I don't understand that command"
		chamber_()
	
def chamber_4():
	print """
You are in Chamber 4.
As you walk in, you kick something on the ground and hear it bounce away.
"""
	choice = raw_input("> ")
	
	if choice == "n":
		chamber_5()
	elif choice == "e":
		chamber_1()
	elif choice == "s":
		chamber_3()
	elif choice == "w":
		chamber_11()
	else:
		print "I don't understand that command"
		chamber_4()
	
def chamber_3():
	print """
You are in Chamber 3.
A chill runs down your spine.
There is a door to the South but it is locked.
"""
	choice = raw_input("> ")
	
	if choice == "n":
		chamber_4()
	elif choice == "e":
		chamber_2()
	elif choice == "s":
		dungeon_a()
	elif choice == "w":
		print "There is only a wall that direction."
		chamber_3()
	else:
		print "I don't understand that command"
		chamber_3()
	
def chamber_2():
	print """
You are in Chamber 2.
You see a book.
You also see a shiny object on the ground.
"""
	choice = raw_input("> ")
	
	if choice == "n":
		chamber_1()
	elif choice == "e":
		chamber_9()
	elif choice == "s":
		chamber_10()
	elif choice == "w":
		chamber_3()
	else:
		print "I don't understand that command"
		chamber_2()
	
def chamber_1():
	print """
You are in Chamber 1.
You see a lantern on a table.
You also see a pamphlet on the ground.
"""
	choice = raw_input("> ")
	
	if choice == "n":
		chamber_6()
	elif choice == "e":
		chamber_8()
	elif choice == "s":
		chamber_2()
	elif choice == "w":
		chamber_4()
	elif choice == "take lantern":
		player_inventory.append("lantern")
		print player_inventory
		chamber_1()
	elif choice == "take pamphlet":
		player_inventory.append("pamphlet")
		print player_inventory
		chamber_1()		
	else:
		print "I don't understand that command"
		chamber_1()

# a function that ends the game quickly when dishonorable actions occur		
def unchosen(why):
	print why, "Goodbye!"
	exit(0)
	
	
def start():
	print "You are dropped into a dark cellar."
	print "There is a glimmer of light above."
	print "A staircase leads toward the light."
	print "Do you climb up?"
	
	choice = raw_input("> ")
	
	if choice == "yes":
		chamber_1()
	elif choice == "no":
		unchosen("You are a coward. The door closes on you and you are trapped in the cellar for eternity.")		
	else:
		"I do not understand."
		start()

def prompt(self):
    #prints the prompt and returns the input
    print "\nWhat do you want to do?"
    action = raw_input("> ")
    return action
    
inventory = []

#introduction to game
print "Welcome to Chambers"
time.sleep(1.5)
print "Type start to begin"
answer = raw_input("> ")
if answer == "start":
	print "Great. Let's go."
else:
	print "That's not how you spell 'start' but we're gonna begin anyway."
print "What's your adventurer's name?"
name = raw_input("> ")
print "Ok %s, let's get going?" % name
time.sleep(1.5)
print "This is an exploration game. All you need to do is enter some basic commands."
time.sleep(3.0)
print "At any time you can bring up the list of basic commands by typing command\nand pressing enter."
time.sleep(4.0)
print "The goal is to collect all four keys to the four dungeons and retrieve the four elemental orbs."
time.sleep(4.0)
print "The final step is to bring the orbs to the tower and save humanity."
time.sleep(4.0)
print "You get three lives and unlimited moves."
time.sleep(3.0)
print "Ok, %s. Let's go." % (name)
time.sleep(2.0)

#inventory menu

command_list = """
Command List
n - go North
e - go East
s - go South
w - go West
d - Go/Climb Down
u - Go/Climb Up
take - Take item
drop - Drop item
inventory - Show items in inventory
vent - Let out some frustration
attack - Attack with chosen weapon
"""
print"Do you want to see a list of commands?"
answer = raw_input("> ")
if answer == "yes":
	print command_list
	start()
else:
	print "Fine...Know-it-all. \n"
	time.sleep(2.0)
	start()
	
