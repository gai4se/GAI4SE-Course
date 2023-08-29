import openai

# Open the file in read mode
with open('api.key', 'r') as file:
    # Read the entire content of the file as a string
    content = file.read()

# Set your OpenAI API key
openai.api_key = content

defect_code = "static void filter_mirror_setup(NetFilterState *nf, Error **errp)\n{\n    MirrorState *s = FILTER_MIRROR(nf);\n    Chardev *chr;\n    chr = qemu_chr_find(s->outdev);\n    if (chr == NULL) {\n        error_set(errp, ERROR_CLASS_DEVICE_NOT_FOUND,\n                  \"Device '%s' not found\", s->outdev);\n    qemu_chr_fe_init(&s->chr_out, chr, errp);"

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

