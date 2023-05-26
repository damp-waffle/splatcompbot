import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
def generate():
    return(openai.Completion.create(
    model="davinci:ft-personal-2023-05-18-07-16-43",
    prompt="",
    max_tokens=100,
    temperature=0.1
    ).get('choices')[0].get('text'))
# openai api completions.create -m davinci:ft-personal-2023-05-18-07-16-43 -p <YOUR_PROMPT>