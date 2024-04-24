class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("Task added successfully!")

    def view_tasks(self):
        if self.tasks:
            print("Your To-Do List:")

            for index, task in enumerate(self.tasks, 1):
                print(f"{index}. {task}")
        else:
            print("Your to-do list is empty.")

    def delete_task(self, task_number):
        if task_number >= 1 and task_number <= len(self.tasks):
            deleted_task = self.tasks.pop(task_number - 1)
            print(f"Task '{deleted_task}' deleted successfully!")
        else:
            print("Invalid task number.")

def main():
    todo_list = TodoList()
    
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Quit")

        choice = input("Enter your choice [1-4]: ")

        if choice == "1":
            task = input("Enter a task: ")
            todo_list.add_task(task)
        elif choice == "2":
            todo_list.view_tasks()
        elif choice == "3":
            task_number = int(input("Enter the task number to delete: "))
            todo_list.delete_task(task_number)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main()
