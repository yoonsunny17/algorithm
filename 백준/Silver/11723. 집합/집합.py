import sys

M = int(input())
ans = set()
for _ in range(M):
    calc = sys.stdin.readline().strip().split()

    # case 1. calc 가 명령만 있는 경우
    if len(calc) == 1:
        if calc[0] == 'all':
           ans = set([x for x in range(1, 21)])

        else:
            ans = set()
        continue

    # case 2. 숫자도 주어지는 경우
    command, numb = calc[0], calc[1]
    numb = int(numb)

    if command == 'add':
        ans.add(numb)
    
    elif command == 'remove':
        ans.discard(numb)

    elif command == 'check':
        print(1) if numb in ans else print(0)

    elif command == 'toggle':
        ans.add(numb) if numb not in ans else ans.discard(int(calc[1]))
