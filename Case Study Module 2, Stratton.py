#Ty Stratton
#3/24/25
# Case Study Module 2, Dean's List
# This app asks for a user's name and GPA and determines what list they fit on (Dean's or Honors)

while True:
    lname = input("What is your last name (enter ZZZ to quit): ")
    if (lname == "ZZZ"):
        break
    fname = input("What is your first name: ")
    gpa = input("What is your GPA: ")
    floatgpa = float(gpa)
    if(floatgpa > 3.5):
        print(f"{fname} {lname} has made the Dean's List")  
    elif(gpa > 3.25):
        print(f"{fname} {lname} has made the Honor Roll")
    else:
        print(f"{fname} {lname} did not make the Dean's List or Honor Roll")
