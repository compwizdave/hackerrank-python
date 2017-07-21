if __name__ == '__main__':
    N = int(input())
    output=[]
    for loop in range(N):
        cmd = input().split(' ')
        
        p1=0
        p2=0
        if len(cmd) == 2:
            p1 = int(cmd[1])
        if len(cmd) == 3:
            p1 = int(cmd[1])
            p2 = int(cmd[2])
            
        if cmd[0] == "insert":
            output.insert(p1,p2)
        elif cmd[0] == "print":
            print(output)
        elif cmd[0] == "remove":
            output.remove(p1)
        elif cmd[0] == "append":
            output.append(p1)
        elif cmd[0] == "pop":
            output.pop()
        elif cmd[0] == "reverse":
            output.reverse()
        elif cmd[0] == "sort":
            output.sort()
        else:
            print("error")
            
