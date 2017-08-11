print('A number between 1 and 99: ')
num = int(input())

tens = num // 10
ones = num % 10

if tens == 9:
    ones = print('ninety-one')
elif ones == 8:
    print('eight')
elif ones == 7:
     print('seven')
elif ones == 6:
     print('six')
elif ones == 5:
     print('five')
elif ones == 4:
     print('four')
elif ones == 3:
     print('three')
elif ones == 2:
     print('two')
elif ones == 1:
     print('one')
