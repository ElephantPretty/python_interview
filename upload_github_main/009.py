"""
题目9
写一个用来遍历某目录所有内容的函数。(使用os模块)
1-遍历某目录下所有文件和文件夹
2-判断是文件还是文件夹
3-如果是文件就直接打印，如果是文件夹就再次判断，一直到没有文件夹为止
"""
# https://www.cnblogs.com/smallfoxdog/p/8622119.html
import os
def all_path(dir_name):
    result = [] #所有的文件
    for main_dir, sub_dir, file_name_list in os.walk(dir_name):
        print("1:", main_dir) # 当前主目录
        print("2:", sub_dir) # 当前主目录下的所有目录
        print("3:", file_name_list) # 当前主目录下的所有文件
        for file_name in file_name_list:
            a_path = os.path.join(main_dir, file_name)
            result.append(a_path)
    return result

print(all_path("D:\作品"))


