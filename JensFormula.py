import math

prob: int = 0

for i in range(5):
    for j in range(5 - i):
        throw1 = math.comb(5, i) * (1/6)**i * (5/6)**(5-i)
        throw2 = math.comb(5-i, j) * (1/6)**j * (5/6)**(5-i-j)
        throw3 = (1/6)**(5-i-j)
        prob += throw1 * throw2 * throw3

print(f'{prob * 100:.4f}%')  # not correct yet, TODO

