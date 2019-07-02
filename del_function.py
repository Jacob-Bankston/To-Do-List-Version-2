def del_task():
    while True:
        del_input = input("Please select a task to remove from the list: ")
        try:
            del_index = int(del_input)
            del_index -= 1
            return del_index
        except ValueError:
            print("ERROR: Please enter a number from the list to delete.")