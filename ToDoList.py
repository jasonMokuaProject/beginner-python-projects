# To Do List

def main():
    tasks = []
    playornot = True

    while playornot:
        print(" ------ To Do List ------ ")
        print(" 1. Add Task ")
        print(" 2. Show Specific Task ")
        print(" 3. Show All Tasks")
        print(" 4. Mark Task Complete")
        print(" 5. Exit")

        user_option = input("Enter Your Choice: ")

        if int(user_option) == 1:
            the_task = input(" \n Enter the task you want to add to your To-Do-List: ")
            tasks.append({"task":the_task,"done":False})

        if int(user_option) == 2:
            for i,x in enumerate(tasks,start=1):
                print(f"Task Number {i} : {x['task']}")

            the_task_user_picked = int(input("Enter the number of the task you want to show: "))
            print(f"{tasks[the_task_user_picked - 1]['task']}")

        if int(user_option) == 3:
            number_of_tasks = 0
            for x in tasks:
                number_of_tasks += 1
                print(" Task number "+str(number_of_tasks)+ " : " +x["task"] +"\n")

        if int(user_option) == 4:
            for x,y in enumerate(tasks,start=1):
                print(f" Task Number {x} : {y['task']}")
                user_mark_option = input("Enter the number of the task you want to mark as complete")


        if int(user_option) == 5:
            playornot = False















main()