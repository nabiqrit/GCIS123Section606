def choose_operation(num1,num2):
    print("Welcome to the calculator")
    print("Which operation would you like to perform")
    print(" 1- Addition")
    print(" 2- Subtraction")
    print(" 3- Multiplication")
    print(" 4- Division")
    chooseoperation=int(input("Enter your choice: "))
    if chooseoperation==1:
        return "Answer :",num1+num2
    elif chooseoperation==2:
        return "Answer: ",num1-num2
    elif chooseoperation==3:
        return "Answer: ",num1*num2
    elif chooseoperation==4:
        print("Which division would you like to do : " \
        "1- Regular Division" \
        "2- Integer Division")
        divisontype=int(input("Choose which division do you want to perform"))
        if divisontype==1:
            return num1/num2
        else:
            return num1//num2
    else:
        print("Invalid Option Please Retry")




def main():
    num1=int(input("Enter your 1st number:"))
    num2=int(input("Enter your 2nd number:"))
    result=choose_operation(num1,num2)
    print(result)

main()


    