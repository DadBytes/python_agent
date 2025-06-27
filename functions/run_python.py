import os


def run_python_file(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.join(abs_working_dir, file_path)

    if not abs_file_path.startswith(abs_working_dir):
        print(
            f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        )
        return

    if not os.path.isfile(abs_file_path):
        print(f'Error: "{file_path}" is not a Python file.')
        return
    
    if not file_path.endswith(".py"):
        print(f'Error: "{file_path}" is not a Python file.')

    subprocess.run(abs_file_path, timeout=30, capture_output=True)
