import os
from google.genai import types

MAX_CHARS = 10000


def get_file_content(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(abs_working_dir, file_path))

    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    if not os.path.isfile(abs_file_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'

    try:
        with open(abs_file_path, "r") as file:
            content = file.read(MAX_CHARS)

            if os.path.getsize(abs_file_path) > MAX_CHARS:
                content += f'[...File "{file_path}" truncated at 10000 characters]'

        return content

    except Exception as e:
        return f'Error reading file "{file_path}": {e}'


schema_get_files_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Returns the content of a file, limited to the first 10,000 characters, and constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file that we are asking for the contents of.",
            ),
        },
    ),
)
