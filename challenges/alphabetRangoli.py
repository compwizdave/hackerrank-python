from itertools import chain

def print_rangoli(size):
    length=(size*2)+(size-1)*2-1
    for vpos in chain(range(size-1,0,-1),range(0,size,1)):
        line=''
        for hpos in chain(range(size - vpos-1,0,-1),range(0,size - vpos,1)):
            line = line + chr(ord('a')+vpos+hpos)+'-'    
        print(line[:length].center(length,'-'))                

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
