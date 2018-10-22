import math

if __name__ == '__main__':
    p = 3
    q = 7
    n = p * q
    phi = (p - 1)*(q - 1)
    e = 3
    while(e < phi):
        if math.gcd(e, phi) == 1:
            break
        else:
            e += 1
    k = 2
    d = (1 + (k * phi)) / e

    while(True):
        print("1. Encrypt Message 2. Decrypt Message")
        ch = int(input())
        if ch == 1:
            message = int(input("Enter integer: "))
            print("Encrypted Data: {}".format((message ** e) % n))
        elif ch == 2:
            message = int(input("Enter encypted integer: "))
            print("Decrypted Data: {}".format((message ** d) % n))

#only works till integers upto 20
