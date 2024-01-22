grade = 0

grade = int(input("Enter a grade from 0 to 100: "))

if grade >= 90 and grade <= 100:
    print("Your grade is A")
elif grade < 90 and grade >= 80:
    print("Your grade is B")
elif grade < 80 and grade >= 70:
    print("Your grade is C")
elif grade < 70 and grade >= 60:
    print("Your grade is D")
else:
    print("Your grade is F")

