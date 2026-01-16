# Switch Case Example

a = 10
b = 5
choice = 2   # change value to test

match choice:
    case 1:
        print("Addition:", a + b)
    case 2:
        print("Subtraction:", a - b)
    case 3:
        print("Multiplication:", a * b)
    case 4:
        print("Division:", a / b)
    case _:
        print("Invalid choice")
