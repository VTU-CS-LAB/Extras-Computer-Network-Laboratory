def xor(a, b):
    y = int(a,2) ^ int(b,2)
    return '{0:b}'.format(y)
def divide(dividend, divisor):
    pick = len(divisor)
    temp = dividend[0:pick]
    while(pick < len(dividend)):
        if temp[0] == '1':
            # print(xor(divisor, temp), dividend[pick])
            temp = xor(divisor, temp) + dividend[pick]
        else:
            temp = xor('0' * pick, temp)+ dividend[pick]
        pick += 1
    if temp[0] == '1':
        temp = xor(divisor, temp)
    else:
        temp = xor('0' * pick, temp)
    return temp
def generate(message, generator):
    msgLen = len(message)
    gtrLen = len(generator)
    dividend = message + ("0" * (gtrLen - 1))
    remainder = divide(dividend, generator)
    return message + '0' * (gtrLen - 1 - len(remainder)) + remainder
def check(codeword, generator):
    if (divide(codeword, generator)) == '0':
        print("Verified.")
    else:
        print("Data Error.")

if __name__ == '__main__':
    generator = "1101" #CRC32
    message = "1001"
    print("Message:", message)
    print("Generator:", generator)
    cw = generate(message, generator)
    print("Codeword:", cw)
    print("---------------")
    print("1. Checking codeword with correct value {}:\n".format(cw))
    check(cw, generator)
    print("---------------")
    print("1. Checking codeword with incorrect value {}:\n".format(cw + '010'))
    check(cw + '010', generator)
