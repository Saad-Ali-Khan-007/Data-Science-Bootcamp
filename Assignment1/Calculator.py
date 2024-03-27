def calculator():
    while True:
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


calculator()
