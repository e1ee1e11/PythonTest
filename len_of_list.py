list0 = []
list1 = [1]
list2 = range(10)
list3 = [["a","b","1"], "456", 7]
list4 = [list0, list1, list2]

print "list0's length is " + str(len(list0))
print "list1's length is " + str(len(list1))
print "list2's length is " + str(len(list2))
print "list3's length is " + str(len(list3))
print "list4's length is " + str(len(list4))
print list4
print " ".join((str(x) for x in list2))
