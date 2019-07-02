def add_task():

    while True:
        task_title = input("Please enter a title for the task: ")
        if task_title == "":
            print("ERROR: The title you entered for the task was blank.")
        else:
            break

    print("  1 - High   2 - Medium   3 - Low  ")

    while True:
        task_priority = input("Please enter a priority level for the task: ")
        try:
            task_priority_int = int(task_priority)
            if task_priority_int > 3 or task_priority_int < 0:
                print("ERROR: Please enter one of the available priority options.")
            else:
                break
        except ValueError:
            print("ERROR: Please enter one of the available priority options.")
    if task_priority_int == 3:
        priority = "Low"
    if task_priority_int == 2:
        priority = "Medium"
    if task_priority_int == 1:
        priority = "High"
    return task_title, priority