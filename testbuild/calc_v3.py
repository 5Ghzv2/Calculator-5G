#importing math module
import math

#intro
print("Welcome to Calculator v3!")
print("Using Lists.")

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
usr_input = int(input("Choose your choice of operation (1 to 4): "))

if usr_input > 4:
    print("Calculator exitting, wrong input provided.")
    exit()

def arithmetic_calc(usr_input):                
    #Addition
    if usr_input == 1:
        #Calculating sum
        g = i[0]
        for k in i[1:]:
            g = g + k      
      
        #Printing Output
        iv = " + ".join(str(p) for p in i) 
        print(iv, "=", g)
        
    #Subtraction
    if usr_input == 2:    
    #Calculating sum
        g = i[0]
        for k in i[1:]:
            g = g - k      
        
        #Printing Output
        iv = " - ".join(str(p) for p in i) 
        print(iv, "=", g)
        
    #Multiplication
    if usr_input == 3:    
        #Calculating sum
        g = i[0]
        for k in i[1:]:
            g = g * k      
        
        #Printing Output
        iv = " * ".join(str(p) for p in i) 
        print(iv, "=", g)
        
    if usr_input == 4:
        iv = i.copy()
        iv2 = i.copy()
        iv3 = i.copy()
    
        #Calculating quotient
        g = i[0]
        for k in i[1:]:
            g = g / k
            g1 = g % k
            g2 = math.floor(g)      
            
        #Printing Output
        iv = " / ".join(str(p) for p in iv) 
        print(iv, "=", g)
        iv3 = " // ".join(str(p2) for p2 in iv3) 
        print(iv3, "=", int(g2), "(Floor Division, ie. quotient without decimals)")    
        iv2 = " % ".join(str(p1) for p1 in iv2) 
        print(iv2, "=", g1, "(Remainder)")

#Userinput == y/n        
Y_n = ["y", "n"]

def stringInList(str, lst):
    for i in lst:
        if str in i:
            return True
    print("Calculator exitting, wrong input provided.")
    exit()

#user input
i = []
i.append(int(input("Enter the number: ")))
i.append(int(input("Enter the number: ")))
       
#add/sub/mul/div statement
if usr_input == 1:
    sub = "add"
if usr_input == 2:
    sub = "subtract"
if usr_input == 3:
    sub = "multiply"
if usr_input == 4:
    sub = "divide"

#More Numbers    
t = str(input(f"Do you want to {sub} more numbers? (y/n): "))
stringInList(t, Y_n)

while t == "y":
    i.append(int(input("Enter the number: ")))
    t = str(input(f"Do you want to {sub} more numbers? (y/n): "))
        
if t == "n":
    arithmetic_calc(usr_input)