def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y !=0:
        return x/y
    else:
        return "cannot divide by zero "

def calculator():
    print("easy calculator")
    print("1. add")
    print("2. sub")
    print("3. multi")
    print("4. divide")

    choice=input("enter one of the opiton (1/2/3/4): ")

    num1= float(input("enter urs first number:  "))
    num2=float(input("enter urs seconed number:  "))

    if choice=="1":
       print(num1,"+",num2,"=",add(num1, num2))
    if choice=="2":
       print(num1,"-",num2,"=",subtract(num1, num2))
    if choice=="3":
       print(num1,"*",num2,"=",multiply(num1, num2))
    if choice=="4":
       print(num1,"/",num2,"=",divide(num1, num2))

if __name__=="__name___":
    calculator