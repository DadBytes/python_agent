import os
import sys

from dotenv import load_dotenv
from google import genai
from google.genai import types

from functions.get_files_info import schema_get_files_info
from functions.get_file_content import schema_get_files_content
from functions.run_python_file import schema_run_python_file
from functions.write_file_content import schema_write_file
from system_prompt import system_prompt

if len(sys.argv) < 2:
    raise ValueError("Must include a prompt.")


load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

user_prompt = sys.argv[1]

messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
]

model = "gemini-2.0-flash-001"
contents = messages

available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_files_content,
        schema_run_python_file,
        schema_write_file,
    ]
)

response = client.models.generate_content(
    model=model,
    contents=contents,
    config=types.GenerateContentConfig(
        tools=[available_functions], system_instruction=system_prompt
    ),
)
for function_call_part in response.function_calls:
    print(f"Calling function: {function_call_part.name}({function_call_part.args})")

if len(sys.argv) > 2 and (sys.argv[2] == "--verbose"):
    print(f"User prompt: {user_prompt}")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
