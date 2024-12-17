import re

def read_input():
    with open('input4.txt') as f:
        return f.readlines()

def listToMatrix(lines):
    return [list(line.strip()) for line in lines]

def findXmas(strings):
    matches=[]
    for line in strings:
        matches.extend(re.findall(r'XMAS', line))
    for line in strings:
        matches.extend(re.findall(r'SAMX', line))
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

'''
def transpose(matrix):
    matrixT = [['' for i in range(len(matrix))] for j in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrixT[j][i] = matrix[i][j]
    return matrixT
'''

def main():
    count=0
    lines = read_input()
    matrix = listToMatrix(lines)
    #matrixT=transpose(matrix)

    count+=len(findXmas(lines))

    #transposed matrix
    column_strings = [''.join(row) for row in zip(*matrix)]
    count+=len(findXmas(column_strings))
    
    #from right to left
    diagonal_strings = flatten_diagonally(matrix)
    count += len(findXmas(diagonal_strings))

    #from left to right
    diagonal_reverse = flatten_diagonally_reverse(matrix)
    count += len(findXmas(diagonal_reverse))
    print(count)
    

if __name__ == '__main__':
    main()