str = list(input().lower())
flag_str = input().lower()
count = 0
for i in str:
    if flag_str == i:
        count += 1
print(count)
