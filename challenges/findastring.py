'''
In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string.
'''
def count_substring(string, sub_string):
    count=0
    i=0
    while i < len(string):
        isFound = string.find(sub_string,i,len(string))
        if isFound != -1:
           count+=1
           i=isFound
        i+=1   
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
