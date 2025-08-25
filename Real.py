'''Real (2 star)'''
def main():
    '''it okay'''
    result = ''
    isError = False
    for i in range(3):
        a,b,c,d,e,f,g,dp = input(),input(),input(),input(),input(),input(),input(),input()
        data = (a+b+c+d+e+f+g).replace('on','1').replace('off','0')
        num0,num1,num2,num3,num4,num5 = '1111110','0110000','1101101','1111001','0110011','1011011'
        num6,num7,num8,num9 = '1011111','1110000','1111111','1111011'
        if data == num0:
            result += '0'
        elif data == num1:
            result += '1'
        elif data == num2:
            result += '2'
        elif data == num3:
            result += '3'
        elif data == num4:
            result += '4'
        elif data == num5:
            result += '5'
        elif data == num6:
            result += '6'
        elif data == num7:
            result += '7'
        elif data == num8:
            result += '8'
        elif data == num9:
            result += '9'
        else:
            isError = True
        if dp == 'on':
            result += '.'
            if result.count('.') > 1:
                isError = True
    if isError:
        print('Error')
    else:
        print(f'{float(result):.2f}')
main()
