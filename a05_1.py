from string import ascii_lowercase, ascii_uppercase
import re

with open('input05.txt') as f:
    text = f.read().strip()
#text = 'dabAcCaCBAcCcaDA'

def react(text, ignore=''):
    left_idx = 0
    right_idx = 1
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
    return length - len(skips)

print(react(text))

sizes = []
for l, u in zip(ascii_lowercase, ascii_uppercase):
    shorter_text = re.sub(f'{l}|{u}', '', text)
    sizes.append(react(shorter_text))

print(min(sizes))
