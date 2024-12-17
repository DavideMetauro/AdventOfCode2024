#setX
#setY
#map(num, countNum)
#index[len(setX)]
def read_input():
    with open('input5.txt', 'r') as file:
        input_data = file.read().split('\n\n')
        part1 = input_data[0].strip().split()
        part2 = input_data[1].strip().split(',')
    return part1, part2

def create_comparison(part1):
    comparison = {}
    for pair in part1:
        num1, num2 = map(int, pair.split('|'))
        if num1 not in comparison:
            comparison[num1] = []
        comparison[num1].append(num2)
    return comparison

#return true if num1 is bigger than num2. Default is false (num1 is smaller than num2)
def compare(comparison, num1, num2):
    if num1 not in comparison:
        return False
    return True if num2 in comparison[num1] else False

'''
def create_sets(part1):
    setX = set()
    setY = set()

    for pair in part1:
        num1, num2 = map(int, pair.split('|'))
        setX.add(num1)
        setY.add(num2)
        
    print(setX)
    print(setY)
    return setX, setY
'''

if __name__ == '__main__':
    part1, part2 = read_input()
    print(create_comparison(part1))

    