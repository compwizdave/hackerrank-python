def minion_game(string):
    # your code goes here
    kevinWords = {}
    stuartWords = {}
    
    vowel='AEIOU'
    length=len(string)
    
    for outsideScan in range(length):
        startLetter=string[outsideScan]
        for insideScan in range(1,length+1-outsideScan):
            subWord=string[outsideScan:outsideScan+insideScan]
            print(subWord)
            
            count = 0
            pos = 0
            isFound=string.find(subWord,pos)
            while(isFound != -1):
                count = count + 1
                pos = isFound + 1
                isFound=string.find(subWord,pos)
            print(count)
            
            if subWord[0] in vowel:
                kevinWords[subWord] = count
            else:
                stuartWords[subWord] = count
    
    stuartCount=sum(stuartWords.values())
    kevinCount=sum(kevinWords.values())
    
    if stuartCount == kevinCount:
        print('Draw')
    elif stuartCount > kevinCount:
        print('Stuart',stuartCount)
    else:
        print('Kevin',kevinCount)

if __name__ == '__main__':
    s = input('input:')
    minion_game(s)

