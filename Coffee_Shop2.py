'''Coffee Shop (0 star)'''
def main():
    '''what promotion ฉงน should choose?'''
    a = float(input())
    b = float(input())
    c = float(input())
    d = float(input())
    e = int(input())
    price_1 = a
    price_2 = a
    price_all = a*e
    if e > 1:
        discount = ((b/100)*a)
        price_discount = a - discount
        price_1 = a + (price_discount * (e-1))
    if price_all >= d:
        discount2 = (c/100)*price_all
        price_2 = price_all - discount2
    if price_1 < price_2:
        print(1)
        print(f'{price_1:.2f}')
    elif price_2 < price_1:
        print(2)
        print(f'{price_2:.2f}')
    else:
        print(2)
        print(f'{price_2:.2f}')
main()
