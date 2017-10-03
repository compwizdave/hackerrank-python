if __name__ == '__main__':
    n = int(input())
    s=set('')
    for l in range(n):
        i=input()
        s.add(i)
    print(len(s))
