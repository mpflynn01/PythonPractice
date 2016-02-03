# 1
def light_switch(x, y):
	print "You are wasting money by turning them %s and %s." % (x, y)

print "Hey, what are you doing over there?"
light_switch("on", "off")

# 2
def add(a, b):
	print "Let's practice some functions by adding %d + %d!" % (a, b)
	return a + b

print add(30, 5)

#3
def name(n):
	print "Hey %s, nice to meet you!" % n
	
print "Don't I know you from somewhere? What's your name again?"
print name(raw_input("> "))
	