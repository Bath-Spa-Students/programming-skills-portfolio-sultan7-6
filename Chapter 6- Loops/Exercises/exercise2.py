prompt = "How old are you?"
prompt += "\nEnter 'quit' when you are done. "

while True:
    age = input(prompt)
    if age == 'quit':
        break
    age = int(age)

    if age < 5:
        print("  You get in free!")
    elif age < 12:
        print("  Your ticket is $12.")
    else:
        print("  Your ticket is $19.")