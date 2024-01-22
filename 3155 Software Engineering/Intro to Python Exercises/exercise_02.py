string1 = ""
string2 = ""

string1 = input("Enter a string: ")
string2 = input("Enter another string: ")

s1 = string1.lower()
s2 = string2.lower()

if s1.endswith(s2) or s2.endswith(s1):
    print("true")
else:
    print("false")


