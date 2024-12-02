# Read the input file
with open('input_1.txt', 'r') as file:
    lines = file.readlines()

# Initialize the lists
first_elements = []
second_elements = []

# Process each line
for line in lines:
    parts = line.strip().split('   ')  # Split by 3 spaces
    if len(parts) == 2:
        first_elements.append(parts[0])
        second_elements.append(parts[1])

first_elements.sort()
second_elements.sort()

total_distance = 0
for i in range(len(first_elements)):
    distance = abs(int(first_elements[i]) - int(second_elements[i]))
    total_distance += distance 

# primo risultato
print(total_distance)

count = 0
distance = 0
for element in first_elements:
    for element2 in second_elements:
        if element == element2:
            count += 1
    distance += int(element) * count
    count = 0

# secondo risultato
print(distance)