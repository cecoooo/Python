import random
def discount():
    global dct
    global sum
    global lis2
    global lis3
    i = lis2.index(c)
    list_c = list(dct[lis3[i]])
    low_price = list_c[0]
    old_sum = low_price*list_c[1] 
    print(f"{lis3[i]}'s price before discount: ", low_price)
    low_price *= 0.9
    print(f"{lis3[i]}'s new price: ", low_price)
    new_sum = low_price*list_c[1]
    sum -= (old_sum - new_sum)
    list_c.pop(0)
    list_c.insert(0, low_price)
    dct[lis3[i]] = list_c
def new_product():
    global sum
    global dct
    global lis3
    total_price = 0
    lis1 = []
    goods = input('Enter goods to add: ')
    while goods in dct.keys():
        print('The goods already exist.')
        goods = input('Enter goods to add: ')
    lis3.append(goods)
    price = float(input('Enter price: '))
    lis1.append(price)
    quantuty = int(input('Enter quantity (int num): '))
    lis1.append(quantuty)
    total_price = price*quantuty
    sum += total_price
    lis1.append('0000')
    dct.update({goods:lis1})
dct = {}
lis2 = []
lis3 = []
sum = 0.0
while True:
    total_price = 0.0
    lis1 = []
    goods = input('Enter goods: ')
    while goods in dct.keys():
        print('The goods already exist.')
        goods = input('Enter goods to add: ')
    if goods == '':
        break
    lis3.append(goods)
    price = float(input('Enter price: '))
    lis1.append(price)
    quantuty = int(input('Enter quantity (int num): '))
    lis1.append(quantuty)
    total_price = price*quantuty
    sum += total_price
    code = random.randrange(1000,10000)
    while code in lis2:
        code = random.randrange(1000,10000)
    lis1.append(code)
    lis2.append(code)
    dct.update({goods:lis1})
print(dct)
print('Enter 0 to stop.')
while True:
    c = int(input('Enter 4-number code: '))
    if c == 0:
        break
    if c in lis2:
        discount()
    else:
        new_product()
print(dct)
print('Total sum: ', sum)
print('Average sum for a single product: ', sum/len(lis3))