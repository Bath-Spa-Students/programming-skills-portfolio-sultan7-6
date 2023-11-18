prompt = "\nWhat topping would you like for your pizza?"
prompt += "\nEnter 'quit' when you are done: "

while True:
    topping = input(prompt)
    if topping != 'quit':
        print(f"  I'll add {topping} to your pizza.")
    else:
        break