# ~*~ coding: utf-8 ~*~
import copy

import gevent
from gevent import monkey
from gevent.lock import BoundedSemaphore
monkey.patch_all()
sem = BoundedSemaphore(1)

import requests
from bs4 import BeautifulSoup
import re
from redis.client import Redis
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import unicodedata
from helper import FileData
from helper import getFileData
from threadEx import MyGet

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
from random import shuffle
import random

from lxml import etree

# 0、文章模式（百度相关搜索） 1、文章模式  2、问答模式  3、问答模式（百度相关搜索）
# 4 插入单词问答模式  5 插入单词文章模式

choice_model = 0

# 广告间距
advertising_len = 200

# 图片插入数  最大值 最小值你
pic_max = 1
pic_min = 1

# 句子的分割最大值 比如超过  22就分割成俩段
sentence_fenge_size = 22

# 段落的长度  文章的
paragraph_len_max15 = 80
paragraph_len_mim15 = 50

# 段落的长度  问答
paragraph_len_max234 = 100
paragraph_len_mim234 = 40

red = Redis(host='127.0.0.1', port='6379', db='1')
# red = Redis(host='127.0.0.1', port='6379', db='1')
split_size = 22

SONGGOU_NAME = "baiduzhidaodata"
BAIDU_FIND = 'baidu_zhidao'
# red.set(SONGGOU_NAME,"")
# red.set(BAIDU_FIND,"")
zis = ',，！!\t？?。|;、：:；\n '
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE',
}


def addErrorWordFile(c):
    try:
        f = open("采集失败的词.txt", "a+")
        c = c.replace("|||", "\n")
        f.write(c)
        f.write("\n")
        f.close()
    except:
        pass

def baiduxiangguan(c):
    try:
        f = open("采集成功的百度相关搜索词.txt", "a+")
        c = c.replace("|||", "\n")
        f.write(c)
        f.write("\n")
        f.close()
    except:
        pass



def zisindex(s):
    cend = 0
    for i in range(0, len(s)):
        if zis.find(s[i]) != -1:
            return cend
        cend += 1
    return cend


def fenge(s, cont):
    cbegin = 0
    cend = 0
    cdata = ""
    for i in range(0, len(s)):
        cend += 1
        if zis.find(s[i]) != -1:
            max_c = (cend - cbegin) - 1
            item_d = s[cbegin:cend]
            if max_c < cont:
                cdata += item_d
            else:  # 替换
                cint = int(max_c / 2)
                cdata += item_d[:cint]
                cdata += "，"
                cdata += item_d[cint:]
            cbegin = cend
            pass

    return cdata


def GetIndexSx(s):
    ret_index = 0
    for i in range(len(s) - 1, -1, -1):
        if not s[i].isalnum():
            break
        if is_Chinese(s[i]):
            break
        ret_index += 1

    return ret_index


class Picsrc():
    global peizhi

    def __init__(self, url, num):
        super().__init__()

        self.datas = self.getFileData(url)
        self.num = num
        self.num_cur = 0
        self.datas_idnex = peizhi[2]
        self.datas_len = len(self.datas)
        self._shuffle()

    def _shuffle(self):
        shuffle(self.datas)
        self.datas_idnex = 0

    def clear(self):
        self.num_cur = 0

    def getFileData(self, url):
        try:
            with open(url) as f:
                configs = f.read().splitlines()
                # configs = f.read()
                return configs
                # print(configs)
        except  Exception as e:
            # print(e)
            pass
        return None

    def get_pic(self):
        ret = ""
        if self.num_cur >= self.num:
            return ret
        if self.datas_len >= self.datas_idnex:
            self._shuffle()
        if self.is_pic():
            ret = self.datas[self.datas_idnex]
            self.datas_idnex += 1
            self.num_cur += 1
        return ret

    def is_pic(self):
        d = random.randint(0, 4)
        return d == 0

    def get_pics(self):
        if self.datas_len <= self.datas_idnex:
            self._shuffle()
        if self.datas_len <= (self.datas_idnex + self.num):
            self._shuffle()

        ret = self.datas[self.datas_idnex:self.datas_idnex + self.num]
        self.datas_idnex += self.num
        peizhi[2] = self.datas_idnex
        return ret


index = 0

str_yonghu_head = '''<div class="zuijiahuida">
<div class="clear"></div>
<div class="zuijiatop">
<div class="zuijiatoptx">{3}</div>
<div class="zuijiatopmid">
<div class="zuijiatopxm">{0}</div>
<div class="zuijiatoptime">{1}小时{2}分钟前回答</div>
</div>
<div class="clear"></div>
</div>
<div class="zuijiacont">
{4}
<p><div style="padding-bottom: 10px"><span>已被{5}人点赞</span></div></p>
</div>
</div>         
</div>
'''
usernames_index = 0
toptx_index = 0

# 0名称 1小时  2分钟 3头像 4内容 5点赞
str_yonghu = '''<div class="wendazhuti"> 
<div class="clear"></div> 
<div class="zuijiahuida">
<div class="clear"></div>
<div class="zuijiatop">
<div class="zuijiatoptx">{3}</div>
<div class="zuijiatopmid">
<div class="zuijiatopxm">{0}</div>
<div class="zuijiatoptime">{1}小时{2}分钟前回答</div>
</div>
<div class="clear"></div>
</div>
<div class="zuijiacont">
{4}
<p><div style="padding-bottom: 10px"><span>已被{5}人点赞</span></div></p>
</div>
</div>         
</div>
'''


def GetUserName():
    global usernames
    global usernames_index
    if len(usernames) <= usernames_index:
        shuffle(usernames)

        usernames_index = 0
    d = usernames[usernames_index]
    usernames_index += 1
    return d


def GetToptx():
    global toptx
    global toptx_index
    if len(toptx) <= toptx_index:
        shuffle(toptx)
        toptx_index = 0
    d = toptx[toptx_index]
    toptx_index += 1
    return d


def GetHead(data):
    user = str_yonghu_head.format(GetUserName(), random.randint(1, 23), random.randint(1, 59), GetToptx(), data,
                                  random.randint(1, 5000))
    return user


def Getsuijici():
    global peizhi
    global suijic
    if len(suijic) <= peizhi[0]:
        shuffle(suijic)

        peizhi[0] = 0
    d = suijic[peizhi[0]]
    peizhi[0] += 1
    return d


