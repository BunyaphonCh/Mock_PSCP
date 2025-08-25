'''Scientific Notation (3 star)'''
def main():
    '''let's goooo'''
    text = input().strip()
    if 'x 10^' in text:
        print(text)
        sign = ''
        if text[0] == '-':
            sign = text[0]
            text = text[1:]
        pos = text.find('x 10^')
        num = text[:pos].strip()
        power = text[pos+5:].strip()
        if '.' in num:
            dot_pos = num.find('.')
            digits = num.replace('.','')
        else:
            dot_pos = len(num)
            digits = num
        new_dot = dot_pos + power
        print(new_dot)

main()
