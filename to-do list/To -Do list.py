# Function to display the menu
def display_menu():
    print("To-do List Menu:")
    print("1. View To-do List")
    print("2. Add To-do")
    print("3. Mark To-do as Done")
    print("4. Clear To-do List")
    print("5. Exit")

# Function to view the todo list
def view_todo_list(todo_list):
    print("Todo List:")
    if not todo_list:
        print("Empty")
    else:
        for idx, todo in enumerate(todo_list, start=1):
            print(f"{idx}. {todo}")

# Function to add a todo
def add_todo(todo_list):
    todo = input("Enter todo: ")
    todo_list.append(todo)
    print("Todo added successfully!")

# Function to mark a todo as done
def mark_todo_as_done(todo_list):
    view_todo_list(todo_list)
    try:
        idx = int(input("Enter the index of todo to mark as done: ")) - 1
        if 0 <= idx < len(todo_list):
            todo_list.pop(idx)
            print("Todo marked as done!")
        else:
            print("Invalid index!")
    except ValueError:
        print("Invalid input!")

# Function to clear the todo list
def clear_todo_list(todo_list):
    todo_list.clear()
    print("Todo list cleared!")

if __name__ == "__main__":
    todo_list = []

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            view_todo_list(todo_list)
        elif choice == '2':
            add_todo(todo_list)
        elif choice == '3':
            mark_todo_as_done(todo_list)
        elif choice == '4':
            clear_todo_list(todo_list)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please enter a valid option.")
