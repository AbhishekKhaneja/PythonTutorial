print("Hello")

#   here are the comments i have defined
a = 3
print(a)

b, c = 5.4, "Great"

print("{} {}".format("Value is ", a)) #to concatenate String and Integer

print(type(a))
print(type(b))
print(type(c))


#list
values =[1, 2, "abhishek", 2, 9]
print(values[1])

print(values[-1])

print(values[1:3])


values.insert(3, "Khaneja")
print(values)

values.append("End")
print(values)

values[2]="Abby" #updating

del values[0]
print(values)


#Tuple datatype -Same as LIST data type But immutable which means it can't change once given a value

val = ('a', 10, "jimmy")

print(val)

#val[2]="jemmy" #TypeError: 'tuple' object does not support item assignment

#disctionary Datatype--it is same like hashmap in java (key value pair)
a = {1:"first name",2:"last name", "age":33}

#print value having key=1
print(a[1])
#print value having key=2
print(a[2])
#print value having key="age"
print(a["age"])


dict = {}

dict["FirstName"] = "Abhishek"

dict["lastName"] = "Khaneja"

print(dict)
print(dict["lastName"])
