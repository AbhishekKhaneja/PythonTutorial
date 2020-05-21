file = open("test")
#read all the contents of file
#print(file.read())

#read n number of characters by passing parameter
#print(file.read(3))

#read one single line at a time using readline()
#print(file.readline())
#print(file.readline())
#file.close()


#Print line by line using readline method
#line = file.readline()
#while line != "":
#    print(line)
#    line =file.readline()

for line in file.readlines():
    print(line)