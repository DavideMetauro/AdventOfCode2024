import time 

def parse_input():
    with open('input7.txt') as f:
        data = [line.strip() for line in f.readlines()]
    return data

def is_possible_1(operands, result, i, total):
    if i == len(operands):
        return total == result
    
    if is_possible_1(operands, result, i + 1, total + operands[i]) or \
        is_possible_1(operands, result, i + 1, total * operands[i]):
        return True

    return False

def is_possible_2(operands, result, i, total):
    if i == len(operands):
        return total == result
    
    if is_possible_2(operands, result, i + 1, total + operands[i]) or \
        is_possible_2(operands, result, i + 1, total * operands[i]) or \
        is_possible_2(operands, result, i + 1, int(str(total) + str(operands[i]))):
        return True

    return False


def main():
    count=0
    count2 = 0
    lines=parse_input()
    for line in lines:
        result, tmp = line.split(': ')
        operands = list(map(int, tmp.split(' ')))
        if is_possible_1(operands, int(result), 1, operands[0]):
            count += int(result)
        if is_possible_2(operands, int(result), 1, operands[0]):
            count2 += int(result)
    print('Part 1:', count)
    print('Part 2:', count2)

if __name__ == '__main__':
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))