def GetSuijic(s):
    cbegin = 0
    cend = 0
    cdata = ""
    listjic = []
    for i in range(0, len(s)):
        cend += 1
        if zis.find(s[i]) != -1:

            max_c = (cend - cbegin) - 1
            item_d = s[cbegin:cend]
            # print(item_d)
            # if item_d.find("子直接吃")!=-1:
            #     print("")
            # if s[i] == "\n":
            #     cbegin = cend
            #     cdata += item_d
            #     continue
            # print( item_d)

            if max_c < 3:
                cdata += item_d
            else:  # 替换
                cint = int(max_c / 2)

                # A =item_d
                # for li in sjic:#数据不插入
                #     size_t =A .find(li)
                #     if (cint) >= (size_t-len(li)):  # 开始的位置  大于当前分割地方 且小于 分割地方
                #         if  (cint)<=(size_t + len(li)):
                #             cint= size_t
                #             break
                cdata += item_d[:cint]
                c = Getsuijici()
                listjic.append(c)
                cdata += c
                cdata += item_d[cint:]
            cbegin = cend

    return cdata, listjic


def GetTihuanc(s):
    global tihuanc
    for i in tihuanc:
        ds = i.split("---")
        if len(ds) == 2:
            s = s.replace(ds[0], ds[1])
        else:
            s = s.replace(ds[0], "")

    return s


def GetZhongjiancs():
    global peizhi
    if len(zhongjianc) <= peizhi[1]:
        peizhi[1] = 0
        shuffle(zhongjianc)
        # print(zhongjianc)
    d = zhongjianc[peizhi[1]]
    peizhi[1] += 1
    return d


def GetZhongjianc(s):
    cbegin = 0
    cend = 0
    cdata = ""
    for i in range(0, len(s)):
        cend += 1
        if zis.find(s[i]) != -1:
            if cend >= (cbegin + 13):
                item_d = s[cbegin:cend]
                # print(item_d)
                # if item_d.find("子直接吃")!=-1:
                #     print("")
                if s[i] == '\n':
                    cdata += item_d[:-1]

                    if zis.find(cdata[-1]) == -1:
                        cdata += "，"
                    cdata += GetZhongjiancs()
                    cdata += "\n"
                else:
                    cdata += item_d
                    cdata += GetZhongjiancs()
                    if zis.find(cdata[-1]) == -1:
                        cdata += "，"
                cbegin = cend
                # if item_d.find("去医院安安才是当务之急。")!=-1:
                #     print()
    if cbegin != cend:
        cdata += s[cbegin:cend]

    return cdata


# 0名称 1小时  2分钟 3头像 4内容 5点赞
def GetUser(data):
    user = str_yonghu.format(GetUserName(), random.randint(1, 23), random.randint(1, 59), GetToptx(), data,
                             random.randint(1, 5000))
    return user


def GetTail():
    return "</article>"


# dete_url = getFileData("屏蔽url.txt")
dete_data = getFileData("屏蔽内容.txt")
peizhi = None
if not peizhi:
    peizhi = []
    peizhi.append(0)
    peizhi.append(0)
    peizhi.append(0)
else:
    peizhi[0] = int(peizhi[0])
    peizhi[1] = int(peizhi[1])
    peizhi[2] = int(peizhi[2])

zhongjianc = getFileData("随机关键词.txt")
tihuanc = getFileData("替换关键词.txt")
usernames = getFileData("名称.txt")  # 名称
toptx = getFileData("头像.txt")  # 名称
bunengcharu = getFileData("不能插入.txt")  # 名称
shuffle(zhongjianc)
shuffle(tihuanc)

shuffle(usernames)
shuffle(toptx)

don_not_get_words = getFileData("百度不采集的词.txt")
guanggao2 = getFileData("广告2.txt")  # 广告
guanggao = getFileData("广告.txt")  # 广告


def get_val(allCon):
    if not allCon:
        allCon = ""
    else:
        allCon = allCon.decode('utf-8', "ignore")
    return allCon


def is_Chinese(ch):
    if '\u4e00' <= ch <= '\u9fff':
        return True
    return False


def IsTime(bs):
    tag = bs.find(class_='tag-time')
    if tag:
        return tag.text

    tag = bs.find(class_='str_time')
    if tag:
        return tag.text
    return ""


def GetData(user):
    st = ''
    text = user.find(class_='text-layout')
    if text:
        c999 = text.find(class_='font-c999')
        # p-line-height
        ps = text.find_all(class_='p-line-height')
        try:
            if ps:
                st = ps[-1].text
                return st
        except Exception as e:
            print(e)
        dd = text.find(class_='star-wiki')
        if dd:
            st = (dd.text)
        else:
            st = (text.text)
        try:
            st = st.replace(c999.text, "")
        except:
            pass
    else:
        text = user.find(class_='str_info')
        if text:
            st = (text.text)

        else:
            text = user.find(class_='space-txt')
            if text:
                st = (text.text)
            else:
                if user.text.find("百度经验") != -1:
                    for u in user.find_all(class_="clamp1"):
                        st += u.text

                else:
                    for text in user.find_all(class_="str-text-info"):
                        if text:
                            st += (text.text)

    return st


def GetSuijics(s, sjic):
    cbegin = 0
    cend = 0
    cdata = ""
    listjic = []
    for i in range(0, len(s)):
        cend += 1
        if zis.find(s[i]) != -1:
            max_c = (cend - cbegin) - 1
            item_d = s[cbegin:cend]
            if max_c < 3:
                cdata += item_d
            else:  # 替换
                cint = int(max_c / 2)
                A = item_d
                for li in sjic:  # 数据不插入
                    size_t = A.find(li)
                    if size_t == -1:
                        continue
                    if (cint) >= (size_t - len(li)):  # 开始的位置  大于当前分割地方 且小于 分割地方
                        if (cint) <= (size_t + len(li)):
                            cint = size_t
                            break
                pos = GetIndexSx(item_d[:cint])
                cint -= pos
                cdata += item_d[:cint]
                c = Getsuijici()
                if not c in listjic:
                    listjic.append(c)
                cdata += c
                cdata += item_d[cint:]
            cbegin = cend

    return cdata, listjic


