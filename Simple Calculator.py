# Function To Add 2 Numbers

def add(num1,num2):
    return num1+num2

# Function To Subtract 2 numbers:

def subtract(num1,num2):
    return num1-num2

# Function to Multiply 2 numbers
def multiply(num1,num2):
     return num1*num2

# Function to Divide 2 numbers 
def divide(num1,num2):
     return num1/num2
 

print("Please select Operation -\n" \
      "1. Add \n"\
      "2. Subtract\n"\
      "3. Multiply\n"\
      "4. Divide\n"\)

# Take Input FromThe User

select = int(input("Select Operations From 1. 2. 3. 4. :"))
 
number_1 = int(input("Enter First Number:"))
number_2 = int(input("Enter Second Number"))
 
if select == 1:
     print(number_1," + ",number_2,"=",
           add(number_1,number2))
elif select == 2:
    print(number_1,"-",number_2, "="
          subtract(number_1,number_2))
elif select == 3:
    print(number_1, "*" , number_2, "="
           multiply(number_1,number_2))
elif select == 4:
    print(number_1, "/" , number_2, "="
          divide(number_1,number_2))

else:
    print("Invalid Input")

    