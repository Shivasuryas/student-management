# Student Management System

A simple **Python-based Student Management System** that allows users to perform operations such as viewing, adding, searching, and removing students from a list. The system also includes the ability to run multiple actions without restarting the script.

## Features

1. **View Student List**: Displays a list of 20 students.
2. **Add New Student**: Allows users to add a new student to the list, ensuring no duplicates.
3. **Search for a Student**: Enables users to search for a student by name.
4. **Remove Student**: Removes a student from the list (if the student exists).
5. **Run Again**: Prompts the user to decide whether they want to run the program again, with the screen being cleared between runs.

## Requirements

- **Python 3.x** or higher.

## How to Run

### Steps:
1. **Clone or download** the project files to your local machine.
2. **Open a terminal** or command prompt on your computer.
3. **Navigate to the folder** where the `student_management_system.py` script is located.
4. **Run the script** by typing the following in the terminal or command prompt:

   ```bash
   python student_management_system.py

5.Follow the on-screen instructions to:

    View the list of students.
    Add a new student to the list.
    Search for a student by name.
    Remove a student from the list.

6.After each action, the program will ask if you want to run it again. Type Y to continue or n to exit.

##Code Overview

    - listStd: A global list containing the initial 20 students.
    - manageStudent(): This is the main function that provides options to the user:
        View the student list.
        Add, search, and remove students from the list.
    - runAgain(): This function allows the user to repeat the process or exit the program, displaying a goodbye message at the end.

Example Interaction

  ------------------------------------------------------
 |======================================================| 
 |======== Welcome To Student Management System ========|
 |======================================================|
  ------------------------------------------------------

Enter 1 : To View Student's List 
Enter 2 : To Add New Student 
Enter 3 : To Search Student 
Enter 4 : To Remove Student

Please Select An Above Option: 1

List of Students
=> yugesh
=> kishor
=> gajen
=> Gopi
=> Arjun
=> Sita
=> Maya
=> Ravi
=> Amit
=> Priya
=> Neha
=> Anjali
=> Ramesh
=> Shalini
=> Vikas
=> Suresh
=> Pooja
=> Asha
=> Deepak
=> Vandana

Want to run again Y/n: y

Key Notes

    - The student list initially contains the names of 20 students.
    - After any action (add, search, or remove), the updated student list is printed for confirmation.
    - The program validates user inputs, ensuring that only valid numbers (1 to 4) are accepted for the main options.
    - If the user tries to add a student that is already in the list, the program will display a message indicating that the student is already present.
    - If the user tries to remove a student who does not exist, an error message will be displayed.

License

This project is open source and available under the MIT License.