
while True:
        print("\nWelcome to my Calculator!")
        print("1. Addition")
        print ("2. Subtraction")
        print ("3. Division")
        print ("4. Multiplication")
        print ("5. Exit")

        choice = input("Choose an option (1-5):")
        if choice == "5":
            print("Exiting calculator. Goodbye!")
            break

        if choice not in ["1", "2", "3", "4", "5"]:
            print ("Invalid Choice, Please choose a valid option.")
            continue

        try:
            Num1 = int(input("Enter your first number: "))
            Num2 = int(input("Enter your second number: "))
            Num3 = int(input("Enter your third number: "))
        except ValueError:
            print ("INVALID INPUT! Please enter only Integers.") 
            continue

        if choice == "1":
            print (f"Addition Result: {Num1+Num2+Num3}")
        elif choice == "2":
            print (f"Subtraction Result: {Num1-Num2-Num3}")
        elif choice == "3":
            if Num2 == 0 or Num3 == 0:
                print ("Error")
            else:
                print (f"Division Result: {Num1/Num2/Num3}")
        elif choice == "4":
            print (f"Multiplication Result: {Num1*Num2*Num3}")








