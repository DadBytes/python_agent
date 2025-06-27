import os


def write_file(working_directory, file_path, content):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.join(abs_working_dir, file_path)

    if not abs_file_path.startswith(abs_working_dir):
        print(
            f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        )
        return

    if not os.path.isfile(abs_file_path):  # check to see if file already exists
        if len(file_path.split("/")) > 1:  # check to see if directory exists
            os.makedirs(os.path.dirname(abs_file_path), exist_ok=True)
    with open(abs_file_path, "w") as file:
        file.write(content)

    print(f'Successfully wrote to "{file_path}" ({len(content)} characters written)')
