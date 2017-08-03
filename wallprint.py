from time import sleep

print("Hello.")
sleep(2)

#setup


#input
print('what is the width if the wall?')
width = float(input())
print('What is the Height of the wall?')
lenght = float(input())
print('How much does 1 gallon of print cost?')
cost = float(input())
#transform
square_feet = width * lenght
gallons = square_feet / 400
total_cost = gallons * cost

#output
print('5 seconds are need for me to calculate')
sleep(1)
print('What color is the paint?')
name = str(input())
print('That is a cool color')
sleep(5)
print('The total square feet is '+ str(square_feet))
print('The total cost is $'+ str(total_cost))
