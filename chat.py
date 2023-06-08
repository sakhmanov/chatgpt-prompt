import openai
import sys
import os

argv = sys.argv[1:]

if not sys.stdin.isatty():
    stdin_list = []
    for line in sys.stdin:
        stdin_list.append(line.rstrip())
    argv.extend(stdin_list)

# Set up the OpenAI API client
openai.api_key = os.getenv('OPENAI_API_KEY')

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

response = get_completion(prompt=' '.join(argv))
print(response)
