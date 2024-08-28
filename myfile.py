def add_numbers(a, b):
    return a + b

def main():
    num1 = 5
    num2 = 10  # Error: mixing integer and string types
    result = add_numbers(num1, num2)  # This will cause a TypeError
    print("The sum is:", result)

if __name__ == "__main__":
    main()