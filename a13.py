import sys

class Cart:
    def __init__(self, x, y, d):
        self.x = x
        self.y = y
        self.d = d
        self.active = True
        self.intersection = 'l' # 's' 'r'

    def __repr__(self):
        return f'Cart({self.x}, {self.y}, {self.d})'

    def order(self):
        return self.y, self.x

    def tick(self, m):
        c = m[self.y][self.x]
        if c == '/':
            self.d = {'>': '^', 'v': '<', '<': 'v', '^': '>'}[self.d]
        elif c == '\\':
            self.d = {'>': 'v', 'v': '>', '<': '^', '^': '<'}[self.d]
        elif c == '+':
            if self.intersection == 'l':
                self.d = {'>': '^', 'v': '>', '<': 'v', '^': '<'}[self.d]
            elif self.intersection == 'r':
                self.d = {'>': 'v', 'v': '<', '<': '^', '^': '>'}[self.d]
            self.intersection = {'l': 's', 's': 'r', 'r': 'l'}[self.intersection]
        self.x += {'>': 1, '<': -1}.get(self.d, 0)
        self.y += {'^': -1, 'v': 1}.get(self.d, 0)

def solve(m):
    carts = []
    for y, line in enumerate(m):
        for x, c in enumerate(line):
            if c in '^v<>':
                carts.append(Cart(x, y, c))
    while True:
        carts = sorted(carts, key=Cart.order)
        for cart in carts:
            cart.tick(m)
            for other_cart in carts:
                if other_cart is cart:
                    continue
                if other_cart.order() == cart.order():
                    print(f'{cart.x},{cart.y}')
                    return

def solve2(m):
    carts = []
    for y, line in enumerate(m):
        for x, c in enumerate(line):
            if c in '^v<>':
                carts.append(Cart(x, y, c))
    while True:
        carts = sorted(carts, key=Cart.order)
        for cart in carts:
            if not cart.active:
                continue
            cart.tick(m)
            for other_cart in carts:
                if other_cart is cart:
                    continue
                if other_cart.order() == cart.order():
                    cart.active = False
                    other_cart.active = False
        carts = [c for c in carts if c.active]
        if len(carts) == 1:
            c = carts[0]
            print(f'{c.x},{c.y}')
            return

def main(argv):
    fname = 'input13.txt'
    if len(argv) > 1:
        fname = argv[1]
    with open(fname) as f:
        m = f.read().splitlines()
    solve(m)
    solve2(m)

if __name__ == '__main__':
    main(sys.argv)
