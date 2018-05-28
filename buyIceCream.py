def buyIcecream(cash):
    s0 = 0
    s20 = 20
    s40 = 40
    state = s0

    if state == s0:
        if cash == 20:
            state = s20
        elif cash == 40:
            state = s40
        else:
            print('Kindly enter 20 or 40')
            #state == s0
    elif state == s20:
        if cash == 20:
            state = s40
        elif cash == 40:
            state = s60
        else:
            print('Kindly enter 20 or 40')
            #state == s20
    elif state == s40:
        if cash == 20:
            state = s60
        elif cash == 40:
            state = s60
        else:
            print('Kindly enter 20 or 40')
            #state == s40
    elif state == s60:
        print ('success')

counter = 0
s60 = 60

while counter < s60:
    amount = input('Enter cash in denominations of 20 or 40.\n')
    buyIcecream(int(amount))
    counter = counter + int(amount)
    if counter > s60:
        change = counter-60
        print ('Your change is ' + str(change) + ' Kshs')



print ('success')


