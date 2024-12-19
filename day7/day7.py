#solve with recursion
def parse_input():
    with open('input7.txt') as f:
        data = [line.strip() for line in f.readlines()]
    return data

def is_possible(operands, result):
    operators = ['+', '*']

def main():
    lines=parse_input()
    for line in lines:
        result, tmp = line.split(': ')
        operands = tmp.split(' ')



if __name__ == '__main__':
    main() 