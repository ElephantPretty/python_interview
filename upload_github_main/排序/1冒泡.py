"""
1-冒泡排序-O(n^2)
https://cloud.tencent.com/developer/article/1108770
"""

def bubble_sort(alist):
    n = len(alist)
    for i in range (1, n):
        for j in range(n-i):
            if alist[j] > alist[j+1]:
                alist[j], alist[j+1] = alist[j+1],alist[j]
        return alist

if __name__ == '__main__':
    lis = [9,11,2,2,1,20,13]
    bubble_sort(lis)
    print(lis)