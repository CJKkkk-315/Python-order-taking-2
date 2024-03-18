# ------------      -------    --------    -----------    -----------
# @File       : 大学排行榜分析大作业模板.py    
# @Contact    : 河北农业大学
# @Copyright  : 信息科学与技术学院
# @Modify Time: 2022/4/22 
# @Author     : 数信系
# @Version    : 1.0
# @License    : 仅限用于Python数据处理与分析大作业，具体要求请参照word文档。
# ------------      -------    --------    -----------    -----------

def read_file(file):
    """
    @参数 file:文件名，字符串类型
    读文件中的学校名到列表中，返回排名前10学校集合，集合类型。
    """
    res = set()
    with open(file,'r',encoding='utf-8') as f:
        data = f.readlines()
    for i in range(10):
        aw = [i for i in data[i].replace('\n','').split(' ') if i]
        res.add(aw[1])
    return res

def either_in_top(alumni, soft):
    """
    @参数 alumni：alumni大学排行榜中排名前10的学校的集合，集合类型
    @参数 soft：soft大学排行榜中排名前10的学校的集合，集合类型
    接收两个排行榜前10高校名字集合，返回在这两个排行榜中均名列前10的学校名。
    """
    return alumni&soft


def all_in_top(alumni, soft):
    """
    @参数 alumni：alumni大学排行榜中排名前10的学校的集合，集合类型
    @参数 soft：soft大学排行榜中排名前10的学校的集合，集合类型
    接收两个排行榜前10高校名字集合，
    返回在两个榜单中名列前10的所有学校名。
    """
    return alumni|soft


def only_alumni(alumni, soft):
    """
    @参数 alumni：alumni大学排行榜中排名前10的学校的集合，集合类型
    @参数 soft：soft大学排行榜中排名前10的学校的集合，集合类型
    接收两个排行榜前10高校名字集合，返回在alumni榜单中名列前10但soft榜单中未进前10的学校名。
    """
    res = set()
    for i in alumni:
        if i not in soft:
            res.add(i)
    return res


def only_one(alumni, soft):
    """
    @参数 alumni：alumni大学排行榜中排名前10的学校的集合，集合类型
    @参数 soft：soft大学排行榜中排名前10的学校的集合，集合类型
    接收两个排行榜前10高校名字集合，返回在alumni和soft榜单中名列前10，
    但不同时出现在两个榜单的学校名。
    """
    return alumni-soft


if __name__ == '__main__':
    alumni_set = read_file('./data/alumni.txt')
    soft_set = read_file('./data/soft.txt')
    either_rank = either_in_top(alumni_set, soft_set)
    all_rank = all_in_top(alumni_set, soft_set)
    only_in_alumni_rank = only_alumni(alumni_set, soft_set)
    alumni_soft_rank = only_one(alumni_set, soft_set)
    print(either_in_top(alumni_set, soft_set))
    print(f'两榜单中均名列前10的学校{either_rank}')
    print(f'两榜单名列前10的所有学校{all_rank}')
    print(f'alumni中名列前10，soft中未进前10的学校{only_in_alumni_rank}')
    print(f'不同时出现在两个榜单前10的学校{alumni_soft_rank}')
