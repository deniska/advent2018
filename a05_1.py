from string import ascii_lowercase, ascii_uppercase

def react(text):
    text = 'ж' + text
    left_idx = 1
    right_idx = 2
    length = len(text)
    skips = set()
    while right_idx < length:
        left = text[left_idx]
        right = text[right_idx]
        if left != right and left.upper() == right.upper():
            skips.add(left_idx)
            skips.add(right_idx)
            while left_idx in skips:
                left_idx -= 1
            right_idx += 1
            continue
        right_idx += 1
        left_idx = right_idx - 1
    new_string = ''.join(c for i, c in enumerate(text) if i not in skips)
    return new_string[1:], length - len(skips) - 1

def main():
    with open('input05.txt') as f:
        text = f.read().strip()

    text, r = react(text)
    print(r)

    sizes = []
    for l, u in zip(ascii_lowercase, ascii_uppercase):
        shorter_text = text.replace(l, '').replace(u, '')
        sizes.append(react(shorter_text)[1])
    print(min(sizes))

if __name__ == '__main__':
    main()
