FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """Read a txt file and return a list with
    a to-do items."""
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
        return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """Read a list of to-do items and write
    to a txt file."""
    with open(filepath, "w") as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    pass
