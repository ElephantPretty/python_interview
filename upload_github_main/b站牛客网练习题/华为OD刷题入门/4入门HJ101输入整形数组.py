number_count = input()
prepare_list = list(map(int,input().split(' ')))
sorted_arr_flag = int(input())
# reverse=True-->逆序
# reverse=False->增序
for i in sorted(prepare_list,reverse=sorted_arr_flag):
    print(i, end=' ')