def baiduzhidao(find, get, threshold):
    allCon = red.get(SONGGOU_NAME)
    allCon = get_val(allCon)
    find = find.encode("gbk")
    a = str(find)
    find = a[2:-1].replace("\\x", "%")

    i = 0
    addr = []
    for qindex in range(0, 6):
        # 百度知道列表搜索URL
        pn = 10 * qindex
        url = f" https://zhidao.baidu.com/search?lm=0&rn=10&pn={pn}&fr=search&ie=gbk&word={find}"

        # url = "https://www.sogou.com/web?ie=utf8&query={}&page={}"
        # qq=url.format(find,qindex)
        # qq='https://www.sogou.com/link?url=hedJjaC291N3WVb8QZr-vYtKjeQCiwCo9HxyjH5SmbzXcEiNLB02ZvJGBZzoiO82reaVHN88tHY.'
        # data= requests.get(qq,headers=headers)
        data = get.get(url)  # requests.get(url.format(find), headers=headers, timeout=5,verify=False)
        data.encoding = 'gbk'

        # 百度知道列表页面
        bs = BeautifulSoup(data.text, "lxml")
        list = bs.find(id="wgt-list")
        if not list:
            continue

        # 页面解析
        for dl in list.find_all('dl'):
            st = dl.find(class_='answer')
            if not st:
                continue

            st = st.text
            summary = dl.find(class_='summary')
            if summary:
                st += "\n"
                st += summary.text

            try:
                if not st:
                    continue
                if st.find("查看全部") != -1:
                    index = st.find("查看全部")
                    st = st[:index]
                if st.find("更多") != -1:
                    index = st.find("更多")
                    if len(st) < index + 5:
                        st = st[:index]
                if st.find("更多>>") != -1:
                    index = st.find("更多>>")
                    st = st[:index]
                if st.find("详情") != -1:
                    index = st.find("详情")
                    if len(st) < index + 5:
                        st = st[:index]
                if st.find('知乎 - www.zhihu') != -1:
                    index = st.find("知乎 - www.zhihu")
                    st = st[:index]
                if st.find("知乎 - zhuanlan.zhihu.com") != -1:
                    index = st.find("知乎 - zhuanlan.zhihu.com")
                    st = st[:index]
                st = st.replace("[图文]", '')
                st = st.replace("\r", '')
                st = st.replace(u'\xa0', u'')
                st = st.replace(u'\u3000', u'')
                b = False
                if st.find("document") != -1:
                    continue

                st = re.sub(r'问题说明：', '', st)
                st = re.sub(r'问题说明', '', st)
                st = re.sub(r'最佳答案：', '', st)
                st = re.sub(r'最佳答案', '', st)
                st = re.sub(r'\d{4}-\d{2}-\d{2}：', '', st)
                st = re.sub(r'\d{4}-\d{2}-\d{2}', '', st)
                st = re.sub(r'\d{4}-\d{2}-\d{2}:', '', st)
                st = re.sub(r'\d{4}年\d{2}月\d{2}日', '', st)
                st = re.sub(r'\d{4}-\d{1}-\d{1}', '', st)
                st = re.sub(r'\d{4}年\d{1}月\d{1}日', '', st)
                st = re.sub(r'\d{4}-\d{1}-\d{2}', '', st)
                st = re.sub(r'\d{4}-\d{2}-\d{1}', '', st)
                st = re.sub(r'\d{4}年\d{2}月\d{1}日', '', st)
                st = re.sub(r'\d{4}年\d{1}月\d{2}日', '', st)
                st = re.sub(r'\d{11}', '', st)
                st = re.sub(r'http://', '', st)
                st = re.sub(r'www.*.com.cn', '', st)
                st = re.sub(r'www.*.com', '', st)
                st = st.replace("-", '')
                st = st.replace("答：", '')
                st = st.replace("问：", '')
                while True:
                    sta = st.replace("  ", '')
                    if len(sta) == len(st):
                        break
                    st = sta
                # print(st)
                begin = 0
                list_st = []
                st_len = len(st)
                while True:
                    end = st.find("...", begin)
                    if end == -1:
                        if st_len > begin + 2:
                            list_st.append(st[begin:])
                        break
                    datas = re.split('[,，！？。|;、：；.\n ]+', st[begin:end])
                    list_st.append(st[begin:end - len(datas[-1])])
                    begin = end + 3
                st = ("".join(list_st))
                st = st.strip()
                if allCon.find(st[:10]) != -1:
                    print("重复数据")
                    continue

                print("需要的数据一条")
                allCon += st
                red.set(SONGGOU_NAME, allCon)
                i += 1
                addr.append(st.replace('\n', ''))
                if i >= threshold:
                    if len("".join(addr)) < 400:
                        # print ("小于800继续采集")
                        continue
                    return addr, i

            except:
                pass

    return addr, i


def baiduzhidao1(find, get, discard):
    nrand = random.randint(350, 400)
    # red.set(SONGGOU_NAME, "")
    allCon = red.get(SONGGOU_NAME)
    allCon = get_val(allCon)
    find = find.encode("gbk")
    a = str(find)
    find = a[2:-1].replace("\\x", "%")
    # find= find.decode('GB2132')
    # requests
    # urldecode
    i = 0
    addr = []
    for qindex in range(0, 5):
        # print(qindex)
        pn = 10 * qindex
        url = f" https://zhidao.baidu.com/search?lm=0&rn=10&pn={pn}&fr=search&ie=gbk&word={find}"

        # url = "https://www.sogou.com/web?ie=utf8&query={}&page={}"
        # qq=url.format(find,qindex)
        # qq='https://www.sogou.com/link?url=hedJjaC291N3WVb8QZr-vYtKjeQCiwCo9HxyjH5SmbzXcEiNLB02ZvJGBZzoiO82reaVHN88tHY.'
        # data= requests.get(qq,headers=headers)
        data = get.get(url)  # requests.get(url.format(find), headers=headers, timeout=5,verify=False)
        data.encoding = 'gbk'

        bs = BeautifulSoup(data.text, "lxml")
        list = bs.find(id="wgt-list")
        if not list:
            continue
        for dl in list.find_all('dl'):
            st = dl.find(class_='answer')
            if not st:
                continue

            st = st.text
            summary = dl.find(class_='summary')
            if summary:
                st += "\n"
                st += summary.text

            try:
                if not st:
                    continue
                if st.find("查看全部") != -1:
                    index = st.find("查看全部")
                    st = st[:index]
                if st.find("更多") != -1:
                    index = st.find("更多")
                    if len(st) < index + 5:
                        st = st[:index]
                if st.find("更多>>") != -1:
                    index = st.find("更多>>")
                    st = st[:index]
                if st.find("详情") != -1:
                    index = st.find("详情")
                    if len(st) < index + 5:
                        st = st[:index]
                if st.find('知乎 - www.zhihu') != -1:
                    index = st.find("知乎 - www.zhihu")
                    st = st[:index]
                if st.find("知乎 - zhuanlan.zhihu.com") != -1:
                    index = st.find("知乎 - zhuanlan.zhihu.com")
                    st = st[:index]
                st = st.replace("[图文]", '')
                st = st.replace("\r", '')
                st = st.replace(u'\xa0', u'')
                st = st.replace(u'\u3000', u'')
                b = False
                if st.find("document") != -1:
                    continue

                st = re.sub(r'问题说明：', '', st)
                st = re.sub(r'问题说明', '', st)
                st = re.sub(r'最佳答案：', '', st)
                st = re.sub(r'最佳答案', '', st)
                st = re.sub(r'\d{4}-\d{2}-\d{2}：', '', st)
                st = re.sub(r'\d{4}-\d{2}-\d{2}', '', st)
                st = re.sub(r'\d{4}-\d{2}-\d{2}:', '', st)
                st = re.sub(r'\d{4}年\d{2}月\d{2}日', '', st)
                st = re.sub(r'\d{4}-\d{1}-\d{1}', '', st)
                st = re.sub(r'\d{4}年\d{1}月\d{1}日', '', st)
                st = re.sub(r'\d{4}-\d{1}-\d{2}', '', st)
                st = re.sub(r'\d{4}-\d{2}-\d{1}', '', st)
                st = re.sub(r'\d{4}年\d{2}月\d{1}日', '', st)
                st = re.sub(r'\d{4}年\d{1}月\d{2}日', '', st)
                st = re.sub(r'\d{11}', '', st)
                st = re.sub(r'http://', '', st)
                st = re.sub(r'www.*.com.cn', '', st)
                st = re.sub(r'www.*.com', '', st)
                st = st.replace("-", '')
                st = st.replace("答：", '')
                st = st.replace("问：", '')
                while True:
                    sta = st.replace("  ", '')
                    if len(sta) == len(st):
                        break
                    st = sta
                # print(st)
                begin = 0
                list_st = []
                st_len = len(st)
                while True:
                    end = st.find("...", begin)
                    if end == -1:
                        if st_len > begin + 2:
                            list_st.append(st[begin:])
                        break
                    datas = re.split('[,，！？。|;、：；.\n ]+', st[begin:end])
                    list_st.append(st[begin:end - len(datas[-1])])
                    begin = end + 3
                st = ("".join(list_st))
                st = st.strip()
                if allCon.find(st[:10]) != -1:
                    print("重复数据")
                    continue

                print("需要的数据一条")
                allCon += st
                red.set(SONGGOU_NAME, allCon)
                i += 1
                addr.append(st.replace('\n', ''))
                # if i >= discard:
                if len("".join(addr)) >= nrand:
                    #     # print ("小于800继续采集")
                    #     continue
                    return addr, i

            except:
                pass

    return addr, i


