N = int(input())
cards = [x for x in range(1, N+1)]
arr = [] # 버린 카드 모을 리스트

while len(cards) != 1:
    arr.append(cards.pop(0))
    cards.append(cards.pop(0))

for i in arr:
    print(i, end=' ')
print(cards[0])