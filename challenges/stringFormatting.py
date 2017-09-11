def print_formatted(number):
    '''Given an integer, , print the following values for each integer  from  to :

Decimal
Octal
Hexadecimal (capitalized)
Binary
The four values must be printed on a single line in the order specified above for each  from  to . Each value should be space-padded to match the width of the binary value of .'''
    width = len("{0:b}".format(number))+1 
    for num in range(1,number+1):
        print('{0:{width}{base}}'.format(num, width=width-1, base='d'),end='')
        for base in 'oXb':
            print('{0:{width}{base}}'.format(num, width=width, base=base),end='')
        print()

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
