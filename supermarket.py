from datetime import datetime
name = input('enter user name:')

#items list
lists = '''
        ITEMS        PRICES
        =======================
        rice        rs 50/kg
        eggs        rs 60/doz
        banana      rs 50/doz
        sugar       rs 80/kg
        oil         rs 110/kg
        soap        rs 47/each
        detergent   rs 99/each
        sanetizer   rs 20/each
        mask        rs 20/each
        chocolate   rs 99/each
        biscuits    rs 20/each
        maggie      rs 80/pack
        salt        rs 18/each
        paste       rs 49/each
        '''

#declaration
price =0
pricelist = []
totalprice = 0
finalprice = 0
plist = []
qlist = []
ilist = []

items = {
    'rice':50,
    'eggs':6,
    'banana':5,
    'sugar':80,
    'oil':110,
    'soap':47,
    'detergent':99,
    'sanetizer':20,
    'mask':20,
    'chocolate':99,
    'biscuits':20,
    'maggie':80,
    'salt':18,
    'paste':49
}
option = int(input('enter 1 to display list of items:'))

if option==1:
    print(lists)

for i in range(len(items)):
    inp1 = int(input('enter 1 to buy items or enter 2 to exit:'))
    if inp1==2:
        break
    if inp1==1:
        item = input('enter the item to want to buy:')
        quantity = int(input('enter the quantity:'))
        if item in items.keys():
            price = quantity * (items[item])
            totalprice+=price
            plist.append(price)
            qlist.append(quantity)
            ilist.append(item)
            gst = (totalprice*5)/100
            finalprice = gst+totalprice
        else:
            print('enter the item present the mentioned list')

    else:
        print('enter the valid input')

    inp = input('can i generate the bill enter yes or no:')
    if inp=='yes':
        if finalprice!=0:
            print(60 * '=')
            print(15*' '+'welcome to sata market'+15*' ')
            print(60*'=')
            print('sr.no'+10*' '+'items'+10*' '+'quantity'+10*' '+'price'+10*' ')

            for i in range(len(plist)):
                print(i+1,10*' ',ilist[i],10*' ',qlist[i],10*' ',plist[i],10*' ')
            print(60*'-')
            print('total price:',totalprice)
            print('GST:',gst)
            print(60*'=')
            print('FINAL AMOUNT:',finalprice)
            print(20*'*'+'THANKYOU VISIT AGAIN'+20*'*')



