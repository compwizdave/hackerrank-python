countSet1 = int(input())
Set1 = set(map(int, input().split())) 
countSet2 = int(input())
Set2 = set(map(int, input().split()))

print(len(Set1.intersection(Set2)))
