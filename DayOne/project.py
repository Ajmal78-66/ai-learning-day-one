print("grade of plus2 commerce students")

student = input("ENTER YOUR NAME PLS : ")

mark = int(input("ENTER YOUR MARK PLS " + student + " : "))


if  mark > 100 or mark < 0:
    print("ENTER A VALID MARK")
elif mark >= 90:
    print("YOUR MARK IS 'A' VERY GOOD " + student)
elif mark >= 75:
    print("YOUR MARK IS 'B' GOOD " + student)
elif mark >= 50:
    print("YOUR MARK IS 'C' NEED MORE TO IMPROVE" + student)
else:
    print(student + "YOU FAILED")


