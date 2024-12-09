clear=[]
quantity=[]
final=[]

def read_input():
    count = 0
    with open('input9_test.txt', 'r') as file:
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
    

def create_final():
    for i in range(len(quantity)-1):
        for j in range(quantity[i]):
            final.append(i)
        for j in range(clear[i]):
            final.append(None)
    for j in range(quantity[-1]):
        final.append(len(quantity)-1)



def check_sum():
    return sum([i*final[i] for i in range(len(final)) if final[i] is not None])

if __name__ == "__main__":
    read_input()
    create_final()
    rearrange()
    print(final)
    print(check_sum())