def is_number(s):
    try:
        float(s)  # 如果能转换float，说明是个数字
        return True
    except ValueError:
        pass  # 占位符

    try:
        # 引入Unicodedata模块
        unicodedata.numeric(s)  # 如果能转成numeric，说明是个数字
        return True
    except (TypeError, ValueError):
        pass

    return False


class Advertising:

    def __init__(self):
        super().__init__()
        global advertising_len
        self.advertising_len = advertising_len  # 20的距离插入
        self.advertising_cur = 0
        self.datas = self.getFileData("广告.txt")
        self.datas_len = len(self.datas)

        # self.advertising = self.GetAdvertising()

    def GetAdvertising(self):
        if not self.datas_len:
            return ""
        global index
        if self.datas_len <= index:
            shuffle(self.datas)
            index = 0
        d = self.datas[index]
        index += 1
        return d

    def Advertising(self, str, listjic=None):
        if listjic == None:
            listjic = []
        if self.advertising_len <= (len(str) + self.advertising_cur):
            cur = self.advertising_len - self.advertising_cur
            for li in listjic:
                size_t = str.find(li)
                if cur < size_t:  # 开始的位置  大于当前分割地方 且小于 分割地方
                    if size_t + len(li) > cur:
                        cur = size_t
                        break
            guangao = self.GetAdvertising()
            guangao_len = len(guangao)
            bgungao = False
            try:
                if str[:cur][guangao_len:] == guangao:
                    bgungao = True
                if str[cur:][:guangao_len] == guangao:
                    bgungao = True
            except:
                pass
            if bgungao:
                guangao = ""
            a = str[:cur] + guangao + str[cur:]
            self.advertising_cur = (len(str) + self.advertising_cur) - self.advertising_len
            if self.advertising_cur > self.advertising_len:
                self.advertising_cur = self.advertising_cur % self.advertising_len

            return a

        self.advertising_cur += len(str)
        return str

    def Advertisings(self, str, listjic=None):
        if listjic == None:
            listjic = []
        size_cur = 0
        size_max = len(str)
        size_len = self.advertising_len
        cur = size_len
        a = ""
        while True:
            if (size_len + cur) <= (size_max):
                A = str[size_cur:]
                # print(A[:5])
                for li in listjic:  # 数据不插入
                    size_t = A.find(li)
                    if size_t == -1:
                        continue

                    # 数据太近没啥用
                    if (size_len - size_t) > len(li):
                        size_t = A.find(li, size_t + 1)
                        if size_t == -1:
                            continue

                    if (cur - size_cur) >= (size_t - len(li)):  # 开始的位置  大于当前分割地方 且小于 分割地方
                        if (cur - size_cur) <= (size_t + len(li)):
                            cur = size_t + size_cur
                            break
                # 不打开
                guangao = self.GetAdvertising()
                guangao_len = len(guangao)
                bgungao = False

                try:
                    d = str[cur]
                    if guangao.find(d) != -1:
                        bgungao = True
                except:
                    pass
                try:

                    if str[cur:][:guangao_len] == guangao:
                        bgungao = True
                except:
                    pass

                if bgungao:
                    guangao = ""
                else:
                    pos = GetIndexSx(str[size_cur:cur])
                    if pos:
                        cur -= pos

                bucharu = False
                if str[cur] == '\n' or cur == size_max or cur + 1 == size_max:
                    bucharu = True
                    a += str[size_cur:cur]

                if not bucharu:
                    a += str[size_cur:cur] + guangao

                size_cur = cur
                cur += size_len

                # size_len = self.advertising_len+size_cur

            else:
                self.advertising_cur += len(str)
                a += str[size_cur:]
                break

        return a

    def getFileData(self, url):
        try:
            with open(url) as f:
                configs = f.read().splitlines()
                # configs = f.read()
                return configs
                # print(configs)
        except  Exception as e:
            # print(e)
            pass
        return None


class BeforeAdvertising:

    def __init__(self, exclude=None):
        super().__init__()
        self.exclude = exclude or []     # exclude 不能插入的数据
        self.datas = copy.deepcopy(guanggao)

    def GetAdvertising(self):
        if len(self.datas) <= 0:
            return None
        idx = random.randint(0, len(self.datas) - 1)
        select_gg = self.datas[idx]
        return select_gg

    def Advertising(self, line):
        is_dried = False
        while True:
            sgg = self.GetAdvertising()
            if not sgg:
                is_dried = True
                break

            if sgg in self.exclude:
                continue
            else:
                break

        lines = line.split('，')
        if is_dried or len(lines) in [0, 1]:
            return line
        else:
            # 加逗号的处理方式
            # idx = random.randint(1, len(lines) - 1)
            # lines.insert(idx, sgg)

            # 不加逗号的处理方式
            idx = random.randint(1, len(lines) - 1)
            tmp = lines[idx]
            lines[idx] = ''
            lines[idx] = sgg + tmp
            return '，'.join(lines)

    def getFileData(self, url):
        try:
            with open(url) as f:
                configs = f.read().splitlines()
                return configs
        except Exception as e:
            print(e)
        return None


