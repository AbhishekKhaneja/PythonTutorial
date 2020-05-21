

name = "Good morning"

if name == "Good":
    print("Condition Matches")

else:
    print("Not matches")

#for loop to iterate in a list
obj =[1, 2, 3, 4, 5]

for i in obj:
    print(i)


#sum of first five natural numbers

add =0
for j in range(1, 6) :# range given will iterate from 1 to 5(why 5 it is always 1 less than the number given)
    add = add + j

print("{} {}".format("Value is ", add))


for k in range(1, 10, 2): # to iterate with 2 it is like (for (int k =0;k=10;k+2))
    print(k)


print("****************skipping first index****************")
for m in range(10): # python will br default treat this as maximun value till the loop will iterate and always starting with 0
    print(m)


