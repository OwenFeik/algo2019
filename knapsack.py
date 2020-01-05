
class Item():
    def __init__(self, v, w):
        self.value = v
        self.weight = w
        
    def __str__(self):
        return f'<W: {self.weight} V: {self.value}>'
    
    @property
    def v(self):
        return self.value

    @property
    def w(self):
        return self.weight


items = [Item(100, 3), Item(20, 2), Item(60, 4), Item(40, 1)]
size = 4

def optimise(size, items):
    if size == 0:
        return 0, []

    possible_items = [i for i in items if i.weight <= size]
    options = []
    for i in range(len(possible_items)):
        value, items = optimise(size - possible_items[i].weight, possible_items[:i] + possible_items[i + 1:])
        items.append(possible_items[i])
        option = value + possible_items[i].value, items

        options.append(option) 

    if options:
        return max(options, key = lambda k: k[0])
    else:
        return 0, []

print(optimise(size, items))
