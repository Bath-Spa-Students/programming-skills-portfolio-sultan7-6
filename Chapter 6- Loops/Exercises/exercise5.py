sandwich_orders = [
    'pastrami', 'chicken', 'grilled cheese', 'pastrami',
    'turkey', 'roasted beef', 'pastrami']
finished_sandwiches = []

print("I'm sorry, we're out of pastrami today.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print("\n")
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I'm preparing your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\n")
for sandwich in finished_sandwiches:
    print(f"I made a {sandwich} sandwich.")