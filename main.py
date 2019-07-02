import json # Saving all of the tasks to the json file
from task import Task # Creates a Task Object
from add_function import add_task # Gets user input for the title and priority level with exceptions built in
from del_function import del_task # Gets user input for the index of the task the user wants to delete

class_file_list = []
dict_file_list = []

user_input = "000111222333444555666777888999"

print("Welcome to the To-Do List Application!")

while True: # Loops the Application for the user

    if user_input == "000111222333444555666777888999":  # Starting out the file with adding a task, rather than displaying the options
        print("To begin your task list, let's start by adding a Task!")
        key, value = add_task()
        task = Task(key, value)
        class_file_list.append(task)

        for task in class_file_list:                    #This code puts the task into the JSON file, then clears out the arrays
            dict_file_list.append(task.__dict__)
        with open("tasks.json", "w") as file_object:
            json.dump(dict_file_list, file_object)
        class_file_list.clear()
        dict_file_list.clear()

    user_input = input("_____________ MENU _____________\n  Press 1 to Add a Task\n  Press 2 to Delete a Task\n  Press 3 to View a Task List\n  Press 'q' to Quit the App\n") # Main Menu
    if user_input != "1" and user_input != "2" and user_input != "3" and user_input != "q":
        print("ERROR: Please enter an option from the list!")


    if user_input == "1": # Adds a Task to the Task List

        while True:

            with open("tasks.json") as file_object:
                dict_file_list = json.load(file_object)
            for dict_task in dict_file_list:
                task = Task.from_dictionary(dict_task)
                class_file_list.append(task)
            dict_file_list.clear()

            key, value = add_task()
            task = Task(key, value)
            class_file_list.append(task)


            for task in class_file_list:
                dict_file_list.append(task.__dict__)
            with open("tasks.json", "w") as file_object:
                json.dump(dict_file_list, file_object)
            class_file_list.clear()
            dict_file_list.clear()

            print("Task Added Successfully!")
            user_input = input("If you would like to return to the menu press 'm'\nIf you would like to quit press 'q'\nIf you would like to add another task press any other key!\n")
            if user_input == "m":
                break
            if user_input == "q":
                break

        
    if user_input == "2": # Deletes a Task from the Task List
        
        while True:
            cancel_input = input("Are you sure you would like to delete a task\nPress 'c' to cancel, or any other key to continue.")
            if cancel_input == "c":
                break
            with open("tasks.json") as file_object:
                dict_file_list = json.load(file_object)
            for dict_task in dict_file_list:
                task = Task.from_dictionary(dict_task)
                class_file_list.append(task)
            dict_file_list.clear()

            for index in range(len(class_file_list)):
                print(f"{(index + 1)} - {class_file_list[index].title} - {class_file_list[index].priority}")
            index_to_delete = del_task()
            del class_file_list[index_to_delete]

            for task in class_file_list:
                dict_file_list.append(task.__dict__)
            with open("tasks.json", "w") as file_object:
                json.dump(dict_file_list, file_object)
            class_file_list.clear()
            dict_file_list.clear()

            print("Task Deleted Successfully!")
            user_input = input("If you would like to return to the menu press 'm'\nIf you would like to quit press 'q'\nIf you would like to delete another task press any other key!\n")
            if user_input == "m":
                break
            if user_input == "q":
                break

    if user_input == "3": # Views the Task List

        with open("tasks.json") as file_object:
            dict_file_list = json.load(file_object)
        for dict_task in dict_file_list:
            task = Task.from_dictionary(dict_task)
            class_file_list.append(task)

        if len(class_file_list) == 0:
            print("There are no Tasks in your Task List!")

        for index in range(len(class_file_list)):
            print(f"{(index + 1)} - {class_file_list[index].title} - {class_file_list[index].priority}")

        class_file_list.clear()
        dict_file_list.clear()
        user_input = input("Press any key to return to the main menu, or press 'q' to quit: ")


    if user_input == "q": # Quits the Application
        print("We'll see you next time! And remember!")
        print("Organize, Prioritize, Optimize, Live!")
        break