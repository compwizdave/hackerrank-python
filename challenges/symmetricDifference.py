def symmetricDifference(array1, array2):
    # your code goes here
    s1 = set(array1)
    s2 = set(array2)
    for n in sorted(list(s1.symmetric_difference(s2))):
        print(n)

if __name__ == '__main__':
    n1 = int(input())
    arr1 = list(map(int, input().split()))
    n2 = int(input())
    arr2 = list(map(int, input().split()))
    
    result = symmetricDifference(arr1,arr2)
