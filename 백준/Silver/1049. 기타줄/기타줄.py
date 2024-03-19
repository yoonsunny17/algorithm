N, M = map(int, input().split())
package_lst, item_lst = [], []

for _ in range(M):
    package_price, item_price = map(int, input().split())
    package_lst.append(int(package_price))
    item_lst.append(int(item_price))

package_lst, item_lst = min(package_lst), min(item_lst)

if package_lst < item_lst * 6:
    if package_lst < (N % 6) * item_lst:
        print((N // 6) * package_lst + package_lst)
    else:
        print((N // 6) * package_lst + (N % 6) * item_lst)

elif package_lst >= item_lst * 6:
    print(N * item_lst)
