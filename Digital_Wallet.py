'''เริ่มทำตอนนี้ยังทันไหม'''
def main():
    '''wtf'''
    name = input()
    thai = input().lower()
    local = input().lower()
    age = float(input())
    income = float(input())
    deposit = float(input())
    is_thai = (thai == 'yes') or (thai == 'true')
    is_local = (local == 'yes') or (local == 'true')
    valid = is_thai and is_local and age>=16 and deposit<=500000 and income<=840000
    if valid:
        print(f'Congratulations! {name} is qualified to receive a digital wallet amount of \
10,000 baht, sponsored by all taxpayers in Thailand.')
    else:
        print(f'Unfortunately, {name} is not qualified.')
main()
