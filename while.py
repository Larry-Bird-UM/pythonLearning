number = 100
running = True

while running:
    guess = int(raw_input('666:'))
    if guess == number:
        print 'Congratulations, you guessed it.'
        running = False
    elif guess < number:
        print 'No, it is a little higher that that'
    else:
        print 'No, it is a little lower that that'

else:
    print 'The while loop is over.'

print 'Done'

i = 0
for i in range(0,10,1):
    print i
    i = i + 1
    if i < 3:
        continue
    else:
        i = i - 10
else:
    print 'The loop is over'