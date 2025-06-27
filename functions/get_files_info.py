import os


def get_files_info(working_directory, directory=None):
    abs_working_dir = os.path.abspath(working_directory)
    search_dir = abs_working_dir

    if directory:
        search_dir = os.path.abspath(os.path.join(working_directory, directory))

    # searching in working dir
    if not search_dir.startswith(abs_working_dir):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if not os.path.isdir(search_dir):
        return f'Error: "{directory}" is not a directory'

    try:
        lst_dir_contents = os.listdir(search_dir)
        files_info = []

        for item in lst_dir_contents:
            full_item_path = os.path.join(search_dir, item)
            files_info.append(
                f"- {item}: file_size={os.path.getsize(full_item_path)} bytes, is_dir={os.path.isdir(full_item_path)}"
            )
        return "\n".join(files_info)

    except Exception as e:
        return f"Error listing files: {e}"
