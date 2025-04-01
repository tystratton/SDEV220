#Ty Stratton
#4/1/2025
# Sort 0s, 1s, and 2s
# Given an array, sort the array in ascending order

while True:
    lname = input("What is your last name (enter ZZZ to quit): ")
    if (lname == "ZZZ"):
        break
    fname = input("What is your first name: ")
    gpa = input("What is your GPA: ")
    floatgpa = float(gpa)
    if(floatgpa > 3.5):
        print(f"{fname} {lname} has made the Dean's List")  
    elif(floatgpa > 3.25):
        print(f"{fname} {lname} has made the Honor Roll")
    else:
        print(f"{fname} {lname} did not make the Dean's List or Honor Roll")
