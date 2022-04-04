x, y, w, h = map(int, input().split())

min_x = min((w-x), abs(x))
min_y = min((h-y), abs(y))
min_rlt = min(min_x, min_y)
print(min_rlt)