if __name__ == '__main__':
    '''  Task

You are given a string . 
Your task is to find out if the string  contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.

Input Format

A single line containing a string .

Constraints


Output Format

In the first line, print True if  has any alphanumeric characters. Otherwise, print False. 
In the second line, print True if  has any alphabetical characters. Otherwise, print False. 
In the third line, print True if  has any digits. Otherwise, print False. 
In the fourth line, print True if  has any lowercase characters. Otherwise, print False. 
In the fifth line, print True if  has any uppercase characters. Otherwise, print False.'''

    s = input()
    
    isAlphanumeric, isAlphabetical, isDigits, isLower, isUpper = (False, False, False, False, False)

    for c in s:
        if c.isalnum():
            isAlphanumeric = True
        if c.isalpha():
            isAlphabetical = True
        if c.isdigit():
            isDigits = True
        if c.islower():
            isLower = True
        if c.isupper():
            isUpper = True
   
    print(isAlphanumeric)
    print(isAlphabetical)
    print(isDigits)
    print(isLower)
    print(isUpper)
