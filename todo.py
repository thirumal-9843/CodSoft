from operations import *
import os

print("Welcome to our task manager!")

while True:
    print("you can perform the following operations:")
    print("1.Add a task\n2.Update a task\n3.Delete a task")
    choice=input("Enter your choice [1,2,3]:")
    if choice in ["1","2","3"]:
        if choice=="1":
            add_task(input("Enter task description:"))
            view_task()
        elif choice=="2":
            try:
                view_task()
                update_task(int(input("Enter task id to be marked done:")))
                view_task()
            except:
                print("Invalid task")
        elif choice=="3":
            try:
                view_task()
                delete_task(int(input("Enter task id to be deleted:")))
                view_task()
            except:
                print("Invalid task id")
    else:
        print("invalid choice")
    
    cont=input("Do you want to continue[y/n]")
    if cont=="y" or cont=="Y":
        os.system("cls||clear")
    else:
        print("Thanks for using the app!\nKeep using!!")
        exit()