word = input()
word = word.upper()
# print(word)
alpha_lst = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alpha_cnt = [0] * len(alpha_lst)
max_idx = 0

for i in word:
    if i in alpha_lst:
        alpha_cnt[alpha_lst.find(i)] += 1

        max_idx = max(max_idx, alpha_lst.find(i))

for i in range(len(alpha_cnt)):
    if alpha_cnt[i] == max(alpha_cnt):
        if alpha_cnt.count(max(alpha_cnt)) == 1:
            print(alpha_lst[i])
        else:
            print('?')
            break