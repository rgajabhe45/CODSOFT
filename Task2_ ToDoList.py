# To Do List program 
my_tasks = []

while True:
  print("\n*** To Do List *** ")
  print("1. Add Task")
  print("2. View Task")
  print("3. Delete Task")
  print("4. Exit")

choice = input("Enter your Choice: ") 
if choice == '1':
  task = input("Enter new task: ")
  task.append(task)
  print("task added!")

elif choice == '2':
  if len(tasks) == 0:
    print("No tasks available")
  else:
    print("\n Your Tasks")
    for i in range len(tasks)):
      print(i + 1, "_", tasks[i])

elif choice == '3':
  if len(tasks) == 0:
    print("No tasks to delete.")
  else:
    num = int(input("Enter task number to delete: "))
    if 1 <= num <= len(tasks):
      removed = tasks.pop(num-1)
      print("Removed task:", removed)
    else:
      print("Invalid task number...")

elif choice == '4':
  print("Exiting program...")
  break
  
else:
  print("Invalid choice, try again.")
  
     
    
    






