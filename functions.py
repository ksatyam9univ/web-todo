FILE_PATH = 'todos.txt'


def get_todos(file_path=FILE_PATH):
    """
    Reads the targeted text file and returns a list,
    in which each element is each line of the text file.
    :param file_path:
    :return:
    """
    with open(file_path, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(list_item, file_path=FILE_PATH):
    """
    Overwrite the target text file with new list,
    such that each element of list will become each line of text file.
    :param list_item:
    :param file_path:
    """
    with open(file_path, 'w') as file_local:
        file_local.writelines(list_item)



