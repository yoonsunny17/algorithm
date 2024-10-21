import math

ax, ay, az, bx, by, bz, cx, cy, cz = map(int, input().split())

ans = float('inf')

while True:
    mx = (ax + bx) / 2
    my = (ay + by) / 2
    mz = (az + bz) / 2

    ac = math.sqrt((ax - cx)**2 + (ay - cy)**2 + (az - cz)**2)
    bc = math.sqrt((bx - cx)**2 + (by - cy)**2 + (bz - cz)**2)
    h = math.sqrt((mx - cx)**2 + (my - cy)**2 + (mz - cz)**2)

    if abs(ans - h) <= 1e-6:
        print(f'{ans:.10f}')
        exit()
    if h < ans:
        ans = h
    if ac > bc:
        ax, ay, az = mx, my, mz
    else:
        bx, by, bz = mx, my, mz
