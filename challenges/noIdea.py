if __name__ == '__main__':
    (n,m) =    map(int, input().split(' '))
    arr = list(map(int, input().split(' ')))
    a =    set(map(int, input().split(' ')))
    b =    set(map(int, input().split(' ')))
    
    happy=0
    for p in arr:
        if p in a:
            happy+=1
        elif p in b:
            happy-=1
    print(happy)
