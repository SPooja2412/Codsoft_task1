class Task:
    def __init__(self, title):
        self.title = title
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "✔" if self.completed else "❌"
        return f"{status} {self.title}"


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title):
        new_task = Task(title)
        self.tasks.append(new_task)

    def view_tasks(self):
        for index, task in enumerate(self.tasks, start=1):
            print(f"{index}. {task}")

    def mark_as_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_completed()

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)

    def update_task(self, index, new_title):
        if 0 <= index < len(self.tasks):
            self.tasks[index].title = new_title
        else:
            print("Invalid Task Index")


def main():
    todolist = ToDoList()

    while True:
        print("\nTO DO LIST")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Update Task")
        print("6. Exit")

        choice = input("Enter your choice from (1-6): ")

        if choice == '1':
            title = input("Enter task title: ")
            todolist.add_task(title)
        elif choice == '2':
            todolist.view_tasks()
        elif choice == '3':
            index = int(input("Enter task number to mark as completed: ")) - 1
            todolist.mark_as_completed(index)
        elif choice == '4':
            index = int(input("Enter task number to delete: ")) - 1
            todolist.delete_task(index)
        elif choice == '5':
            index = int(input("Enter task number to update: ")) - 1
            new_title = input("Enter new task title: ")
            todolist.update_task(index, new_title)
        elif choice == '6':
            print("Exiting the program, GOOD BYE!!")
            break
        else:
            print("Invalid choice, Please try again!")


if __name__ == "__main__":
    main()


        








    
        
