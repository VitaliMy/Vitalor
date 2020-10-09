s = True
while  s is True:
    action = input('1. Add matrices\n'+ '2. Multiply matrix by a constant\n' +'3. Multiply matrices\n'\
                   +'4. Transpose matrix\n'+ '5. Calculate a determinant\n' + '6. Inverse matrix\n'+'0. Exit\n'+ 'Your coice: ')
    print()
    if action == '1':
        A = []
        x, j = list(map(int,input('Enter size of first matrix: ').split()))
        print('Enter first matrix:')
        for i in range (x):
            a=list(map(float,input().split()))
            A.append(a)
        
        B = []
        b, c = list(map(int,input('Enter size of second matrix: ').split()))
        print('Enter second matrix:')
        for i in range (b):
            y=list(map(float,input().split()))
            B.append(y)
        if len(A) != len(B) or len(A[0]) != len(B[0]):
            print('The operation cannot be performed.')
        else:
            C = [[0 for j in range(len(B[0]))] for x in range(len(A))] 
            for i in range(len(A)):
                for j in range(len(B[0])):
                    C[i][j] = A[i][j] + B[i][j]
        print('The result is:')
        for i in range(len(C)):
            for j in range(len(C[i])):
                print(C[i][j], end=' ')
            print()
        print()
        del (A[i][j], B[i][j], C[i][j])
       
    elif action == '2':
        x, j = list(map(int,input('Enter size of  matrix: ').split()))
        b =[]
        print('Enter matrix:')
        for i in range (x):
            a=list(map(float,input().split()))
            b.append(a)
        
        n = float(input('Enter constant: '))
        print('The result is:')
        for i in b:
            for y in i:
                print(float(y*n), end=' ')
            print()
        print()
        
    if action == '3':
        A = []
        
        x, y = list(map(int,input('Enter size of first matrix: ').split()))
        print('Enter first matrix:')
        for i in range (x):
            a=list(map(float,input().split()))
            A.append(a)
       
        B = []
        
        b,c = list(map(int,input('Enter size of second matrix: ').split()))
        print('Enter second matrix:')
        for i in range (b):
            y=list(map(float,input().split()))
            B.append(y)
       
        C = [[0 for j in range(len(B[0]))] for x in range(len(A))]
        
        for i in range(len(A)):
            for j in range(len(B[0])):
                for k in range(len(A[0])):
                    C[i][j] += A[i][k] * B[k][j]
        print('The result is:')
        for i in range(len(C)):
            for j in range(len(C[i])):
                print(C[i][j], end=' ')
            print()
        print()
        del (A[i][k])
        del (B[k][j])
        del (C[i][j])
        
    elif action == '4':
        choice = input('1. Main diagonal\n'+'2. Side diagonal\n'+ '3. Vertical line\n'
              +'4. Horizontal line\n'+ 'Your coice: ')
        
        if choice == '1':
            
            row,col = map(int,input('Enter matrix size:: ').split())
            matrix = list()
            print('Enter matrix:')
            for i in range(row):
                r = list(map(int,input().split()))
                matrix.append(r)
            trans = [[0 for y in range(row)]for x in range(col)]

            for i in range(len(matrix[0])):
                for j in range(len(matrix)):
                    trans[i][j] = matrix[j][i]
            print('The result is:')       
            for i in range(len(trans)):
                for j in range(len(trans[0])):
                    print(trans[i][j],end=' ')
                print(' ')
            print()
            del (matrix[i][j], trans[i][j])
             
        elif choice == '2':
            
            row,col = list(map(int,input('Enter matrix size: ').split()))
            B =[]
            print('Enter matrix:')
            for i in range (row):
                a=list(map(float,input().split()))
                B.append(a)
            a = len(B)
            a -=1
            b = len(B[0])
            b -=1
            for j in range(int(b), -1, -1):
               for i in range(int(a), -1, -1):
                   print(B[i][j],end=' ')
               print(' ')
            print()
            del (B[i][j])
            
        elif choice == '3':
            
            row,col = list(map(int,input('Enter matrix size: ').split()))
            B =[]
            print('Enter matrix:')
            for i in range (row):
                a=list(map(float,input().split()))
                B.append(a)
         
            a = len(B)
            a -=1
            b = len(B[0])
            b -=1

            B.reverse()
            print('The result is:') 
            for i in range(int(a), -1, -1):
               for j in range(int(b), -1, -1):
                  print(B[i][j],end=' ')
               print(' ')
            print()

            del (B[i][j])    
                 
        elif choice == '4':
            row,col = list(map(int,input('Enter matrix size: ').split()))
            B =[]
            print('Enter matrix:')
            for i in range (row):
                a=list(map(float,input().split()))
                B.append(a)

            B.reverse()

            print('The result is:')       
            for i in range(len(B)):
                for j in range(len(B[0])):
                    print(B[i][j],end=' ')
                print(' ')

            print()
            del (B[i][j])
            
    elif action == '5':
        
        def det2(matrix):
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
 
        def minor(matrix, i, j):
            tmp = [row for k, row in enumerate(matrix) if k != i]
            tmp = [col for k, col in enumerate(zip(*tmp)) if k != j]
            return tmp
 
        def determinant(matrix):
            size = len(matrix)
            if size == 1:
                a = sum(matrix[0])
                return a
            elif size == 2:
                return det2(matrix)
 
            return sum((-1) ** j * matrix[0][j] * determinant(minor(matrix, 0, j))
                for j in range(size))

        row,col = list(map(int,input('Enter matrix size: ').split()))
        matrix =[]
        print('Enter matrix:')
        for i in range (row):
            a=list(map(float,input().split()))
            matrix.append(a)
        print('The result is:')
        print(determinant(matrix))
        print()
        
    elif action == '6':
        
        import copy
        import math

        def minor(A, i, j):
            M = copy.deepcopy(A)
            del M[i]
            for i in range(len(A[0]) - 1):
                del M[i][j]
            return M
 
 
        def det(A):
            m = len(A)
            n = len(A[0])
            if m != n:
                return None
            if n == 1:
                return A[0][0]
            signum = 1
            determinant = 0
 
            for j in range(n):
                determinant += A[0][j] * signum * det(minor(A, 0, j))
                signum *= -1
            return determinant
        
        def transposeMatrix(A):
            return list(map(list,zip(*A)))


        print('Enter matrix:')
        A = []
        row,col = list(map(int,input('Enter matrix size: ').split()))
        for i in range (row):
            a=list(map(float,input().split()))
            A.append(a)
        
        result = [[0 for x in range(row)] for y in range(col)]
        if det(A) != 0:    
            result = [[0 for x in range(row)] for y in range(col)]
            for i in range(len(A)):
                for j in range(len(A[0])):
                    tmp = minor(A, j, i)
                    if (i +j) % 2 == 1:
                        rez = -1 * det(tmp) / det(A)
                        if rez == 0.0 or rez == (-0.0):
                           rez = math.trunc(rez * 100) / 100                    
                        else:
                            rez = math.trunc(rez * 100) / 100
                            result[i][j]= rez
                    else:
                        rez  = 1 * det(tmp) / det(A)               
                        if rez == 0.0 or rez == (-0.0):
                            rez = math.trunc(rez * 100) / 100
                    
                        else:
                            rez = math.trunc(rez * 100) / 100
                            result[i][j]= rez 

                    
    
            print('The result is:')
            for i in range(len( result)):
                for j in range(len( result[i])):
                    print( result[i][j], end=' ')
                print()
            print()   
        
        else:  
            print("This matrix doesn't have an inverse")
            print()
        
    elif action == '0':
        print()
        s = False
        
