'''Digital Wallet (0 star)'''
def main():
    '''you can get that?'''
    name = input()
    thai = input().lower()
    regist = input().lower()
    age = float(input())
    income = float(input())
    deposit = float(input())
    is_thai = (thai == 'true') or (thai == 'yes')
    is_regist = (regist == 'true') or (regist == 'yes')
    if is_thai and is_regist and age >= 16 and income <= 840000 and deposit <= 500000:
        print(f'Congratulations! {name} is qualified to receive a digital wallet amount of \
10,000 baht, sponsored by all taxpayers in Thailand.')
    else:
        print(f'Unfortunately, {name}')
main()
