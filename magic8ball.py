"""magic 8 ball"""
from random import randint

print('Hi, whom speaks to the magic 8 ball of FORTUNE!!')
name = input()


r = randint(1,9)

if 1 == r:
    print('You will die believing in what you did was right.')
elif 2 == r:
    print('A flying raccon will hug you then punch you in 1 year.')
elif 3 == r:
    print('Um your Rick, you pay me $5 now')
elif 4 == r:
    print('A loved one is of utmost importance at this time.')
elif 5 == r:
    print('Illerate software engineers will punch you in exactly 10 years.')
elif 6 == r:
    print('YOUR PICKLE RIIIIIIIIIIIICCCCCCCCCCKKKKKK!!!!!!!!')
elif 7 == r:
    print('You have an ambitious nature and may make a name for yourself.')
elif 8 == r:
    print('Rick is real ')
elif 9 == r:
    print('Youre missing the point Morty. Why would he drive a smaller toaster with wheels? I mean, does your car look like a smaller version of your house? No.')
