koloda = [6,7,8,9,10,2,3,4,11] * 4
import random
random.shuffle(koloda)

print('Play games?')
count = 0

while True:
    choice = input('One more? 1/2_\n')
    if choice=='1':
        print('You have %d') 
        current = koloda.pop()
        print('You have %d' %current)
        count += current
        if count > 21:
            print('Sory, end games')
            break
        elif count == 21:
            print('You are Win 21!')
            break
        else:
            print('You have %d.' %count)
    elif choice == '2':
        print('You have  %d and you end game.' %count)
        break

print('By!')