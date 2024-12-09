clear=[]
quantity=[]
final=[]

def read_input():
    count = 0
    with open('input9.txt', 'r') as file:
        while True:
            c = file.read(1)
            if not c:
                break
            if count%2==0:
                quantity.append(int(c))
            else:
                clear.append(int(c))
            #print(c, end='')
            count+=1

def rearrange():
    last_index = len(quantity)-1
    for i in range(len(quantity)):
        for j in range(quantity[i]):
            final.append(i)
        quantity[i] = 0
        for j in range(clear[i]):
            final.append(last_index)
            quantity[last_index] -= 1
            if quantity[last_index] == 0:
                last_index -= 1
            if last_index == i:
                break
        if last_index == i:
            break


def check_sum():
    sum=0
    for i in range(len(final)):
        sum+=final[i]*i
    return sum

if __name__ == "__main__":
    read_input()
    rearrange()
    print(check_sum())


