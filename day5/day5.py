from functools import cmp_to_key

comparison = {}

def read_input():
    with open('input5.txt', 'r') as file:
        input_data = file.read().split('\n\n')
        part1 = input_data[0].strip().split()
        part2 = input_data[1].strip().split()
    return part1, part2

def create_comparison(part1):
    for pair in part1:
        num1, num2 = map(int, pair.split('|'))
        if num1 not in comparison:
            comparison[num1] = []
        comparison[num1].append(num2)

#return true if num1 is bigger (printed before) than num2. Default is false (num1 is smaller than num2)
def compare(num1, num2):
    if num1 == num2 :
        return 0
    return 1 if num1 in comparison and num2 in comparison[num1] else -1

def main():
    correct = 0
    wrong = 0
    part1, part2 = read_input()
    create_comparison(part1)
    for line in part2:
        num= list(map(int, line.split(',')))
        num_sorted = sorted(num, key=cmp_to_key(compare), reverse=True)
        if num == num_sorted:
            correct += num[len(num) // 2 ]
        else:
            wrong += num_sorted[len(num_sorted) // 2]
    print("part1: ",correct)
    print("part2: ",wrong)

if __name__ == '__main__':
    main()   