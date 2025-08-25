'''Coffeeeeee'''
def main():
    a = float(input()) # ราคาเเก้วละ a บาท
    b = float(input()) # เเก้วที่ 2 เป็นต้นไป ส่วนลดเเก้วละ b %
    c = float(input()) # ลด c % หากซื้อครบอย่างน้อย d บาท
    d = float(input()) # ลด c % หากซื้อครบอย่างน้อย d บาท
    e = float(input()) # ต้องการกาเเฟ e เเก้ว
    price1 = a + (e-1) * (a*(1-b/100)) if e > 0 else 0
    price_full = e*a
    price2 = price_full
    if price2 >= d:
        price2 = price_full * (1-c/100)
    
    if price1 < price2:
        print(1)
        print(f'{price1:.2f}')
    else:
        print(2)
        print(f'{price2:.2f}')
main()
