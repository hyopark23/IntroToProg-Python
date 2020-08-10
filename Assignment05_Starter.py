# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# Hyo Park, 08.06.2020, Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = ""  # A Capture the user option selection

print("This program will allow you to read, write, and remove your tasks and priorities.")
# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
objFile = open("ToDoList.txt", "r")
for row in objFile:
    strData = row.split(",")  # put rows from the file into lists
    dicRow = {"Task": strData[0], "Priority": strData[1].strip()}  # create dictionary from strData
    lstTable.append(dicRow)
objFile.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while True:
    print("""
    Menu of Options
    1) Show current tasks
    2) Add a new task
    3) Remove an existing task
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks

    # Step 3 - Show the current items in the table
    if strChoice.strip() == '1':
        print("Your current tasks and priorities are:")
        for row in lstTable:
            print(row["Task"] + "\t|\t" + row["Priority"])
        continue
    # Step 4 - Add a new item to the list/Table
    elif strChoice.strip() == '2':
        print("Please enter a new task and priority.")
        while True:
            strKey = input("To Do Task: ")
            strValue = input("Task Priority: ")
            lstTable.append({"Task": strKey, "Priority": strValue})
            strAdditionalInput = input("More input? Please enter Yes or No: ")
            if strAdditionalInput.lower() == "yes":
                continue
            elif strAdditionalInput.lower() == "no":
                break
        continue
    # Step 5 - Remove a new item from the list/Table
    elif strChoice.strip() == '3':
        numTasks = len(lstTable)        # Get length of the table for no match
        print("Please enter an existing task to remove from the database.")
        print("Your current tasks and priorities are:")
        for row in lstTable:
            print(row["Task"] + "\t|\t" + row["Priority"])
        strTask = input("Task to remove: ")
        for row in lstTable:
            if row["Task"].lower() == strTask.lower():
                lstTable.remove(row)
                print("Task found and removed!")
        if numTasks == len(lstTable):   # If length is same it means no match
            print("Task not found! Please re-check current database.")
        input("\nPress 'Enter' to see the menu. ")
        continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif strChoice.strip() == '4':
        objFile = open("ToDoList.txt", "w")
        for row in lstTable:
            objFile.write(row["Task"] + ", " + row["Priority"] + "\n")
        objFile.close()
        print("Data saved to file!")
        continue
    # Step 7 - Exit program
    elif strChoice.strip() == '5':
        print("Exiting the program.")
        break  # and Exit the program
    # Else statement for non-valid choices
    else:
        print("Please enter 1, 2, 3, 4, or 5.")
