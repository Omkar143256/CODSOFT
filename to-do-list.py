# Python Programming 
# Task 1: Create a to-do list application 

def task():
    tasks = []
    print("----Welcome to task management application----")

    total_tasks = int(input("Enter the number of tasks you want to add: "))
    for i in range(1,total_tasks+1):
        task_name = input(f"Enter task {i} name: ")
        tasks.append(task_name)
    
    print(f"Today's tasks are\n{tasks}")

    while True:
        operation = int(input("Enter 1-add\n2-update\n3-delete\n4-view\n5-exit/stop:"))
        if operation == 1:
            add = input("Enter task you want to add: ")
            tasks.append(add)
            print(f"Task '{add}' has been successfully added.")

        elif operation == 2:
            updated_value = input("Enter the task you want to update: ")
            if updated_value in tasks:
                up=input("Enter new task: ")
                ind=tasks.index(updated_value)
                tasks[ind] = up
                print(f"Updated task {up}")
        
        elif operation == 3:
            delete_value = input("Which task do you want to delete? ")
            if delete_value in tasks:
                ind = tasks.index(delete_value)
                del tasks[ind]
                print(f"Task {delete_value} has been deleted.")

        elif operation == 4:
            print(f"Total tasks are:{tasks}")

        elif operation  == 5:
            print("Closing the Program.....")
            break

        else:
            print("Invalid Input!")
