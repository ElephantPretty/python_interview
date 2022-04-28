# https://www.bilibili.com/video/BV1qT4y1Y76U?spm_id_from=333.337.search-card.all.click

def m1():
    f = open("1.txt","w")
    f.write("python211")
    f.close()

"""
问题-如果在write中出现了问题，
会导致close一直无法被调用
1.txt这个资源一直被占用，无法被释放
"""
m1()