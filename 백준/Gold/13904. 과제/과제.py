N = int(input())

arr = []
answer = [0 for _ in range(1000)]  # 최대 1000일의 과제

for _ in range(N):
    d, w = map(int, input().split())
    arr.append([d, w])

arr.sort(reverse=True, key=lambda x: x[1])  # 점수를 기준으로 내림차순 정렬

for i in range(N):
    for j in range(arr[i][0]-1, -1, -1):  # 주어진 마감일부터 첫날까지 역순으로 검사
        if answer[j] == 0:  # 아직 과제를 안했으면
            answer[j] = arr[i][1]  # 과제 해주기
            break  # 최댓값만 저장하고 끝내야함

print(sum(answer))