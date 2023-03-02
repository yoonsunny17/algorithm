N, M = map(int, input().split())
books = list(map(int, input().split()))

neg, pos = [], []  # 음수, 양수 나누기
max_walk = 0  # 제일 멀리있는 책 위치

for book in books:
    if book < 0:
        neg.append(book)
    elif book > 0:
        pos.append(book)

    if abs(book) > abs(max_walk):
        max_walk = book

neg.sort()
pos.sort(reverse=True)

rlt = 0  # 최소 걸음 수 출력할 변수

# M권을 들고 음수 방향으로 책을 두는 경우
for i in range(0, len(neg), M):
    # 제일 멀리 있는 책은 무시
    if neg[i] != max_walk:
        # 가장 멀리있는 것이 아니면 최소 걸음 수 갱신해주기
        rlt += abs(neg[i])

# M권을 들고 양수 방향으로 책을 두는 경우
for i in range(0, len(pos), M):
    # 제일 멀리 있는 책은 무시
    if pos[i] != max_walk:
        # 가장 멀리있는 것 아니면 최소 걸음 수 갱신
        rlt += pos[i]

# 최소 걸음 수 = 왕복 + 제일 멀리 있는 책 위치
rlt = rlt * 2 + abs(max_walk)

print(rlt)
