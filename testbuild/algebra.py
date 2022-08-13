#Welcome statement
print("Welcome to Quasicrystal Calculator")

#Running Program again
loop_again = True
y_ = 0
while loop_again == True:
    
    #Equation or Expression?
    eq_ex = dict()

    #Equation
    eq = eq_ex.copy()

    #Splitting Terms
    term_loop_again = True
    while term_loop_again == True:

        #Terms
        y_ = y_ + 1
        term = input("Enter your Term: ")
        eq.update({y_:term})
        eq_term = eq
        print(eq, type(eq)) #TESTING

        #Terms again...
        term_loop_again_user_input = str(input("Do you want to enter a Term again (y/n): "))
        if term_loop_again_user_input == "y":
            print("=" * 40)
            term_loop_again = True
            eq = eq.copy()
            print(eq) #TESTING
            eq.update(eq_term)
            eq = eq

        elif term_loop_again_user_input == "n":
            term_loop_again = False

            #Equals to (=)
            equal_to = str(input("Do you want to enter an equal-to symbol[=] again (y/n): "))
            if equal_to == "y":
                eq["equal_to"] = "="       

    if "=" in eq_ex: #TESTING
        print(eq)

    #Running Program Again
    loop_again_user_input = str(input("Do you want to calculate again (y/n): "))
    if loop_again_user_input == "y":
        print("=" * 40)
        loop_again = True
    elif loop_again_user_input == "n":
        loop_again = False
        print("Exiting Calculator.")
        exit()