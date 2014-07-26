print "How old are you?"

age = input()

if age>= 18:
	print "You're an %s-year-old adult." % age
elif age<18 and age>=0: 
	print "%s-year-old child should Go back to school." % age
else:
	print "Be serious!"
