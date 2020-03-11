koloda = [6,7,8,9,10,2,3,4,11] * 4
import random 
random.shuffle(koloda)

print('Lets play?')
count = 0

while True:
    choice = input('One more? y/n\n')
    if choice=='y':
        current = koloda.pop()
        print('You have %d' %current)
        count += current
        if count > 21:
            print('Sory, end game, you count %d' %count)
            break
        elif count == 21:
            print('You won 21!')
            break
        else:
            print('Total %d.' %count)
    elif choice == 'n':
        print('You have %d and you finished the game.' %count)
        break

print('Goodbye!')
