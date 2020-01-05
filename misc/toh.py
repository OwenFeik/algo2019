
def move(_1,_2):
    _2.append(_1.pop(-1))
    print(a,b,c)

def toh(disks,source,dest,aux):
    if disks==1:
        move(source,dest)
    else:
        toh(disks-1,source,aux,dest)
        move(source,dest)
        toh(disks-1,aux,dest,source)

# def tower(disks,source,dest,aux):
#     if disks==1:
#         print(f'move {source} to {dest}')
#     else:
#         tower(disks-1,source,aux,dest)
#         print(f'move {source} to {dest}')
#         tower(disks-1,aux,dest,source)
  
a=[5,4,3,2,1]
b=[]
c=[]

toh(5,a,c,b)