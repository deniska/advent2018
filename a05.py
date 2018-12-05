from string import ascii_lowercase, ascii_uppercase

with open('input05.txt') as f:
    text = f.read().strip()

things_to_remove = [''.join(a)
        for a in zip(ascii_lowercase, ascii_uppercase)]
things_to_remove += [''.join(a)
        for a in zip(ascii_uppercase, ascii_lowercase)]

def react(text):
    while True:
        old_len = len(text)
        for r in things_to_remove:
            text = text.replace(r, '')
        if old_len == len(text):
            break
    return text, len(text)
text, l = react(text)

print(l)
sizes = []
for l, u in zip(ascii_lowercase, ascii_uppercase):
    shorter_text = text.replace(l, '').replace(u, '')
    sizes.append(react(shorter_text)[1])

print(min(sizes))
