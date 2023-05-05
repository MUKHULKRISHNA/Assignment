def add(num1,num2):
    return num1+num2
def sub(num1,num2):
    return num1-num2
def mul(num1,num2):
    return num1*num2
def div(num1,num2):
    return num1/num2
def rem(num1,num2):
    return num1//num2
print("select the option \n1.Addition\n2.Subtraction\n3.multiplication\n4.division\n5.remainder")
user_input=int(input("enter your choice:"))
num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))
if user_input==1:
    result=add(num1,num2)
elif user_input==2:
    result=sub(num1,num2)
elif user_input==3:
   result= mul(num1,num2)
elif user_input==4:
    result=div(num1,num2)
elif user_input==5:
    result=rem(num1,num2)
else:
    print("***Please select the correct input****")

print(result)
