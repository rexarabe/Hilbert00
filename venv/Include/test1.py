import random
file_name = 'matrix.dat'
n = 10
with open(file_name, 'w')as file:
    #file.write(str(n)+'\n')
    for i in range(1,n):
        file.write(str(n) + '\n')
        for j in range(1,n):
            file.write(str(1/(i+j-1))+' ')


#Array's files

file_name = 'matrix.dat'
matrix=[]
with open(file_name, 'r') as file:
    n = int(file.readline())
    for i in range(n):
        line = file.readline().replace('\n','').strip()
        if line == '':
            break
        s = line.split(' ')
        row = []
        for j in range(len(s)):
            row.append(float(s[j]))
        matrix.append(row)

for i in range(len(matrix)):
    s=''
    for j in range(len(matrix[i])):
        s+=str(matrix[i])+''
    print(s)