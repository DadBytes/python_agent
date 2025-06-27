import os


def get_files_info(working_directory, directory=None):
    # searching in working dir
    if directory is None or directory == ".":
        search_dir = os.path.abspath(working_directory)
        lst_dir_contents = os.listdir(search_dir)
    else:
        lst_working_dir = os.listdir(working_directory)

        if directory not in lst_working_dir:
            print(
                f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
            )
            return

        if not os.path.isdir(
            os.path.join(os.path.abspath(working_directory), directory)
        ):
            print(f'Error: "{directory}" is not a directory')
            return

        search_dir = os.path.join(os.path.abspath(working_directory), directory)
        lst_dir_contents = os.listdir(search_dir)

    for item in lst_dir_contents:
        full_item = os.path.join(search_dir, item)
        print(
            f"- {item}: file_size={os.path.getsize(full_item)} bytes, is_dir={os.path.isdir(full_item)}"
        )
