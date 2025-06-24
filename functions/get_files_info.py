import os


def get_files_info(working_directory, directory=None):
    abs_path_working_directory = os.path.abspath(working_directory)
    abs_path_directory = os.path.join(abs_path_working_directory, directory)
    lst_working_dir_contents = os.listdir(working_directory)

    if directory is None or directory not in lst_working_dir_contents:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if not os.path.isdir(os.path.join(working_directory, directory)):
        return f'Error: "{directory}" is not a directory'

    lst_dir_contents = os.listdir(abs_path_directory)

    for item in lst_dir_contents:
        full_item = os.path.join(abs_path_directory, item)
        print(
            f"- {item}: file_size={os.path.getsize(full_item)} bytes, is_dir={os.path.isdir(full_item)}"
        )

    # print(os.path.join(abs_path_working_directory, directory))
    # print(os.path.isdir(os.path.join(abs_path_working_directory, directory)))
    # return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    # for item in lst_dir_contents:
    #     if os.path.isdir(os.path.join(abs_path_working_directory, item)):
    #         print("dir", item)

    # if directory is none not in working_directory:
    #     print()
    # f'Error: Cannot list "{directory}" as it is outside the permitted working directory'


# get_files_info("calculator", ".")
# get_files_info("calculator", "pkg")
get_files_info("calculator", "/bin")
get_files_info("calculator", "../")
