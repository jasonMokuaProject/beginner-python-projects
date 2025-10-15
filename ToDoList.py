import json
import os

def load_tasks():
    tasks = []
    if os.path.exists("daily_tasks.txt"):
        with open("daily_tasks.txt", "r") as f:
            for line in f:
                line = line.strip()
                if line:
                    tasks.append(json.loads(line))
    return tasks

def save_tasks(tasks):
    with open("daily_tasks.txt", "w") as f:
        for task in tasks:
            f.write(json.dumps(task) + "\n")

def main():
    tasks = load_tasks()
    playornot = True

    while playornot:
        print("\n------ To Do List ------")
        print("1. Add Task")
        print("2. Show Specific Task")
        print("3. Show All Tasks")
        print("4. Mark Task Complete")
        print("5. Clear All Tasks")
        print("6. Exit")

        try:
            user_option = int(input("Enter Your Choice: "))

            if user_option == 1:
                the_task = input("\nEnter the task you want to add: ")
                tasks.append({"task": the_task, "done": False})
                save_tasks(tasks)

            elif user_option == 2:
                for i, x in enumerate(tasks, start=1):
                    print(f"{i}. {x['task']}")
                the_task_user_picked = int(input("Enter the number of the task to show: "))
                print(f"Task: {tasks[the_task_user_picked - 1]['task']}")
                print(f"Done: {tasks[the_task_user_picked - 1]['done']}")

            elif user_option == 3:
                if not tasks:
                    print("No tasks found.")
                else:
                    for i, x in enumerate(tasks, start=1):
                        status = "✅" if x['done'] else "❌"
                        print(f"{i}. {x['task']} - {status}")

            elif user_option == 4:
                for i, y in enumerate(tasks, start=1):
                    print(f"{i}. {y['task']} - {'✅' if y['done'] else '❌'}")
                user_mark_option = int(input("Enter the number of the task to mark as complete: "))
                tasks[user_mark_option - 1]['done'] = True
                save_tasks(tasks)
                print("Task marked as complete!")

            elif user_option == 5:
                confirm = input("Are you sure you want to clear all tasks? (y/n): ")
                if confirm.lower() == "y":
                    tasks = []
                    save_tasks(tasks)
                    print("All tasks cleared.")

            elif user_option == 6:
                playornot = False
                print("Goodbye!")

            else:
                print("Invalid choice. Try again.")

        except Exception as e:
            print(f"Error: {e}. Please enter a valid value.")

main()
