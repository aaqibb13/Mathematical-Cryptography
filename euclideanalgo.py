def gcd(n, a):
    while n != 0:
        if a > n:
            n, a = a, n
        else:
            pass
        n = n%a
        gcd(n, a)
        print(f'The gcd is {a}')

if __name__ == '__main__':
    n = int(input('Enter the first number\t'))
    a = int(input('Enter the second number\t'))
    gcd(n, a)