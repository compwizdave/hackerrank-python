if __name__ == '__main__':

    '''
    Given the names and grades for each student in a Physics class of  students, 
    store them in a nested list and print the name(s) of any student(s) having
    the second lowest grade.

    Note: If there are multiple students with the same grade, order their names
    alphabetically and print each name on a new line.
    '''

    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.insert(0,[name,score])       
    
    #print(students)
    
    students.sort( key=lambda x: x[0] )
    students.sort( key=lambda x: x[1] )
    
    #print(students)
    
    lowest = students[0][1]
    second = students[-1][1]
    
    for pos in range(len(students)):
        if students[pos][1] > lowest and students[pos][1] < second:
            second = students[pos][1]
            
    #print(second)
    for pos in range(len(students)):
        if students[pos][1] == second:
            print(students[pos][0])


