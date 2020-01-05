from graph import Graph

def is_legal(one,two):
    if 'H1' in [one,two] and 'H2' in [one,two]:
        return True
    elif 'H1' in [one,two] and 'W1' in [one,two]:
        return True
    elif 'W1' in [one,two] and 'W2' in [one,two]:
        return True
    elif 'W2' in [one,two] and 'H2' in [one,two]:
        return True
    return False

def get_legal_groups(l):
    out=[]
    for a in l:
        for b in l:
            if is_legal(a,b) and not (((a,b) in out) or ((b,a) in out)):
                out.append((a,b))
        out.append(a)
    return out

l1=['H1','H2','W1','W2']
l2=[]

g=Graph()
g.add_node((l1,l2))

print(get_legal_groups(l1))