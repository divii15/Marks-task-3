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