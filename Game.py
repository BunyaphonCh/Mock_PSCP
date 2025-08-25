'''Game (1 star)'''
def main():
    '''Gambling'''
    A = int(input())
    B = int(input())
    Draw_A = A % 3
    Draw_B = B % 3
    if Draw_A == Draw_B:
        print(f'{Draw_A}')
    else:
        print('Error')

main()
