import openai

# Open the file in read mode
with open('api.key', 'r') as file:
    # Read the entire content of the file as a string
    content = file.read()

# Set your OpenAI API key
openai.api_key = content

conversation_history = [{"role": "system", "content": "You are a weather reporter."}]

while True:


    user_input = input("Enter something: ")

    prompt={"role": "user", "content": "{}".format(user_input)},

    # Create a conversation history
    conversation_history.extend(prompt)

    # Generate a response
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation_history
    )

    # Extract and print assistant's reply
    assistant_reply = response['choices'][0]['message']['content']
    print(assistant_reply)
    conversation_history.extend([{"role": "assistant", "content": assistant_reply}])

