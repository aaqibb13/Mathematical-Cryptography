import math
def eea(a, b):
    s, s_p, t, t_p = 0, 1, 1, 0
    r = int(b) 
    r_p = int(a)
    while r != 0:
        q = math.floor(r_p/r)
        r_p, r = r, r_p - q*r
        s_p, s = s, s_p - q*s
        t_p, t = t, t_p - q*t
    d, x, y = r_p, t, s

    print(f'The multiplicative inverse is {s_p}')

if __name__ == '__main__':
    a = input('Enter the first number:\n')
    b = input('Enter the first number:\n')
    eea(a, b)