with open('input_2.txt', 'r') as file:
    lines = file.readlines() 

data = [[int(num) for num in line.strip().split()] for line in lines]

safe = True
count = 0
for record in data:
    safe = True
    if not(record == sorted(record) or record == sorted(record, reverse=True)):
        safe = False
    else:
        for i in range(len(record) - 1):
            if abs(record[i] - record[i + 1]) > 3 or abs(record[i] - record[i + 1]) == 0:
                safe = False
                break
    if safe:
        count+=1

print(count)