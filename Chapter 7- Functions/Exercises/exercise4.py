def make_shirt(size='large', message='I love UAE!'):
    """Summarize the shirt that's going to be made."""
    print(f"\nI'm going to make a {size} t-shirt.")
    print(f'It will say, "{message}"')

make_shirt()
make_shirt(size='large')
make_shirt('small', 'Programmers are smart.')