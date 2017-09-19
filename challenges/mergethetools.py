def merge_the_tools(string, k):
    # your code goes here
    word={}
    for split in range(0,len(string),k):
        word=[]
        for p in range(split,split + k):
            if string[p] not in word:
                word.append(string[p])
        print(''.join(word))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
