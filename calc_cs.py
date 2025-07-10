def Addition():
    print(f"the Addition of the number is:{n1+n2}")
def Subtraction():
    print(f"the Subtraction of the number is:{n1-n2}")
def Multiplication():
    print(f"the Multiplication of the number is:{n1*n2}")
def Division():
    print(f"the Division of the number is:{n1/n2}")
def exit():
    print(invalid)

if __name__ == "__main__": 

    n1 = float(input("Enter the number you like:"))
    n2 = float(input("Enter the number you like:"))
    
   

    choice=int(input("Enter the choice you like:"))

    if choice==1:
        print("1.Addition")
        Addition()
    elif choice==2:
        print("2.Subtraction")
        Subtraction()
    elif choice==3:
        print("3.Multiplication")
        Multiplication()
    elif choice==4:
        print("4.Division")
        Division()
    else:
        exit()
