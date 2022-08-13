#Welcome statement
print("Welcome to Calculator v1")

#Running Program again
loop_again = 0

#Calculation Type
while loop_again == 0:
    print("1: Addition")
    print("2: Subtraction")
    print("3: Multiplication")
    print("4: Division")
    calc_method = int(input("Select which kind of operation you would like to do: "))

    #Addition
    if calc_method == 1:
        x = int(input("Enter the first addend: "))
        y = int(input("Enter the second addend: "))        

        def Addition():
            print(x, "+", y, "=", x + y)

        Addition()

    #Subtraction
    if calc_method == 2:
        x = int(input("Enter the Minuend: "))
        y = int(input("Enter the Subtrahend: "))        

        def Subtraction():
            print(x, "-", y, "=", x - y)

        Subtraction()

    #Multiplication
    if calc_method == 3:
        x = int(input("Enter the Multiplicand: "))
        y = int(input("Enter the Multiplier: "))        

        def Multiplication():
            print(x, "*", y, "=", x * y)

        Multiplication()

   #Division
    if calc_method == 4:
        x = int(input("Enter the Dividend: "))
        y = int(input("Enter the Divisor: "))        

        def Division():
            print(x, "÷", y, "=", x / y)

        Division()

    #Running Program Again
    loop_again_user_input = str(input("Do you want to Calculate Again (y/n): "))
    if loop_again_user_input == "y":
        print("=" * 40)
        loop_again = 0
    else:
        loop_again = 1
        print("Exiting Calculator.")
        exit()