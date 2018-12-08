import sys

def solve(nums, ptr=0):
    children_cnt = nums[ptr+0]
    metadata_cnt = nums[ptr+1]
    metadata_sum = 0
    ptr = ptr + 2
    children_values = {}
    metadatas = []
    for i in range(children_cnt):
        s, l, v = solve(nums, ptr)
        ptr = l
        metadata_sum += s
        children_values[i+1] = v
    for i in range(metadata_cnt):
        metadatas.append(nums[ptr])
        metadata_sum += nums[ptr]
        ptr += 1
    value = 0
    if children_cnt == 0:
        value = metadata_sum
    else:
        for metadata in metadatas:
            value += children_values.get(metadata, 0)
    return metadata_sum, ptr, value

def main(argv):
    fname = 'input08.txt'
    if len(argv) > 1:
        fname = argv[1]
    with open(fname) as f:
        nums = [int(a) for a in f.read().split()]
    result = solve(nums)
    print(result[0])
    print(result[2])

if __name__ == '__main__':
    main(sys.argv)
