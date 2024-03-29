def calculator():
    while True:
        try:
            print("")
            print("")
            print("Welcome to simple Calculator")
            print("")
            print("")

            print("1. Add Operation")
            print("2. Subtarct Operation")
            print("3. Multiplication Operation")
            print("4. Division Operation")
            print("5. Exit Operation")

            choice = int(input("Enter Your Choice (1/2/3/4/5): "))
            if choice == 5:
                break
            else:
                num1 = int(input("Enter first number: "))
                num2 = int(input("Enter first number: "))
                if choice == 1:
                    sum = num1 + num2
                    print(f"Result: {num1} + {num2} = {num1+num2}")
                elif choice == 2:
                    sub = num1 - num2
                    print(f"Result: {num1} - {num2} = {num1-num2}")
                elif choice == 3:
                    prod = num1 * num2
                    print(f"Result: {num1} * {num2} = {num1*num2}")
                elif choice == 4:
                    div = num1 / num2
                    print(f"Result: {num1} / {num2} = {num1/num2}")

                print("")
                print("")
        except ValueError:
            print("Invalid Input")

        except Exception as ZeroDivisionError:
            print("Canont divide by zero")


calculator()


# Function: calculator()
# Test cases:
# Test Case 1: Test addition operation
# Input: 1, 5, 7
# Expected Output: "Result: 5 + 7 = 12"
# Test Case 2: Test subtraction operation
# Input: 2, 10, 3
# Expected Output: "Result: 10 - 3 = 7"
# Test Case 3: Test multiplication operation
# Input: 3, 6, 8
# Expected Output: "Result: 6 * 8 = 48"
# Test Case 4: Test division operation
# Input: 4, 20, 4
# Expected Output: "Result: 20 / 4 = 5.0"
# Test Case 5: Test division by zero
# Input: 4, 10, 0
# Expected Output: "Cannot divide by zero"
# Test Case 6: Test invalid input (non-integer choice)
# Input: "abc"
# Expected Output: "Invalid Input"
# Test Case 7: Test invalid input (non-integer numbers)
# Input: 1, "abc", 5
# Expected Output: "Invalid Input"
# Test Case 8: Test exit operation
# Input: 5
# Expected Output: Program exits
