'''Post'''
def main():
    '''waoo'''
    n = int(input())
    m = int(input())
    en = 0
    pack = 0
    price_en = 0
    price_pack = 0
    special_en = 13*n
    special_pack = 15*m
    for _ in range(n):
        w_en = float(input())
        en += w_en
    for _ in range(m):
        w_pack = float(input())
        pack += w_pack
    if w_en > 1000:
        price_en = 68
    elif w_en > 500:
        price_en = 48
    elif w_en > 250:
        price_en = 33
    elif w_en > 100:
        price_en = 28
    elif w_en > 20:
        price_en = 23
    elif w_en > 10:
        price_en = 18
    else:
        price_en = 16
    if w_pack > 1000:
        price_pack = 70
    elif w_pack > 500:
        price_pack = 55
    else:
        price_pack = 45
    print(price_en + special_en + price_pack + special_pack)
main()
