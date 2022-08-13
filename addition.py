#Intro
print("Addition:")
#initializing list
i = list() #[]

i.append(int(input("Enter the number: ")))
i.append(int(input("Enter the number: ")))

t = str(input("Do you want to add more numbers? (y/n): "))
while t == "y":
    i.append(int(input("Enter the number: ")))
    t = str(input("Do you want to add more numbers? (y/n): "))

if t == "n":
    #Conlusion
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
else:
    exit()