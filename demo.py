import os
import requests
import json

# Set your OpenAI API key here
OPENAI_API_KEY = "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"

# Set the endpoint
api_endpoint = "https://api.openai.com/v1/engines/davinci/completions"

# Set the prompt
prompt_text = "Once upon a time, there was a"

# Set the request headers
headers = {
    "Authorization": f"Bearer {OPENAI_API_KEY}",
    "Content-Type": "application/json",
}

# Set the request payload
data = {
    "prompt": prompt_text,
    "max_tokens": 100,
}

# Send the request
response = requests.post(api_endpoint, headers=headers, json=data)

# Parse and print the response
if response.status_code == 200:
    print("Generated text:")
    print(response.json()['choices'][0]['text'])
else:
    print("Error:", response.text)
