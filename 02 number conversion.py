
def binary_to_decimal(binary_num):
    value = 0
    #find the number of digits and set it to n
    #run loop from n-1 to 0
    #value = value + (digit)*(power(2, n))

    b = 0b1111
    n = 4

    d1 = 1
    d2 = 1
    d3 = 1
    d4 = 1

    value1 = d1 * (2**0)
    print(value1)

    value2 = d2 * (2**1)
    print(value2)

    value3 = d3 * (2**2)
    print(value3)

    value4 = d4 * (2**3)
    print(value4)

    value = value1 + value2 + value3 + value4
    return value

def binary_to_hex(binary_num):
    value = 0
    return value

def binary_to_octal(binary_num):
    value = 0
    return value

def main():
    print(binary_to_decimal(0b1111))
    #print(binary_to_hex(0b1111))
    #print(binary_to_octal(0b1111)) 

main()