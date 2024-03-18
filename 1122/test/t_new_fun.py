# coding=utf-8
import random


def random_file_symbol(name):
    symbol = [('（', '）'), ('「', '」'), (' - ',), ('，',)]
    idx = random.randint(0, len(symbol) - 1)
    if len(symbol[idx]) == 1:
        name = '{}{}'.format(symbol[idx][0], name)
    else:
        name = '{}{}{}'.format(symbol[idx][0], name, symbol[idx][1])
    return name


def t_random_file_symbol():
    for i in range(1000):
        fn = "中华人民共和国"
        print(random_file_symbol(fn))


def insert_search_str(ori_str, search_str):
    ori_list = ori_str.split('，')
    if len(ori_list) == 1:
        ori_list.insert(0, search_str)
    else:
        idx = random.randint(1, len(ori_list) - 1)
        ori_list.insert(idx, search_str)
    return '，'.join(ori_list)


def t_insert_search_str():
    for i in range(1000):
        print(insert_search_str(
            '这个镜，头就是对照的奥林巴斯。',
            '中华人民共和国'
        )
    )


def getFileData(url):
    try:
        with open(url) as f:
            # configs = f.read().splitlines()
            configs = f.read().splitlines()
            return configs
            # print(configs)
    except Exception as e:
        print(e)
        pass
    return []


def t_not_get_words():
    don_not_get_words = getFileData("../百度不采集的词.txt")
    t = '中奖'

    b = False
    for i in range(0, 10):
        print(i)
        for w in don_not_get_words:
            if t.find(w) != -1:
                print("包含不采集的关键词", t)
                b = True
            if b:
                print('x')
                break
        if b:
            continue


def t_eliminate_repeated_sentences():
    words = ['萧山区20002003年医卫科研成果一览表', '序号课', '称完成单位负责人评审结果获', '奖评审年份获奖年份', '1老年大学退休老人心身健康研', '究一院闻吾森国内领先市医卫三等', '区科技二等19992',
     '萧山医院的前身是萧山妇保', '单纯就妇产科来说', '个人觉得萧山医院比萧山人民医院靠谱点', '企业回ABC诊所管家（成都字', '节流科技有限公司）适用于全科', '儿科', '妇科', '西医',
     '中医等多类型诊所机构', '同时也适用于中小个体诊所', '大型诊所', '连锁诊所', '社区医院等多种规模形态的医疗机构', '体验简单快捷', '功能丰富强大', '适用于所有角色', '患者预约挂号',
     '既然预产期快到了', '就要做好准备', '有要大便的感觉就是要生了', '不过', '产兆是有规律的痛', '痛的时间间隔由长变短', '而且会越来越痛', '您好', '根据您的描述', '大部分人', '早孕反应',
     '不会很重', '而且孕三月后就会消失', '但也有少数孕妇会在孕中期仍有孕反应', '甚至有人持续到', '分娩', '结束才消失', '而且随着孕周增大', '增大的子宫将胃及膈肌向上挤推', '也会加重胃肠道症状',
     '你现在最好去医院查下', '怀孕前12周一直孕吐比较严重', '吐到胃疼', '但是多少还能吃点东西', '男生学外科肯定比学妇产科好一点', '男妇科医生一般会受妇女同胞的歧视', '病人少了收入自然少了',
     '除非你貌如潘安才比宋玉就另当别论', '当外科医生月薪医院级别不同收入差距也较大', '大概是4000一50000元', '准备宝宝的贴身衣物尿片', '医院有衣服提供', '不过面料一般', '护臀膏', '痱子粉',
     '（这个时候天气热', '小宝宝容易长痱子）', '奶瓶', '奶粉（可能有发）', '产妇要带上产妇专用卫生巾', '还有', '毛巾牙刷等个人用品', '睡衣带两套', '方便换洗',
     '萧山医院都是会提供些什么（产妇的和宝宝的）', '一般普通床位都有三个', '肯定是住单房好了', '生个孩子那么辛苦', '你今天的胎监评几分?是在什么方面', '扣了分?如果吸氧之后胎监正常的话', '就没什么影响',
     '你只需要每天自我监测胎动', '发现异常及时去医院就可以了', '我怀孕40周', '以前都正常', '今天去做监护说小孩缺氧', '我吸了半个小时的氧', '每月按50台手术计算',
     '每台手术的提成大约在300块钱到1000元之内', '这样的提成收入还是比较低的', '因为很多手术的费用往往达到了5万甚至10万以上', '一场手术差不多1万元费用的话', '那么提成比例按照7%核算',
     '医生和护士以及其他工作人员都要平摊', '结局', '尤盛美本以为经过了这一切', '曲晋明与她的婚姻算是走到了尽头', '但曲晋明却坦然的告诉她', '在今天看来', '尤盛美已经是他身体不可分割的一部分',
     '两人早已融为了一体', '两人早已融为了一体', '他是爱她的', '尤盛美终于等到了她这辈子一直在等的话', '在萧山医院的妇科上班', '正解', '给分吧', '萧山医院的妇科医生赵玲莉在哪上班', '我也是六楼小宝医生开的',
     '没有什么感觉宝宝就出来了', '麻醉师是很重要', '我老公同学在手术室', '所以麻醉打的很好', '母女平安', '产妇已经出院了', '孩子因为早产所以还要医院观察一段时间', '3月10号晚上',
     '在萧山区第三人民医院急诊室出现了一名孕妇', '裤子上袜子上都是血', '医生怀疑是胎盘早脱', '值班医生紧急呼叫在家备班的产科医生', '儿科医生', '还是第二个医生好', '她理解孕妇', '关心孕妇第一位医生的情况',
     '丁医生', '丁医生', '医生介绍（妇产科教授', '硕士生导师', '萧山医院', '全称浙江萧山医院', '是浙江杭州的三级综合医院', '地址', '浙江省杭州市萧山区萧然东路19号', '电话', '医院总机', '预约挂号']
    print('Before->', len(words))
    words = list(set(words))
    print('After->', len(words))

ggs = ['清华大学', '北京大学', '复旦大学', '科技大学']
def get_advertising():
    print(ggs)
    idx = random.randint(0, len(ggs) - 1)
    select_gg = ggs.pop(idx)
    print(select_gg)


def t_insert_advertising():
    line = '绝大部分人都选择蒙牛牛奶，从挤奶完成到加工不超过2小时，爱氏晨曦是国际知名的乳制品品牌，有助于孩子长身体，算中国最著名牛清华大学奶之一。'
    lines = line.split('，')
    if len(lines) == 1:
        pass
    else:
        idx = random.randint(1, len(lines) - 1)
        lines.insert(idx, '我是广告')
    return '，'.join(lines)


def g_ad_idx():
    datas = ['a', 'b', 'c', 'd', 'e']
    min_ad_count = 3
    max_ad_count = 5
    ad_count = random.randint(min_ad_count, max_ad_count)
    if len(datas) < ad_count:
        ad_count = len(datas)

    ad_index = []
    while ad_count > 0:
        idx = random.randint(0, len(datas) - 1)
        if idx not in ad_index:
            ad_index.append(idx)
            ad_count -= 1

    print(sorted(ad_index))


if __name__ == '__main__':
    # print(t_insert_advertising())
    # for i in range(1000):
    #     print(t_insert_advertising())

    paragraph_cur = random.randint(10, 13)
    print(paragraph_cur)

    alen = 999999
    sign_indexs = random.sample(range(0, alen), paragraph_cur)
    print(len(sign_indexs))
