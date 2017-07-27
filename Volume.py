from time import sleep

print("Hey there bro.")
sleep(2)

#setup
liter_per_gallon = 3.78541

#input
print('How many gallons?')
gallons = float(input())

#transform
liters = liter_per_gallon * gallons

#output
print(str(gallons) + ' gallons is ' + str(liters) + ' liters. ')
