#Intro
print("Division:")
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
    iv2 = i.copy()
    iv3 = i.copy()
 
    #Odd number gen
    end = len(i)
    for q in range(0, end + 1):
        if q % 2 != 0:
            iv.insert(q, "//")
            
    end = len(i)
    for q in range(0, end + 1):
        if q % 2 != 0:
            iv2.insert(q, "%")
            
    end = len(i)
    for q in range(0, end + 1):
        if q % 2 != 0:
            iv3.insert(q, "/")
    
    #Calculating quotient
    g = i[0]
    for k in i[1:]:
        g = g // k
        g1 = g % k
        g2 = g / k       
            
    #Printing Output
    iv = " ".join(str(p) for p in iv) 
    print(iv, "=", g)
    
    iv2 = " ".join(str(p1) for p1 in iv2) 
    print(iv2, "=", g1)
    
    iv3 = " ".join(str(p2) for p2 in iv3) 
    print(iv3, "=", g2)     
else:
    exit()