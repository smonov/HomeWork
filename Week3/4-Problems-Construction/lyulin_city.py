#Week3 Task4.4 lyulin_city.py

def solution(blocks):
    if len(blocks) == 0:
        return 0

    seen = 1
    current_max = blocks[0]

    for block in blocks:
        if block > current_max:
            seen += 1
            current_max = block

    return seen

n = input()
n = int(n)

blocks = []
start = 1

while start <= n:
    height = input()
    heihgt = int(height)

    blocks = blocks + [height]

    start += 1

print(solution(blocks))

