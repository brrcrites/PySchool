i = 2
j = 1
print "unindented code will always print"
if i == 1:
    print "but this only prints if i is 1"
if i == 2:
    print "and this only prints if i is 2"
    if j == 1:
        print "this prints when i is 2 and j is 1"