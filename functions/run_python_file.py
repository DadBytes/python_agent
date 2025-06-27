import os
import subprocess

from google.genai import types


def run_python_file(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(abs_working_dir, file_path))

    if not abs_file_path.startswith(abs_working_dir):
        print(
            f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        )
        return

    if not os.path.isfile(abs_file_path):
        print(f'Error: File "{file_path}" not found.')
        return

    if not file_path.endswith(".py"):
        print(f'Error: "{file_path}" is not a Python file.')

    try:
        result = subprocess.run(
            ["python3", abs_file_path],
            timeout=30,
            capture_output=True,
            text=True,
            cwd=abs_working_dir,
        )

        output = []

        if result.stdout:
            output.append(f"STDOUT:\n{result.stdout}")
        if result.stderr:
            output.append(f"STDERR:\n{result.stderr}")

        if result.returncode != 0:
            output.append(f"Process exited with code {result.returncode}")

        return "\n".join(output) if output else "No output produced."

    except Exception as e:
        return f"Error: executing Python file: {e}"


schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs a given python file, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file_path of the python file.",
            ),
        },
    ),
)
