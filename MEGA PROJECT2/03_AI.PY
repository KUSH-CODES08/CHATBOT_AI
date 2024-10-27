from openai import OpenAI

client = OpenAI(
    api_key="your_api_key"
)

command='''
YOUR COPIED PATH 
'''
completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a person named kush  who speaks hindi as well as  english .he is from india and is a coder . You analyize chat history  and respond like Kush "},
        {
            "role": "user",
            "content": command
        }
    ]
)

print(completion.choices[0].message.content) 


