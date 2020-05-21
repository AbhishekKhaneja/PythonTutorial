#Problem statement
#read the file and strore all the lines in list
#reverse the list
#write the list back to the file

with open('test', 'r') as reader: # this is a another way to read the file ('test' is the filename and r is used to denote read file)
    content = reader.readlines() # content is in list form like this [abcde,abc,aaaa,bbb,ccc]
    reversed(content)# using reversed method to reverse the list[ccc,abcde,abc,aaaa,bbb]
    with open('test', 'w') as writer: # this is way to write into the file('test' is the filename and w is used to denote write file)
        for line in reversed(content):
            writer.write(line)