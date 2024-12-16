import os
import platform

global listStd  # Making listStd as Super Global Variable
listStd = [
    "yugesh", "kishor", "gajen", "Gopi", "Arjun", "Sita", "Maya", "Ravi", "Amit", "Priya",
    "Neha", "Anjali", "Ramesh", "Shalini", "Vikas", "Suresh", "Pooja", "Asha", "Deepak", "Vandana"
]  # List of 20 Students

def manageStudent():  # Function for the Student Management System
    x = "#" * 30
    y = "=" * 28
    global bye  # Making Bye as Super Global Variable
    bye = "\n {}\n# {} #\n# ===> Brought To You By <===  #\n# ===> code-projects.org <===  #\n# {} #\n {}".format(x, y, y, x)  # Goodbye message

    # Printing Welcome Message and options for this program
    print(""" 

  ------------------------------------------------------
 |======================================================| 
 |======== Welcome To Student Management System ========|
 |======================================================|
  ------------------------------------------------------

Enter 1 : To View Student's List 
Enter 2 : To Add New Student 
Enter 3 : To Search Student 
Enter 4 : To Remove Student 
		
		""")

    try:  # Using Exceptions for Validation
        userInput = int(input("Please Select An Above Option: "))  # Take input from user
    except ValueError:
        exit("\nHy! That's Not A Number")  # Error message
    else:
        print("\n")  # Print new line

    # Checking based on user input
    if(userInput == 1):  # This option will print list of students
        print("List of Students\n")  
        for student in listStd:
            print("=> {}".format(student))

    elif(userInput == 2):  # This option will add new student to the list
        newStd = input("Enter New Student: ")
        if(newStd in listStd):  # Check if the student already exists
            print("\nThis Student {} Already In The Database".format(newStd))  # Error message
        else:    
            listStd.append(newStd)
            print("\n=> New Student {} Successfully Added \n".format(newStd))
            for student in listStd:
                print("=> {}".format(student))  

    elif(userInput == 3):  # This option will search for a student in the list
        srcStd = input("Enter Student Name To Search: ")
        if(srcStd in listStd):  # Searching the student
            print("\n=> Record Found For Student {}".format(srcStd))
        else:
            print("\n=> No Record Found For Student {}".format(srcStd))  # Error message

    elif(userInput == 4):  # This option will remove a student from the list
        rmStd = input("Enter Student Name To Remove: ")
        if(rmStd in listStd):  # Removing the student
            listStd.remove(rmStd)
            print("\n=> Student {} Successfully Deleted \n".format(rmStd))
            for student in listStd:
                print("=> {}".format(student))
        else:
            print("\n=> No Record Found of This Student {}".format(rmStd))  # Error message

    elif(userInput < 1 or userInput > 4):  # Validating user option
        print("Please Enter a Valid Option")  # Error message


def runAgain():  # Function to run the program again
    runAgn = input("\nWant to run again Y/n: ")
    if(runAgn.lower() == 'y'):
        if(platform.system() == "Windows"):  # Check user OS to clear the screen
            os.system('cls') 
        else:
            os.system('clear')
        manageStudent()
        runAgain()
    else:
        quit(bye)  # Print Goodbye message and exit the program

manageStudent()
runAgain()
