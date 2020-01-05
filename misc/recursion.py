#
# Format:
#
# func(n):
#   iteration strategy
# func_r(n):
#   recursion strategy
#

def laugh(n):
    return 'Ha'*n
    
def laugh_r(n):
    return laugh_r(n-1)+'Ha' if n>1 else 'Ha'


def add_up(n):
    return sum([i for i in range(1,n+1)])

def add_up_r(n):
    return add_up_r(n-1)+n if n>1 else n


def reverse(string):
    return ''.join([string[len(string)-(i+1)] for i in range(len(string))])

def reverse_r(string):
    return string if len(string)==1 else reverse_r(string[1:])+string[0]


def length(l):
    return len(l)

def length_r(l):
    return length_r(l[1:])+1 if len(l)>1 else 1


def factorial(n):
    total=1
    for i in range(1,n+1):
        total*=i
    return total

def factorial_r(n):
    return factorial_r(n-1)*n if n>1 else 1
        

def fibonacci(n):
    fib=[1,1]
    while len(fib)<=n:
        fib.append(fib[-1]+fib[-2])
    return fib[-1]

def fibonacci_r(n):
    return 1 if n in [0,1] else fibonacci_r(n-1)+fibonacci_r(n-2)


def any_7(l):
    return True if 7 in l else False

def any_7_r(l):
    if l==[]:
        return False
    elif l[0]==7:
        return True
    else:
        return any_7_r(l[1:])


# def both_equal(stringa,stringb):
#     return stringa==stringb
def both_equal(stringa,stringb):
    if len(stringa)!=len(stringb):
        return False
    for i in range(len(stringa)):
        if stringa[i]!=stringb[i]:
            return False
    return True

def both_equal_r(stringa,stringb):
    if len(stringa)!=len(stringb):
        return False
    elif stringa[0]!=stringb[0]:
        return False
    
    if len(stringa)==1:
        return True
    else:    
        return both_equal_r(stringa[1:],stringb[1:])


def count_down(n):
    return [i for i in range(n,-1,-1)]

def count_down_r(n):
    return [0] if n==0 else [n]+count_down_r(n-1)


def square_list(l):
    return [n**2 for n in l]

def square_list_r(l):
    return [l[0]**2] if len(l)==1 else [l[0]**2]+square_list_r(l[1:])
