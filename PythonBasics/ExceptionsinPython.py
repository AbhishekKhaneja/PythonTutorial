
ItemsinCart =  0


# first way to raise an exception explicity

#if ItemsinCart !=2:
#    raise Exception("Items count is not equal to 2")

# another way of throwing and error using assert
#assert(ItemsinCart==2)

#try catch Block-In python instead of catch we use except

try:
    with open('test', 'r') as reader:
        reader.read()
except:
    print("this is a customized exception  by the user")


try:
    with open('test1', 'r') as reader:
        reader.read()
except Exception as e:# if you want to see the actual exception thrown by python use like this
    print(e)
finally:
    print("I will always execute irrespective of any failures/error or without any failure")