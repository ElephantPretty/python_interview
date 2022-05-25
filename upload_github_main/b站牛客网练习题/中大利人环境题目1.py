# 学员成绩:
from copy import deepcopy

stu_g = {"A": {'语文': 11, '数学': 97, '英语': 83, '化学': 61, '物理': 31, '生物': 71},
         "B": {'语文': 4, '数学': 3, '英语': 59, '化学': 22, '物理': 72, '生物': 82},
         "C": {'语文': 80, '数学': 76, '英语': 26, '化学': 67, '物理': 42, '生物': 42},
         "D": {'语文': 54, '数学': 81, '英语': 60, '化学': 33, '物理': 30, '生物': 58},
         "E": {'语文': 38, '数学': 96, '英语': 47, '化学': 32, '物理': 56, '生物': 76},
         "F": {'语文': 97, '数学': 85, '英语': 24, '化学': 53, '物理': 74, '生物': 44},
         "G": {'语文': 59, '数学': 39, '英语': 30, '化学': 50, '物理': 39, '生物': 58},
         "H": {'语文': 30, '数学': 84, '英语': 21, '化学': 77, '物理': 94, '生物': 38},
         "I": {'语文': 68, '数学': 84, '英语': 19, '化学': 90, '物理': 100, '生物': 41},
         "J": {'语文': 66, '数学': 68, '英语': 76, '化学': 13, '物理': 70, '生物': 13},
         "K": {'语文': 1, '数学': 2, '英语': 62, '化学': 23, '物理': 71, '生物': 10},
         "L": {'语文': 86, '数学': 72, '英语': 7, '化学': 53, '物理': 31, '生物': 88},
         "M": {'语文': 92, '数学': 25, '英语': 19, '化学': 10, '物理': 70, '生物': 58},
         "N": {'语文': 10, '数学': 75, '英语': 7, '化学': 91, '物理': 46, '生物': 48},
         "O": {'语文': 96, '数学': 91, '英语': 85, '化学': 48, '物理': 62, '生物': 21},
         "P": {'语文': 98, '数学': 80, '英语': 85, '化学': 70, '物理': 47, '生物': 94}}
# 老师负责的学生:
tch_stu = {"AA": ["A", "C", "D", "K", "L"],
           "BB": ["B", "P", "O", "M"],
           "CC": ["E", "F", "G", "N"],
           "DD": ["H", "I", "J"]}
# 老师所在的年纪:
tch_grade = {"001": ["AA", "BB"], "002": ["CC", "DD"]}
# 时间--1,5h
"""
哪一个年级的平均分最高-->先区分年级->把每个年级的分平均一下  
001和002这个两个年级 001下面有AA和BB两个班 每个班上有不同的学生
A+C+D+K+L这五个人的成绩平均一下
"""
res_dic = deepcopy(tch_grade)
for i in tch_grade:
    dic_name_1 = i + 'grade'
    res_dic[dic_name_1] = 0
    dic_name_2 = i + 'stu_number'
    res_dic[dic_name_2] = 0
# print(res_dic)
# {'001': ['AA', 'BB'], '002': ['CC', 'DD'], '001grade': 0, '001stu_number': 0, '002grade': 0, '002stu_number': 0}
for grade_key,grade_value in  tch_grade.items():
    # ['AA', 'BB'] ['CC', 'DD']
    # print(grade_value)
    for stu_key,stu_value in tch_stu.items():
        # print(stu_key,grade_value)
        # AA ['AA', 'BB']
        if stu_key in grade_value:
            for stu_g_key,stu_g_value in stu_g.items():
                # print(stu_g_key)
                # 这一段暂时废弃
                # print(stu_g_value)
                if stu_g_key in stu_value:
                    dic_stu_number = grade_key + 'stu_number'
                    res_dic[dic_stu_number] += 1
                    dic_stu_grade = grade_key + 'grade'
                    for add_number in stu_g_value.values():
                        res_dic[dic_stu_grade] += add_number
# print(res_dic)
res_dic['001grade'] = res_dic['001grade'] / res_dic['001stu_number']
res_dic['002grade'] = res_dic['002grade'] / res_dic['002stu_number']
# 题目1--answer
# if res_dic['001grade'] > res_dic['002grade']:
#     print('001年级平均分高')
# else:
#     print('002年级平均分高')
# print(res_dic)
# 题目1分割线----------------------------------------
# 求题目2  按照数据成绩给全体成员排序
# prepare_list  = list()
# for i in
# stu_g



