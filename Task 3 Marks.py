#TASK 3
#6)get the name,rollnumber,tamil, eng, maths mark from user.
#if 3 subject total is greater than 90, output will be First class.
#if 3 subject total is greater than 80, output will be Second class.
#if 3 subject total is greater than 60, output will be third class.
#if 3 subject total is greater  than or equal to 35, output will be Avarage.
#otherwise fail.



name = input("Enter your name:")
roll_number = input("Enter your roll number:")
tamil_marks = int(input("Enter Tamil marks:"))
eng_marks = int(input("Enter English marks:"))
maths_marks = int(input("Enter Maths marks:"))
total = tamil_marks + eng_marks + maths_marks

if (total>90):
    print("Output will be First class")
elif (total>80):
    print("Output will be Second class")
elif (total>60):
    print("Output will be Third class")
elif (total>=35):
    print("Output will be Average")
else:
    print("Output will be Fail")