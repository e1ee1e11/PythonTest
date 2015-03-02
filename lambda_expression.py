garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"
message = filter(lambda x: x ,"".join(garbled.split('X')))
def remove_X(garbled):
	return "".join(garbled.split('X'))

			 
print message
#print remove_X(garbled)
