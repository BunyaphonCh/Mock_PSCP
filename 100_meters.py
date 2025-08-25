'''100 meters (2 star)'''
def main():
    '''bell gonna cooked'''
    gold_time = 9999999
    silver_time = 9999999
    broze_time = 9999999
    broze = 0
    silver = 0
    gold = 0
    for i in range(1,9):
        run_time = float(input()) # 9
        if run_time < gold_time:
            broze = silver # 2
            broze_time = silver_time
            silver = gold # 6
            silver_time = gold_time
            gold = i # 7
            gold_time = run_time
        elif run_time < silver_time:
            broze = silver # 2
            broze_time = silver_time
            silver = i # 7
            silver_time = run_time
        elif run_time < broze_time:
            broze = i
            broze_time = run_time
    print(f'{gold} {silver} {broze}')
main()
