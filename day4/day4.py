import re

def read_input():
    with open('input4_test.txt') as f:
        return f.readlines()

def listToMatrix(lines):
    return [list(line) for line in lines]

def findXmas(strings):
    matches=[]
    for line in strings:
        match = re.findall(r'XMAS', line)
        if match:
            for m in match:
               matches.append(m)
    for line in strings:
        match = re.findall(r'SAMX', line)
        if match:
            for m in match:
               matches.append(m)
    return matches

def flatten_diagonally(matrix):
    diagonals = []
    if not matrix or not matrix[0]:
        return diagonals
    for i in range(len(matrix) + len(matrix[0]) - 1):
        diagonal = []
        for j in range(max(0, i - len(matrix[0]) + 1), min(len(matrix), i + 1)):
            if i - j < len(matrix[j]):
                diagonal.append(matrix[j][i - j])
        diagonals.append(''.join(diagonal))
    return diagonals

def flatten_diagonally_reverse(matrix):
    diagonals = []
    if not matrix or not matrix[0]:
        return diagonals
    for i in range(len(matrix) + len(matrix[0]) - 1):
        diagonal = []
        for j in range(max(0, i - len(matrix[0]) + 1), min(len(matrix), i + 1)):
            if i - j < len(matrix[j]):
                diagonal.append(matrix[j][len(matrix[0]) - 1 - (i - j)])
        diagonals.append(''.join(diagonal))
    return diagonals

def transpose(matrix):
    matrixT = [['' for i in range(len(matrix))] for j in range(len(matrix[0]))]
    print(matrixT(len(matrix[0])))
    print(len(matrix[0]))
    print(len(matrixT[0]))
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrixT[j][i] = matrix[i][j]
    return matrixT


def main():
    count=0
    lines = read_input()
    matrix = listToMatrix(lines)
    matrixT=transpose(matrix)

    #print(matrix)
    #print(matrixT)

    count+=len(findXmas(lines))
    #print(findXmas(lines))
    print(count)

    column_strings = [''.join(row) for row in zip(*matrixT)]
    #print(column_strings)
    count+=len(findXmas(column_strings))
    print(count)
    
    diagonal_strings = flatten_diagonally(matrix)
    print(diagonal_strings)
    count += len(findXmas(diagonal_strings))
    print(count)

    diagonal_reverse = flatten_diagonally_reverse(matrix)
    print(diagonal_reverse)
    count += len(findXmas(diagonal_reverse))
    print(count)
    

if __name__ == '__main__':
    main()