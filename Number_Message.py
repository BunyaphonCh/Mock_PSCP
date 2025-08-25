'''Number Message (1 star)'''
def main():
    '''decode it dude'''
    text = input().upper()
    result = ''
    new_text = text.replace('12','R').replace('13','B').replace('1','I').replace('3','E')
    new_text = new_text.replace('4','A').replace('5','S').replace('0','O')
    ignore = '123456789'
    for i in ignore:
        new_text = new_text.replace(i,'')
    print(new_text)
main()
