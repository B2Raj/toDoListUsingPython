def task():
    tasks=[]
    print("(:---->Welcome to Task management app<----:)")
    totalTast=int(input("Enter no of Task you want: "))
    for i in range(1, totalTast+1):
        taskName=input(f"Enter your Task {i}: ")
        tasks.append(taskName)
    print("Note:-Make sure to use same keyword of tasks during operations.")
    print(f"Todays Task are {tasks}")
    
    while True:
        # print("Add.  /nUpdate.    /nDelete.    /nView.    /nExit or Stop.")
        print("Choose Operation to perform on the Tasks.")
        operation=(input("-->Add \n -->Update \n -->Delete \n -->View \n -->Exit \n"))
                   # Add operation 
        if(operation=="add" or operation=="Add"):
            add=input("Enter Task to add: ")
            tasks.append(add)
            print(f"Task{add} has been added to the List.")
                # update operation
        elif(operation=="update" or operation=="Update"):
            previousTask=input("Which Task you want to update: ")
            newTask=input("Enter your new Task: ")
            if (previousTask in tasks): 
                previousIndex=tasks.index(previousTask)
                tasks[previousIndex]=newTask
                print(f"New Task {newTask} has been updated.")
                    # delete operation
        elif(operation=="Delete" or operation=="delete"):
            deletedTask=input("Which Task you want Delete: ")
            if(deletedTask in tasks):
                deleteIndex=tasks.index(deletedTask)
                del tasks[deleteIndex]
                print("Task has been Deleted.")
                # view operation
        elif(operation=="View" or operation=="view"):
            print(f"Total Tasks: {tasks}")      
            # exit operation      
        elif(operation=="Exit" or operation=="exit"):
            print("closing the Program.")
            break
            # for invalid inputs
        else:
            print("------->Invalid input, Enter VALID operations.")
            
task()         