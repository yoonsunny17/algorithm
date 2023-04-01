def dfs(idx):
    # 여섯자리 수 다 골랐으면 출력하고 리턴해줘
    if len(stack) == 6:
        print(" ".join(map(str, stack)))
        return
    
    # 여섯자리 수 아직 안되었으면 채워주자
    for i in range(idx, len(numbs)):
        # 탐색 숫자가 스택 안에 없으면, 백트래킹 해줘
        if numbs[i] not in stack:
            stack.append(numbs[i])
            dfs(i+1)
            stack.pop()


# 입력값으로 0 하나만 받을 때까지 반복해줘
while True:
    # 첫 번째 = k, 두 번째~ = k개의 수 주어짐
    arr = list(map(int, input().split()))
    if arr == [0]:
        break

    # k 뺀거 리스트 하나 만들어주자
    numbs = arr[1:]
    stack = []
    dfs(0)
    print()
