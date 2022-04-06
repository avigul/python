s = ''
prices = [57.8, 46.51, 97.3, 107.5, 51.33, 99.99, 89.07, 114.0, 78.40, 16.1, 86.70, 35.40]
for price in prices:
    price = int(price * 100)
    rub = price //100
    kop = price % 100
    i = str(rub) + ' руб ' + str(kop) + ' коп'
    if s == '':
        s = s + i
    else:
        s = s + ', ' + i
print(s)