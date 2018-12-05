from a05_1 import react
from string import ascii_lowercase, ascii_uppercase
from random import choices
import time

letters = ascii_lowercase + ascii_uppercase

random_inputs = []
for size in range(500, 50000, 500):
    random_inputs.append(''.join(choices(letters, k=size)))

with open('input05.txt') as f:
    text = f.read().strip()
sampled_inputs = []
for size in range(500, 50000, 500):
    sampled_inputs.append(text[:size//2]+text[-size//2:])

appended_inputs = []
for i in range(1, 50):
    appended_inputs.append(text * i)

def test_input(inp, r=10):
    for i in inp:
        begin = time.time()
        for _ in range(r):
            react(i)
        print(len(i), time.time() - begin)

print('Random inputs')
test_input(random_inputs)
print('Sampled inputs')
test_input(sampled_inputs)
print('Appended inputs')
test_input(appended_inputs, 1)
