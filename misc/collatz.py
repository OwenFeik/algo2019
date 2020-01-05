
i=0
while True:
    i+=1
    j=i
    while j>1:
        if not j%2:
            j/=2
        else:
            j*=3
            j+=1
    
    if j==1:
        if not i%1000:
            print(f'Up to {i} all work!')
    else:
        print(f'{i} doesn\'t work! Take that Collatz!')
        break
