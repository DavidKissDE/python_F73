def multiply(x: int, y: int) -> int:
    sum = 0
    for x in range(0, x):
        sum += y
    return sum


def getUserInput(message: str) -> int:
    user_input: str = input(message)
    if not user_input.isnumeric():
        raise Warning
    else:
        return int(user_input)


x = None
y = None

while not (x or y):
    try:
        x, y = getUserInput('Enter your first number: '), getUserInput(
            'Enter a second number: ')
    except Warning:
        print("This isn't a number")

print(multiply(x, y))
