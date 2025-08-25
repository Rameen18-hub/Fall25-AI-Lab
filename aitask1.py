def show_menu():
    print("\n=== TO DO LIST MENU ===")
    print("1. Add Task")
    print("2. View Task")
    print("3. Remove Task")
    print("4. Recorder Task (Prioritize)")
    print("5. Exit")
def add_task(task_list):
    task=input("Enter new task: ")
    task_list.append(task)
    print(f"Task'{task}' added successfully")
 
def view_task(task_list):
    if not task_list:
        print("No tasks in the list.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(task_list ,start=1):
            print(f"{i}. {task}")

def remove_task(task_list):
    view_task(task_list)
    try:
        task_num=int(input("Enter task number to remove:"))
        removed=task_list.pop(task_num-1)
        print(f"Task'{removed}' removed successfully")
    except(ValueError,IndexError):
        print("Invalid task number!")

def recorder_task(task_list):
    view_task(task_list)
    if not task_list:
        return
    
    try:
        print("\nEnter the new order of tasks(space separated indices)")
        print("Example: If you have 4 tasks and want order 2,4,1,3 -> enter: 2 4 1 3 ")
        new_order = list(map(int, input("New order: ").split()))
        if sorted(new_order) != list(range(1,len(task_list)+1)):
            print("Invalid order! Please enter all task numbers correctly.")
            return
        task_list[:] =[task_list[i-1] for i in new_order]
        print("\n Tasks recorded successfully")
        view_task(task_list)

    except Exception as e:
         print("Error in recording",e)

if __name__ =="__main__":
    tasks=[]
    while True:
       show_menu()
       choice=input("Choose an option:")

       if choice=="1":
          add_task(tasks)
       elif choice =="2":
        view_task(tasks)
       elif choice=="3":
        remove_task(tasks)
       elif choice =="4":
        recorder_task(tasks)
       elif choice =="5":
        print("Exiting To-Do List. Goodbye!")
        break
       else:
        print("Invalid choice. Try Again.")
    


