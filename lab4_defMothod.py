# -*- coding: utf8 -*-
"""
def BMI(cm, kg):
	cm = round(float(cm/100), 2) #round(a, 2) 將a四捨五入到小數點第2位
	cm = round(float(cm*cm), 2)  #float(x) 將int x 變成 float x
	n = round(float(kg/cm), 2)
	return n
"""
#from decimal import Decimal
# Using Decimal()function can slove float point, too.
import BMI_module

print "Input your height. (cm)"
cm = round(input()+0.00, 2)
print "cm=%s"%cm
print "Input your weight. (kg)"
kg = round(input()+0.00, 2)
print "kg=%s"%kg
n = BMI_module.BMI(cm, kg)
print "%s" %  n
if cm > 0 and kg > 0 :
	print "Your BMI is %s" % n
	if n >= 25 :
		print "FAT guy."
	elif n < 20 :
		print "Thin guy."
	else :
		print "fantastic! you're super model."
else:
	print "Be serious!" 
