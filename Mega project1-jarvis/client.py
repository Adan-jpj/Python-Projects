from openai import OpenAI

# client = OpenAI()
client = OpenAI(
    api_key="sk-proj-WxS17egGk2PnwmzCHcDWT3BlbkFJMj6bYTk9jG1bqZaFTcj",
)

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts."},
        {"role": "user", "content": "compose a poem that explains the concept of recursion in programming"}
    ]
)

print(completion.choices[0].message)


