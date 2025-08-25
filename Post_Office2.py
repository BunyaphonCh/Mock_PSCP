'''Post Office (1 star)'''
def main():
    '''what cost'''
    n = int(input())
    m = int(input())
    destination_n = n * 13
    destination_m = m * 15
    sum_n = 0
    sum_m = 0
    for _ in range(n):
        g = float(input())
        if g > 1000:
            sum_n += 68
        elif g > 500:
            sum_n += 48
        elif g > 250:
            sum_n += 33
        elif g > 100:
            sum_n += 28
        elif g > 20:
            sum_n += 23
        elif g > 10:
            sum_n += 18
        else:
            sum_n += 16
    for _ in range(m):
        g = float(input())
        if g > 1000:
            sum_m += 70
        elif g > 500:
            sum_m += 55
        else:
            sum_m += 45
    print(sum_n+destination_n+sum_m+destination_m)

main()
