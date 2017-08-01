if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    biggest = -101
    secondBiggest = -101
    for p in arr:
        if p > biggest:
            secondBiggest = biggest
            biggest = p
        if p > secondBiggest and p < biggest:
            secondBiggest = p
        #print(p, biggest, secondBiggest)
            
    print(secondBiggest)
