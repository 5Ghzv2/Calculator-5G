usr_input = str(input("Do you want to add more numbers? (y/n): "))
lst = ["y", "n"]

def stringInList(str, lst):
    for i in lst:
        if str in i:
            return True
    print("Calculator exitting, wrong input provided.")
    exit()

stringInList(usr_input, lst)