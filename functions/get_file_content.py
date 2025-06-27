import os


def get_file_content(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.join(abs_working_dir, file_path)

    if not abs_file_path.startswith(abs_working_dir):
        print(
            f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        )
        return

    if not os.path.isfile(abs_file_path):
        print(f'Error: File not found or is not a regular file: "{file_path}"')
        return

    with open(abs_file_path, "r") as file:
        content = file.read()

    if len(content) > 10000:
        print(f'{content[:10000]}...File "{file_path}" truncated at 10000 characters')

    else:
        print(content)


# get_file_content("calculator", "main.py")
# get_file_content("calculator", "pkg/calculator.py")
# get_file_content("calculator", "/bin/cat")
# get_file_content("calculator", "lorem.txt")  # this should raise an error
