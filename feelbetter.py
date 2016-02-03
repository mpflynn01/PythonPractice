import time

def name(n):
	print "Hey %s, nice to meet you!" % n
	
print "Don't I know you from somewhere? What's your name again?"
name(raw_input("> "))

time.sleep(1.0)

print "How are you feeling today?"
feeling = raw_input("> ")


if feeling == "good":
	print "I'm glad you're feeling well today."
elif feeling == "bad":
	print "That's ok. Everyone has those days. Let's work it out."
elif feeling == "ok":
	print "Ok is great. Plenty of room to grow."
else:
	print "I don't know that feeling. Can you try a different word?"
	
time.sleep(1.0)
	
print "Did you do anything interesting?"
interesting = raw_input("> ")

if interesting == "yes":
	print "That's awesome! What did you do?"
	raw_input("> ")
elif interesting == "no":
	print "I'm sorry to hear that. But, it's not too late."
else:
	print "I don't know what you mean but you're interesting to me!"
	
if interesting == "yes":
	print "Well, was it fun?"
	answer = raw_input("> ")
if answer == "yes":
	print "Great!"
else:
	print "That fuckin' sucks!"
	
	
	