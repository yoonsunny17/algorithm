N = int(input())
length = []
height = []
width = []

for _ in range(N):
    L, H = map(int, input().split())
    length.append(L)
    height.append(H)

    while len(length) != 0:
        i = 0
        if length[i] is min(length):
            width.append([length[i], height[i]])
            del length[i]
            del height[i]

        else:
            i += 1

    width = sorted(width)

# print(width)

# 위치 기반으로 정렬된 length, height list
for j in range(len(width)):
    length.append(width[j][0])
    height.append(width[j][1])

# 가장 높은 기둥을 중심으로 왼쪽, 오른쪽 면적 구하기
center_idx = 0
total = 0
# print(length)
# print(height)

for i in range(len(height)):
    if height[i] is max(height):
        center_idx = i
        break

total += height[center_idx]

# print(center_idx)
# print(height[center_idx])
# print(total)

# 왼쪽 면적 구하기 전 정리
for i in range(center_idx):
    if height[i] >= height[i+1]:
        height[i+1] = height[i]
    total += height[i] * (length[i+1] - length[i])

# 오른쪽 면적 reverse idx 사용해서 정리
for i in range(len(height)-1, center_idx, -1):
    if height[i] >= height[i-1]:
        height[i-1] = height[i]
    total += height[i] * (length[i] - length[i-1])

print(total)