import sys
sys.setrecursionlimit(10**9)

numbs = list()
while True:
    try:
        numbs.append(int(sys.stdin.readline()))
    except:
        break

def postorder(start, end):
    if start > end:
        return
    mid = end + 1

    for i in range(start+1, end+1):
        if numbs[start] < numbs[i]:
            mid = i
            break
    
    postorder(start+1, mid-1)
    postorder(mid, end)
    print(numbs[start])

postorder(0, len(numbs)-1)