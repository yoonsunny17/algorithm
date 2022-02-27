T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    pig = [0] + list(map(int, input().split()))
    day = 1
    while True:
        if sum(pig[1:]) > N:
            break
        odd = pig[1] + pig[3] + pig[5]
        even = pig[2] + pig[4] + pig[6]
        
        for i in range(1, 7):
            if i % 2 == 0:
                pig[i] += odd
            else:
                pig[i] += even
        odd = even = 0
        day += 1
    print(day)