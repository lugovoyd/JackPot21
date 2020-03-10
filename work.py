koloda = [6,7,8,9,10,2,3,4,11] * 4
import random
random.shuffle(koloda)

print('Play games?')
count = 0

while True:
    choice = input('One more? y/n\n')
    if choice=='y':
        current = koloda.pop()
        print('You have %d' %current)
        count += current
        if count > 21:
            print('Sory, end games, you count %d' %count)
            break
        elif count == 21:
            print('You are Win 21!')
            break
        else:
            print('Average %d.' %count)
    elif choice == 'n':
        print('You have  %d and you end game.' %count)
        break

print('Goodby!')