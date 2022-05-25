input_list_n_k = list(map(int,input().split()))
input_list = list(map(int,input().split()))
k = input_list_n_k[1]
for i in sorted(input_list):
    if k != 0:
        print(i, end=' ')
        k = k - 1