class SentenceAdvertising:

    def __init__(self, exclude=None):
        super().__init__()
        self.exclude = exclude or []     # exclude 不能插入的数据
        self.datas = copy.deepcopy(guanggao2)

    def GetAdvertising(self):
        if len(self.datas) <= 0:
            return None
        idx = random.randint(0, len(self.datas) - 1)
        select_gg = self.datas.pop(idx)
        return select_gg

    def Advertising(self, line):
        is_dried = False
        while True:
            sgg = self.GetAdvertising()
            if not sgg:
                is_dried = True
                break

            if sgg in self.exclude:
                continue
            else:
                break

        lines = line.split('，')
        if is_dried or len(lines) in [0, 1]:
            return line
        else:
            # 加逗号的处理方式
            # idx = random.randint(1, len(lines) - 1)
            # lines.insert(idx, sgg)

            # 不加逗号的处理方式
            idx = random.randint(0, len(lines) - 1 - 1)
            lines[idx] += sgg
            return '，'.join(lines)

    def getFileData(self, url):
        try:
            with open(url) as f:
                configs = f.read().splitlines()
                return configs
        except Exception as e:
            print(e)
        return None


advertising = Advertising()


def isChinese(word):
    for ch in word:
        if '\u4e00' <= ch <= '\u9fff':
            return True
    return False


# b= time.time()
find_infos = red.get(BAIDU_FIND)
find_infos = get_val(find_infos)

# allConbaidu = red.get("baidu_infos")
# if not allConbaidu:
#     allConbaidu = ""
# else:
#     allConbaidu = allConbaidu.decode('utf-8', "ignore")


def baidu(key, get):
    global find_infos
    find_url = 'https://www.baidu.com/s?wd=' + key
    retry_count = 0
    change_proxies = False
    while True:
        data = get.get_baidu(find_url, change_proxies)
        html = data.text
        if not html:
            change_proxies = True
            retry_count += 1
            if retry_count > 3:
                return None

        try:
            dom_tree = etree.HTML(html)
            xgss = dom_tree.xpath('//*[@id="rs_new"]/div/text()')
            xgss = ''.join(xgss).replace('\n', '').replace(' ', '')
            if xgss != '相关搜索':
                continue

            for td_ele in dom_tree.xpath('//*[@id="rs_new"]//td'):
                t = ''.join(td_ele.xpath('./a/text()')).replace('\n', '').replace(' ', '')
                if find_infos.find(t) != -1:
                    print("重复相关搜索", t)
                    continue
                # 自己设置包含哪些关键词的不采集
                ctu = False
                for w in don_not_get_words:
                    if t.find(w) != -1:
                        print("包含不采集的关键词", t)
                        ctu = True
                    if ctu:
                        break
                if ctu:
                    continue

                find_infos += t
                red.set(BAIDU_FIND, find_infos)
                return t
        except Exception as e:
            change_proxies = True
            retry_count += 1
            if retry_count > 3:
                return None
            continue
    return None


# lock=threading.Lock()
picsrc = Picsrc("src.txt", 2)
# find_infos = red.get(BAIDU_FIND)
# find_infos = get_val(find_infos)


def random_file_symbol(name):
    symbol = [('（', '）'), ('「', '」'), (' - ',), ('，',)]
    idx = random.randint(0, len(symbol) - 1)
    if len(symbol[idx]) == 1:
        name = '{}{}'.format(symbol[idx][0], name)
    else:
        name = '{}{}{}'.format(symbol[idx][0], name, symbol[idx][1])
    return name


def run(file_data):
    global find_infos
    ident = gevent.getcurrent().getcurrent().name

    get = MyGet()
    for find in file_data:
        print(' <{}> * Search data -> {}'.format(ident, find))
        if find_infos.find(find) != -1:
            # 现在在这里吧
            print("重复搜索数据", find)
            continue
        if choice_model == 3 or choice_model == 0:
            finds = []
            finds.append(find)
            # lock.acquire()
            f = baidu(find, get)
            # lock.release()
            if f:
                print(' <{}> + Baidu data -> {}'.format(ident, f))
                # 保存所以搜索过的问题
                find_infos += find
                red.set(BAIDU_FIND, find_infos)
                finds.append(f)
                # 采集问答
                if choice_model == 0:
                    litsa, index = baiduzhidao(finds[0], get, 8)
                    litsb, index1 = baiduzhidao(finds[1], get, 15 - index)
                else:
                    litsa, index = baiduzhidao(finds[0], get, 5)
                    litsb, index1 = baiduzhidao(finds[1], get, 10 - index)
                if len(''.join(litsa + litsb)) < 800:
                    addErrorWordFile(find)
                    print("不够800", find)
                    continue
            else:
                print(' <{}> - Baidu data -> {}'.format(ident, f"没有相关搜索 [{find}]"))
                addErrorWordFile(find)
                continue

        # choice_model == 1 or choice_model == 2
        else:
            finds = find.split("|||")
            litsa, index = baiduzhidao(finds[0], get, 5)
            litsb, index1 = baiduzhidao(finds[1], get, 10 - index)
            if len(''.join(litsa + litsb)) < 800:
                print("不够800", find)
                addErrorWordFile(find)
                continue

        if len(litsa + litsb) >= 10:
            datas = re.split('[,，！\t？。|;、：:；.\n ]+', '\n'.join(litsa + litsb))
            datas = [i for i in datas if i != '']
            datas = [i.strip() for i in datas]
            dete = []
            datas = [i for i in datas if len(i) > 1]
            for data in datas:
                if not isChinese(data):
                    dete.append(data)
            try:
                for d in dete:
                    datas.remove(d)
            except:
                pass
            # 解决 后面有数字的情况
            try:
                for w in range(0, len(datas)):
                    data = datas[w]
                    d = data[-3:]
                    if d.isdigit():
                        datas[w] = data[:-3]
                        data = data[:-3]
                    else:
                        d = data[-2:]
                        if d.isdigit():
                            datas[w] = data[:-2]
                            data = data[:-2]
                        else:
                            d = data[-1:]
                            if d.isdigit():
                                datas[w] = data[:-1]
                                data = data[:-1]
            except:
                pass

            datas_temp = []
            for data in datas:
                len_data = len(data)
                if len_data >= split_size:
                    n = int(len_data / 2)
                    # 广告插入
                    datas_temp.append(data[:n])
                    datas_temp.append(data[n:])
                    # datas_temp.append( advertising.Advertising(data[:n],[]) )
                    # datas_temp.append( advertising.Advertising(data[n:],[]) )
                else:
                    datas_temp.append(data)

                    # datas_temp.append(advertising.Advertising(data,[]) )

