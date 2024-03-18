import numpy as np
path=r'score-numpy.csv'
score=np.loadtxt(path,delimiter=',',skiprows=1,usecols=[2,3,4,5,6,7])#np.loadtxt()用于从文本加载数据。文本文件中的每一行必须含有相同的数据
name=np.loadtxt(path,delimiter=',',skiprows=1,usecols=[1],dtype=np.str_)
sum=np.sum(score,axis=1).round(2)
mean=np.average(score,axis=1).round(2)
# print(score)#各科成绩的打印
# print(name)#各学生姓名的打印
# print(sum)#各学生总成绩的打印
# print(mean)#各学生总科目的平均分
score_1=score.copy()
id(score)
id(score_1)
score_1[np.where(score_1<60)]=1#不及格
score_1[np.where(score_1>=95)]=5#优秀
score_1[np.where(score_1>=90)]=4.5
score_1[np.where(score_1>=85)]=4#良好
score_1[np.where(score_1>=80)]=3.5#良好
score_1[np.where(score_1>=75)]=3#一般
score_1[np.where(score_1>=70)]=2.5#一般
score_1[np.where(score_1>=65)]=2#及格
学分=np.array([4,3,2,3,4,3])
个人绩点学分成绩=score_1.dot(学分)
个人绩点=(个人绩点学分成绩/np.sum(学分)).round(2)
#整合
# np.vstack
# np.reshape
# np.hstack
#姓名，成绩，总分，平均分，绩点
总表=np.c_[name,score,sum,mean,个人绩点]
#排序
总表1=总表[总表[:,9].argsort()]
#课名称进来
title=np.array(['姓名','Android开发基础4','J2EE体系架构与应用3','J2EE体系结构实训2','计算机网络技术3','软件系统设计及体系结构4','物联网技术导论3','总分','平均分','绩点'])
总表2=np.vstack((title,总表1))
#总表1，shape
#存储
outfile=r'score_new.csv'
np.savetxt(outfile,总表2,fmt='%s',delimiter=',')
#菜单选择
while True:
    print('菜单选择：1,2,3,4,5,6,7,8,9,10')
    print('1,查询某科目最高分及最低分')
    print('2,查询某科目平均分')
    print('3,查询某科目前十名平均分')
    print('4,查询某科目前五名姓名及成绩')
    print('5,查询某科目及格人数')
    print('6,查询某科目的优秀人数及姓名，成绩（即单科成绩大于等于95为优秀）')
    print('7,查询某科目缺考人数及姓名（即分数为0的学生）')
    print('8,查询某学生的所有信息')
    print('9,查询某学生的某科成绩及学分')
    print('10,查询某学生的优秀科目数量')
    choice=eval(input('请选择需要查询的菜单：'))
    if choice == 1:
        pass
    elif choice == 2:
        pass
    elif choice == 3:
        pass
    elif choice == 4:
        pass
    elif choice == 5:
        pass
    elif choice == 6:
        pass
    elif choice == 7:
        pass
    elif choice == 8:
        name = input('请输入学生的姓名：')
        for i in 总表2:
            if i[0] == name:
                for k1,k2 in zip(总表2[0],i):
                    print(k1,k2)
    elif choice == 9:
        pass
    elif choice == 10:
        pass