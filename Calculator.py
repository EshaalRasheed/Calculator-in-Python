while True:
    try:
        print(".....Calculator in Python.....")
        a = int(input("Enter First Number: "))
        b = int(input("Enter Second Number: "))
        
        print("1: Add Numbers")
        print("2: Subtract Numbers")
        print("3: Multiply Numbers")
        print("4: Divide Numbers")
        print("5: Find Exponent")
        print("6: Find Modulus")
        
        choice = int(input("Select your choice (1-6): "))
        
        if choice == 1:
            print("Sum is", a + b)
        elif choice == 2:
            print("Difference is", a - b)
        elif choice == 3:
            print("Product is", a * b)
        elif choice == 4:
            if b == 0:
                print("Error! Division by zero is not allowed.")
            else:
                print("Division Result is", a / b)
        elif choice == 5:
            print("Exponent is", a ** b)
        elif choice == 6:
            print("Modulus is", a % b)
        else:
            print("Invalid choice. Please choose a number between 1 and 6.")
    
    except ValueError:
    
        print("Invalid input! Please enter numbers only.")
    
    
    next_calculation = input("Do you want to perform another calculation? (yes/no): ").lower()
    if next_calculation != 'yes':
        print("Goodbye!")
        break