# ------------------------------------------------------------ #
            '''
            1、文章模式
            2、问答模式
            0、文章模式（百度相关搜索）
            3、问答模式（百度相关搜索）
            '''
# ------------------------------------------------------------ #

            # 文章模式
            if choice_model == 1 or choice_model == 0:
                file_data = FileData(datas_temp, "src.txt", 2)  # 2是图片数量
                file_data.picsrc.num = random.randint(pic_min, pic_max)
                if choice_model == 0:
                    sentence_advertising = SentenceAdvertising()
                    get_d = file_data.get_data_gai0(finds, paragraph_len_max15, paragraph_len_mim15,
                                                    sentence_advertising, advertising)
                else:
                    get_d = file_data.get_data_gai(finds, paragraph_len_max15, paragraph_len_mim15, advertising)

                if get_d:
                    try:
                        name = "%s%s.txt" % (finds[0], random_file_symbol(finds[1]))
                        sets = ['/', '\\', ':', '*', '?', '"', '<', '>', '|']
                        for char in name:
                            if char in sets:
                                name = name.replace(char, '')
                        with open(name, 'w') as f:
                            f.write(get_d.encode("gbk", 'ignore').decode("gbk", "ignore"))
                        print(name)
                    except Exception as e:
                        print(e)
                        pass
                else:
                    print("没有数据", find)
                    addErrorWordFile(find)
            # 问答模式
            elif choice_model == 2 or choice_model == 3:
                name = "%s%s.txt" % (finds[0], random_file_symbol(finds[1]))
                sets = ['/', '\\', ':', '*', '?', '"', '<', '>', '|']
                for char in name:
                    if char in sets:
                        name = name.replace(char, '')

                name = name.replace(' ', '').replace('\n', '').replace('\r', '')
                f = open(name, 'w')
                picsrc.num = random.randint(pic_min, pic_max)
                pics = picsrc.get_pics()
                pics_i = 0
                file_data = FileData(datas_temp, "src.txt", 2)  # 2是图片数量
                mydatas = file_data.get_datass(paragraph_len_max234, paragraph_len_mim234, advertising)
                mydatas = [i for i in mydatas if len(i) > 1]
                data_len = len(mydatas) - 1
                folder_index = 0
                q = 0
                pics_indexs = []
                if data_len <= 1:
                    item_d = mydatas[0]
                    cdata = ""
                    cint = random.randint(0, len(item_d) - 1)
                    cdata += item_d[:cint]
                    cdata += finds[folder_index]
                    cdata += item_d[cint:]
                    item_d = cdata
                    cdata = ""
                    cint = random.randint(0, len(item_d) - 1)
                    cdata += item_d[:cint]
                    cdata += finds[folder_index + 1]
                    cdata += item_d[cint:]
                    mydatas[0] = cdata
                else:
                    try:
                        while True:
                            pics_indexs.append(random.randint(1, data_len))
                            pics_indexs.append(random.randint(1, data_len))
                            if pics_indexs[0] != pics_indexs[1]:
                                break
                            pics_indexs.clear()
                    except Exception as e:
                        print(e)
                        f.close()
                        continue
                if picsrc.num < len(mydatas):
                    sign_indexs = random.sample(mydatas, picsrc.num)
                    bhead = False
                    for i in mydatas:

                        if i == '':
                            continue
                        pic_data = ""
                        if i in sign_indexs:
                            try:
                                pic_data = pics[pics_i]
                                pics_i += 1
                            except:
                                pass
                        if zis.find(i[-1]) == -1:
                            i += "。"
                        elif "。！?".find(i[-1]) == -1:
                            i = i[:-1]
                            i += "。"

                        try:
                            if pics_indexs[0] == q:
                                item_d = i
                                cdata = ""
                                cint = random.randint(0, len(item_d) - 1)
                                post = zisindex(item_d[cint:])
                                cint += post
                                cdata += item_d[:cint]
                                cdata += "，"
                                cdata += finds[folder_index]
                                cdata += item_d[cint:]
                                i = cdata
                            if pics_indexs[1] == q:
                                item_d = i
                                cdata = ""
                                cint = random.randint(0, len(item_d) - 1)
                                post = zisindex(item_d[cint:])
                                cint += post
                                cdata += item_d[:cint]
                                cdata += "，"
                                cdata += finds[folder_index + 1]
                                cdata += item_d[cint:]
                                i = cdata
                        except:
                            pass
                        q += 1
                        i = "<p>" + i + "</p>"
                        shangxia = random.randint(0, 1)
                        if shangxia == 0:
                            i += pic_data
                        else:
                            pic_data += i
                            i = pic_data
                        if not bhead:
                            i = GetHead(i)
                            bhead = True
                        else:
                            i = GetUser(i)
                        f.write(i.encode("gbk", 'ignore').decode("gbk", "ignore"))
                else:
                    mydatas_len2 = (len(mydatas) * 2)
                    if mydatas_len2 < picsrc.num:
                        picsrc.num = mydatas_len2
                    sign_indexs = random.sample(range(mydatas_len2), picsrc.num)

                    bhead = False
                    for data_index, i in enumerate(mydatas):
                        if i == '':
                            continue
                        pic_data = []
                        shangxia = 0
                        for sign in sign_indexs:
                            index = 0
                            if sign:
                                index = (sign / 2)
                            if data_index == index or (data_index + 0.5) == (index):
                                # print(sign)
                                try:
                                    pics[pics_i]
                                    pic_data.append(pics[pics_i])
                                    # f.write(pics[pics_i])
                                    pics_i += 1
                                    # f.write("\n")
                                except Exception as e:
                                    print(e)
                                    pass
                                if sign % 2:
                                    shangxia = 1
                        if zis.find(i[-1]) == -1:
                            i += "。"
                        elif "。！?".find(i[-1]) == -1:
                            i = i[:-1]
                            i += "。"

                        try:
                            if pics_indexs[0] == q:
                                item_d = i
                                cdata = ""
                                cint = random.randint(0, len(item_d) - 1)
                                post = zisindex(item_d[cint:])
                                cint += post
                                cdata += item_d[:cint]
                                cdata += "，"
                                cdata += finds[folder_index]
                                cdata += item_d[cint:]
                                i = cdata
                            if pics_indexs[1] == q:
                                item_d = i
                                cdata = ""
                                cint = random.randint(0, len(item_d) - 1)
                                post = zisindex(item_d[cint:])
                                cint += post
                                cdata += item_d[:cint]
                                cdata += "，"
                                cdata += finds[folder_index + 1]
                                cdata += item_d[cint:]
                                i = cdata
                        except:
                            pass
                        q += 1
                        i = "<p>" + i + "</p>"
                        if len(pic_data) == 2:
                            i += pic_data[0]
                            pic_data[1] += i
                            i = pic_data[1]


                        elif len(pic_data) == 1:
                            if shangxia == 0:
                                i += pic_data[0]
                            if shangxia == 1:
                                pic_data[0] += i
                                i = pic_data[0]
                        if not bhead:
                            i = GetHead(i)
                            bhead = True
                        else:
                            i = GetUser(i)
                        f.write(i.encode("gbk", 'ignore').decode("gbk", "ignore"))

                print(name)
                folder_index += 1
                f.write(GetTail())
                f.close()

            baiduxiangguan(finds[1])
        else:
            print("不够十个", find)
            addErrorWordFile(find)


