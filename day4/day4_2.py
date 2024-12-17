import re

def read_input():
    with open('input4.txt') as f:
        return f.readlines()

def listToMatrix(lines):
    return [list(line.strip()) for line in lines]

def findX_Mas(matrix):
    matches=[]
    for i in range(1,len(matrix)-1):
        for j in range(1,len(matrix[0])-1):
            row = matrix[i-1][j-1] + matrix[i][j] + matrix[i+1][j+1]
            row2 = matrix[i-1][j+1] + matrix[i][j] + matrix[i+1][j-1]
            print(row)
            print(row2)
            if (row == 'MAS' or row == 'SAM') and (row2 == 'MAS'  or row2 == 'SAM'):
                matches.append(i)
    return matches

def main():
    lines = read_input()
    matrix = listToMatrix(lines)
    print(len(findX_Mas(matrix)))

if __name__ == '__main__':
    main()