FILEPATH = 'todos.txt'


def get_todos(filepath=FILEPATH):

    """
    Read a text file and return them in a list
    :param filepath: location for the file
    :return: return the file lines in a list
    """

    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):

    """
    Write or update the to do list

    :param todos_arg: new data in the list
    :param filepath: location for the file
    :return:
    """
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


if __name__ == '__main__':
    print(get_todos())