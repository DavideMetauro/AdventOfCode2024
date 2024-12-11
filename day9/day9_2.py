free_spaces=[]
occupied_spaces=[]
final=[]

def read_input():
    count = 0
    with open('input9_test.txt', 'r') as file:
        while True:
            c = file.read(1)
            if not c:
                break
            if count%2==0:
                occupied_spaces.append(int(c))
            else:
                free_spaces.append(int(c))
            count+=1

def count_clear():
    index=0
    free_dict = {}
    for i in range(len(final)):
        if final[i] is None and final[i-1] is not None:
            index = i
            if index in free_dict:
                free_dict[index] += 1
            else:
                free_dict[index] = 1
            print(free_dict)


def create_final():
    for i in range(len(occupied_spaces)-1):
        final.extend(i for j in range(occupied_spaces[i]))
        final.extend(None for j in range(free_spaces[i]))
    final.extend(len(occupied_spaces)-1 for j in range(occupied_spaces[-1]))



def check_sum():
    return sum([i*final[i] for i in range(len(final)) if final[i] is not None])

if __name__ == "__main__":
    read_input()
    create_final()
    print(final)
    count_clear()
    #rearrange()
    #print(check_sum())


