def bineuclid(a, b):
    g = 1
    """Remove the powers of two from the gcd"""
    while (a%2 == 0) and (b%2 == 0):
        a = a/2
        b = b/2
        g = 2*g
    """Atleast one of a or b is odd now"""
    while a != 0:
        while a%2 == 0:
            a = a/2
        while b%2 == 0:
            b = b/2
        """Now both a and b are odd"""
        if a >= b:
            a = (a-b)/2
        else:
            b = (b-a)/2
    print(g*b)


if __name__ == '__main__':
    a = int(input('Enter the first number:\n'))
    b = int(input('Enter the second number:\n'))
    bineuclid(a, b)