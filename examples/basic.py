"""
STORM AI — Python client example.
pip install openai
"""
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_API_KEY",
    base_url="https://api.stormengine.cloud/v1"
)

# Simple completion
response = client.chat.completions.create(
    model="storm-qwen32b",
    messages=[
        {"role": "system", "content": "You are a coding assistant. Always return valid JSON."},
        {"role": "user", "content": "Sort this list in Python: [3, 1, 4, 1, 5, 9]"}
    ],
    temperature=0.1,
    max_tokens=500
)

print(response.choices[0].message.content)

# Streaming
stream = client.chat.completions.create(
    model="storm-qwen32b",
    messages=[{"role": "user", "content": "Write a binary search in Python"}],
    stream=True
)

for chunk in stream:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)