def run1(file_data):
    global find_infos
    get = MyGet()
    # find_infos = red.get(BAIDU_FIND)
    # find_infos =get_val(find_infos) .
    for find in file_data:
        if find_infos.find(find) != -1:
            print("重复搜索数据", find)
            continue
        # print(find)

        if choice_model == 5:
            finds = []
            finds.append(find)
            # lock.acquire()
            f = baidu(find, get)
            # lock.release()
            if f:
                # print(' <{}> + Baidu data -> {}'.format(ident, f))
                # 保存所以搜索过的问题
                find_infos += find
                red.set(BAIDU_FIND, find_infos)
                finds.append(f)
                # 采集问答
                litsa, index = baiduzhidao(finds[0], get, 5)
                litsb, index1 = baiduzhidao(finds[1], get, 10 - index)
                if len(''.join(litsa + litsb)) < 700:
                    addErrorWordFile(find)
                    print("不够700", find)
                    continue
            else:
                # print(' <{}> - Baidu data -> {}'.format(ident, f"没有相关搜索 [{find}]"))
                addErrorWordFile(find)
                continue
        else:
            finds = find.split("|||")
            litsa, index = baiduzhidao1(finds[0], get, 5)
            litsb, index1 = baiduzhidao1(finds[1], get, 10 - index)
            if len(''.join(litsa + litsb)) < 700:
                print("不够700", find)
                addErrorWordFile(find)
                continue

        if len(litsa + litsb) >= 10:
            datas = re.split('[,，！\t？。|;、：:；.\n ]+', '\n'.join(litsa + litsb))
            datas = [i for i in datas if i != '']
            datas = [i.strip() for i in datas]
            dete = []
            datas = [i for i in datas if len(i) > 1]
            for data in datas:
                if not isChinese(data):
                    dete.append(data)
            try:
                for d in dete:
                    datas.remove(d)
            except:
                pass
            # 解决 后面有数字的情况
            try:
                for w in range(0, len(datas)):
                    data = datas[w]
                    d = data[-3:]
                    if d.isdigit():
                        datas[w] = data[:-3]
                        data = data[:-3]
                    else:
                        d = data[-2:]
                        if d.isdigit():
                            datas[w] = data[:-2]
                            data = data[:-2]
                        else:
                            d = data[-1:]
                            if d.isdigit():
                                datas[w] = data[:-1]
                                data = data[:-1]
            except:
                pass
            datas_temp = []
            for data in datas:
                len_data = len(data)
                if len_data >= split_size:
                    n = int(len_data / 2)
                    datas_temp.append(data[:n])
                    datas_temp.append(data[n:])
                else:
                    datas_temp.append(data)

            # 插入单词文章模式
            if choice_model == 5:
                data = fenge(",".join(datas_temp), sentence_fenge_size)
                data, listjic = GetSuijics(data, bunengcharu)  # 中间插入
                listjic += bunengcharu
                data = advertising.Advertisings(data, listjic)  # 广告插入
                data = GetZhongjianc(data)  # 插入句子
                data = GetTihuanc(data)  # 替换词
                datas = re.split('[,，！\t？。|;、：:；.\n ]+', data)
                datas = [i for i in datas if i != '']
                datas = [i.strip() for i in datas]
                mydatas = [i for i in datas if len(i) > 1]

                file_data = FileData(mydatas, "src.txt", 2)  # 2是图片数量
                file_data.picsrc.num = random.randint(pic_min, pic_max)

                sentence_advertising = SentenceAdvertising(listjic)
                # before_advertising = BeforeAdvertising(listjic)
                get_d = file_data.get_data5(finds, paragraph_len_max15, paragraph_len_mim15,
                                            sentence_advertising)
                if get_d:
                    get_d = GetTihuanc(get_d)  # 替换词
                    try:
                        name = "%s%s.txt" % (finds[0], random_file_symbol(finds[1]))

                        sets = ['/', '\\', ':', '*', '?', '"', '<', '>', '|']
                        for char in name:
                            if char in sets:
                                name = name.replace(char, '')

                        with open(name, 'w') as f:
                            f.write(get_d.encode("gbk", 'ignore').decode("gbk", "ignore"))
                        print(name)
                    except Exception as e:
                        print(e)
                        pass
                else:
                    print("没有数据", find)
                    addErrorWordFile(find)
            elif choice_model == 4:
                data = fenge(",".join(datas_temp), sentence_fenge_size)
                data, listjic = GetSuijics(data, bunengcharu)
                listjic += bunengcharu
                data = advertising.Advertisings(data, listjic)
                data = GetZhongjianc(data)
                data = GetTihuanc(data)
                picsrc.num = random.randint(pic_min, pic_max)
                pics = picsrc.get_pics()
                pics_i = 0

                name = "%s%s.txt" % (finds[0], random_file_symbol(finds[1]))
                sets = ['/', '\\', ':', '*', '?', '"', '<', '>', '|']
                for char in name:
                    if char in sets:
                        name = name.replace(char, '')
                f = open(name, 'w')
                datas = re.split('[,，！\t？。|;、：:；.\n ]+', data)
                datas = [i for i in datas if i != '']
                datas = [i.strip() for i in datas]
                dete = []
                mydatas = [i for i in datas if len(i) > 1]

                file_data = FileData(mydatas, "src.txt", 2)  # 2是图片数量
                mydatas = file_data.get_datas(paragraph_len_max234, paragraph_len_mim234)
                mydatas = [i for i in mydatas if len(i) > 1]
                data_len = len(mydatas) - 1
                folder_index = 0
                q = 0
                pics_indexs = []
                if data_len <= 1:
                    item_d = mydatas[0]
                    cdata = ""
                    cint = random.randint(0, len(item_d) - 1)
                    post = zisindex(item_d[:cint])
                    cint += post
                    cdata += item_d[:cint]
                    cdata += finds[folder_index]
                    cdata += item_d[cint:]
                    item_d = cdata

                    cdata = ""
                    cint = random.randint(0, len(item_d) - 1)
                    post = zisindex(item_d[:cint])
                    cint += post
                    cdata += item_d[:cint]
                    cdata += finds[folder_index + 1]
                    cdata += item_d[cint:]
                    mydatas[0] = cdata
                else:
                    try:
                        while True:
                            pics_indexs.append(random.randint(1, data_len))
                            pics_indexs.append(random.randint(1, data_len))
                            if pics_indexs[0] != pics_indexs[1]:
                                break
                            pics_indexs.clear()
                    except Exception as e:
                        print(e)
                        f.close()
                        continue
                if picsrc.num < len(mydatas):
                    sign_indexs = random.sample(mydatas, picsrc.num)
                    bhead = False
                    for i in mydatas:
                        if i == '':
                            continue
                        pic_data = ""
                        if i in sign_indexs:
                            try:
                                pic_data = pics[pics_i]
                                pics_i += 1
                            except:
                                pass
                        if zis.find(i[-1]) == -1:
                            i += "。"
                        elif "。！?".find(i[-1]) == -1:
                            i = i[:-1]
                            i += "。"
                        try:
                            if pics_indexs[0] == q:
                                item_d = i
                                cdata = ""
                                cint = random.randint(0, len(item_d) - 1)
                                post = zisindex(item_d[cint:])
                                cint += post
                                cdata += item_d[:cint]
                                cdata += "，"
                                cdata += finds[folder_index]
                                cdata += item_d[cint:]
                                i = cdata
                            if pics_indexs[1] == q:
                                item_d = i
                                cdata = ""
                                cint = random.randint(0, len(item_d) - 1)
                                post = zisindex(item_d[cint:])
                                cint += post
                                cdata += item_d[:cint]
                                cdata += "，"
                                cdata += finds[folder_index + 1]
                                cdata += item_d[cint:]
                                i = cdata
                        except:
                            pass
                        q += 1
                        i = "<p>" + i + "</p>"
                        shangxia = random.randint(0, 1)
                        if shangxia == 0:
                            i += pic_data
                        else:
                            pic_data += i
                            i = pic_data
                        if not bhead:
                            i = GetHead(i)
                            bhead = True
                        else:
                            i = GetUser(i)
                        i = GetTihuanc(i)  # 替换词
                        f.write(i.encode("gbk", 'ignore').decode("gbk", "ignore"))
                else:
                    mydatas_len2 = (len(mydatas) * 2)
                    if mydatas_len2 < picsrc.num:
                        picsrc.num = mydatas_len2
                    sign_indexs = random.sample(range(mydatas_len2), picsrc.num)

                    bhead = False
                    for data_index, i in enumerate(mydatas):
                        # for i in mydatas:
                        if i == '':
                            continue
                        pic_data = []
                        shangxia = 0
                        for sign in sign_indexs:
                            index = 0
                            if sign:
                                index = int(sign / 2)
                                index += sign % 2

                            if data_index == index:
                                try:
                                    pics[pics_i]
                                    pic_data.append(pics[pics_i])
                                    # f.write(pics[pics_i])
                                    pics_i += 1
                                    # f.write("\n")
                                except:
                                    pass
                                if sign % 2:
                                    shangxia = 1
                        if zis.find(i[-1]) == -1:
                            i += "。"
                        elif "。！?".find(i[-1]) == -1:
                            # if i in abc:
                            #     print()
                            i = i[:-1]
                            i += "。"

                        try:
                            if pics_indexs[0] == q:
                                item_d = i
                                cdata = ""
                                cint = random.randint(0, len(item_d) - 1)
                                post = zisindex(item_d[cint:])
                                cint += post
                                cdata += item_d[:cint]
                                cdata += "，"
                                cdata += finds[folder_index]
                                cdata += item_d[cint:]
                                i = cdata
                            if pics_indexs[1] == q:
                                item_d = i
                                cdata = ""
                                cint = random.randint(0, len(item_d) - 1)
                                post = zisindex(item_d[cint:])
                                cint += post
                                cdata += item_d[:cint]
                                cdata += "，"
                                cdata += finds[folder_index + 1]
                                cdata += item_d[cint:]
                                i = cdata
                        except:
                            pass
                        i = "<p>" + i + "</p>"
                        q += 1
                        # 上下检测
                        # shangxia = random.randint(0, 1)
                        if len(pic_data) == 2:
                            i += pic_data[0]
                            pic_data[1] += i
                            i = pic_data[1]

                        elif len(pic_data) == 1:
                            if shangxia == 0:
                                i += pic_data[0]
                            if shangxia == 1:
                                pic_data[0] += i
                                i = pic_data[0]
                        if not bhead:
                            i = GetHead(i)
                            bhead = True
                        else:
                            i = GetUser(i)
                        f.write(i.encode("gbk", 'ignore').decode("gbk", "ignore"))

                print(name)

                f.write(GetTail())
                f.close()
            baiduxiangguan(finds[1])
        else:
            print("不够十个", find)
            addErrorWordFile(find)


if __name__ == '__main__':
    suijic = getFileData("中间关键词.txt")
    shuffle(suijic)
    file_datas = getFileData("查找词.txt")
    if choice_model == 3 or choice_model == 0 or choice_model == 5:
        file_data = file_datas
    else:
        fflen = int(len(file_datas) / 2)
        file_data = []
        for f1 in range(fflen):
            file_data.append('%s|||%s' % (file_datas[f1 * 2], file_datas[f1 * 2 + 1]))

    split_size = 22  # 这里修改句子的 最大长度
    cun_index = 5
    cuu = len(file_data) / cun_index

    jobs = []
    cuu = int(cuu)
    for i in range(cun_index):
        datas = []
        if i + 1 == cun_index:
            datas = (file_data[i * cuu:])
        else:
            datas = (file_data[i * cuu:i * cuu + cuu])

        print('All data -> {} '.format(datas))
        if choice_model <= 3:
            # model: 0, 1, 2, 3
            job = gevent.spawn(run, datas)
        else:
            # model: 4, 5
            job = gevent.spawn(run1, datas)

        jobs.append(job)

    print('jobs-->', len(jobs))
    gevent.joinall(jobs)
