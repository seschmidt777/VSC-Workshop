def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

def main():
    x = 9
    y = 1

    addition = add(x, y)
    print(f"Addition: {add}")

    subtraction = subtract(x, y)
    print(f"Subtraction: {sub}")

    multiplication = multiply(x, y)
    print(f"Multiplication: {multiplication}")

    try:
        division = divide(x, y)
        print(f"Division: {division}")
    except ValueError as er:
        print(eror)

    text = "Result: " + 1
    print(text)

    my_list = ["A", "B", "I"]
    print(my_list[3])

if __name__ == "__main__":
    main()
