name = 'Matthew Flynn'
age = 27 # accurate for sure
height = 70 # inches
weight = 220 # lbs
eyes = 'Brown'
teeth = 'Shifty'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "He'd like to lose 30 lbs by June!"
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are weird becuase they are a bit %s." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % ( 
age, height, weight, age + height + weight)