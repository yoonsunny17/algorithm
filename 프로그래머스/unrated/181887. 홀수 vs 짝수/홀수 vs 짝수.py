def solution(num_list):
    ans1, ans2 = 0, 0
    
    for i in range(len(num_list)):
        if i % 2:
            ans1 += num_list[i]
        else:
            ans2 += num_list[i]
    return ans1 if ans1 >= ans2 else ans2