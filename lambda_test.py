func = lambda x : x if x<10 else None
list=range(1,20,2)
#print(list)
print(filter(func,list))
