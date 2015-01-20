def is_numeric(num):
	return type(num)==int or type(num)

apple = "apple"
print is_numeric(0.5)
print is_numeric(5)
print is_numeric("5")
print is_numeric(apple[0])
