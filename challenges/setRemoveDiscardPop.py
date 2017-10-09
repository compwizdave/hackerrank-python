n = int(input())
s = set(map(int, input().split())) 
n = int(input())
for p in range(n):
    command=input()
    if ' ' in command:
        (command,value) = command.split(' ')
    if command=="pop":
        s.pop()
    elif command=="remove":
        s.remove(int(value))
    elif command=="discard":
        s.discard(int(value))
print(sum(s))  
