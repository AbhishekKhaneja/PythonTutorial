str = "Abhishek.Khaneja"
str2 = "@gmail.com"
str3= "Abhishek"

print(str[2])

print(str + str2) # concatenation

print(str[0:5]) # substring

print(str3 in str) # substring check


var = str.split(".") # spliting string with .
print(var)

print(var[0])

str4 = " great "
print(str4.strip()) # strip is the function name which is used to trim the whitespaces like trim function in java
print(str4.lstrip()) # trim the left whitespace
print(str4.rstrip()) # trim the right whitespace