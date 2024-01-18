import openai

openai.api_key = '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'

messages = []

while True:
    content = input("User: ")
    messages.append({"role": "user", "content":content})

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages   # 'message'를 'messages'로 변경
    )

    chat_response = completion.choices[0].message['content']  # 'message.content'를 'message['content']'로 변경
    print(f"ChatGpt: {chat_response}")
    messages.append({'role':"assistant", "content": chat_response})
