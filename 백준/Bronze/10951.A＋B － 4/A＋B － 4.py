while True:
    try:
        numbers = list(map(int, input().split()))
        rlt = 0 
        for i in range(len(numbers)):
            rlt += numbers[i]
        print(rlt)

    except:
        exit()