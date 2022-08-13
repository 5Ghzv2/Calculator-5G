#intro
print("Welcome to Calculator v2!")
print("Using Lists.")

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
usr_input = int(input("Choose your choice of operation (1 to 4): "))

def addition():
    iv = i.copy()
 
    #Odd number gen
    end = len(i)
    for q in range(0, end + 1):
        if q % 2 != 0:
            iv.insert(q, "+")

    #Calculating sum
    g = i[0]
    for k in i[1:]:
        g = g + k       
        
    #Printing Output
    iv = " ".join(str(p) for p in iv) 
    print(iv, "=", g)

def subtraction():
    iv = i.copy()
 
    #Odd number gen
    end = len(i)
    for q in range(0, end + 1):
        if q % 2 != 0:
            iv.insert(q, "-")

    #Calculating sum
    g = i[0]
    for k in i[1:]:
        g = g - k       
        
    #Printing Output
    iv = " ".join(str(p) for p in iv) 
    print(iv, "=", g)
    
def multiplication():
    iv = i.copy()
 
    #Odd number gen
    end = len(i)
    for q in range(0, end + 1):
        if q % 2 != 0:
            iv.insert(q, "*")

    #Calculating sum
    g = i[0]
    for k in i[1:]:
        g = g * k       
        
    #Printing Output
    iv = " ".join(str(p) for p in iv) 
    print(iv, "=", g)
    
def division():
    iv = i.copy()
    iv2 = i.copy()
 
    #Odd number gen
    end = len(i)
    for q in range(0, end + 1):
        if q % 2 != 0:
            iv.insert(q, "/")
            
    end = len(i)
    for q in range(0, end + 1):
        if q % 2 != 0:
            iv2.insert(q, "%")
    
    #Calculating quotient
    g = i[0]
    for k in i[1:]:
        g = g / k
        g1 = g % k       
            
    #Printing Output
    iv = " ".join(str(p) for p in iv) 
    print(iv, "=", g)
    
    iv2 = " ".join(str(p1) for p1 in iv2) 
    print(iv2, "=", g1)

#initializing list
i = list() #[]
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


t = str(input(f"Do you want to {sub} more numbers? (y/n): "))
while t == "y":
    i.append(int(input("Enter the number: ")))
    t = str(input(f"Do you want to {sub} more numbers? (y/n): "))

if t == "n":
    if usr_input == 1:
        addition()
    if usr_input == 2:
        subtraction()
    if usr_input == 3:
        multiplication()
    if usr_input == 4:
        division()