# ~*~ coding: utf-8 ~*~
import re
from random import shuffle
import random

index = 0

# 最小插入广告数数量
min_ad_count = 3
# 最大插入广告数数量
max_ad_count = 3

min_paragraph_count = 13
max_paragraph_count = 24


class Picsrc:
    def __init__(self, url, num):
        super().__init__()
        self.datas = self.getFileData(url)
        self.num = num
        self.num_cur = 0
        self.datas_idnex = 0
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
        if self.datas_len >= self.datas_idnex:
            self._shuffle()
        if self.datas_len >= (self.datas_idnex + self.num):
            self._shuffle()

        ret = self.datas[self.datas_idnex:self.datas_idnex + self.num]
        self.datas_idnex += self.num
        return ret


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


dete_list = getFileData("删除.txt")


def is_Chinese(ch):
    if '\u4e00' <= ch <= '\u9fff':
        return True
    if ch.isalnum():
        return False
    return False


def insert_search_str(ori_str, search_str):
    ori_list = ori_str.split('，')
    if len(ori_list) == 1:
        ori_list.insert(0, search_str)
    else:
        idx = random.randint(1, len(ori_list) - 1)
        ori_list.insert(idx, search_str)
    return '，'.join(ori_list)


def get_ad_index(rows):
    ad_count = random.randint(min_ad_count, max_ad_count)
    if len(rows) < ad_count:
        ad_count = len(rows)

    ad_index = []
    while ad_count > 0:
        idx = random.randint(0, len(rows) - 1)
        if idx not in ad_index:
            ad_index.append(idx)
            ad_count -= 1

    return sorted(ad_index)


def pt(als):
    for a in als:
        print(a)
        al = a.split('，')
        al2 = list(set(al))
        print(len(al), '==', len(al2))


def process_min_sentence(aa, n_min):
    size = []
    idx = []
    for i, a in enumerate(aa):
        if len(a) < n_min:
            size.append(999999999)  # 站位
            idx.append(i)
        else:
            size.append(len(a))
    xx = sorted(size)[0:len(idx)]
    idx2 = [size.index(x) for x in xx]
    swap = list(zip(idx, idx2))
    nls = []
    for k, k2 in swap:
        nl = aa[k].strip('。') + '，' + aa[k2].strip('。') + '。'
        nls.append(nl)

    for o in idx + idx2:
        aa[o] = None

    aa.extend(nls)
    final = [a for a in aa if a is not None]

    return final


# 文件合成
class FileData:
    def __init__(self, datas, url, num):
        super().__init__()
        self.paragraph_min = 10
        self.paragraph_max = 15
        self.paragraph_cur = 0
        self.paragraph_len_max = 500
        self.paragraph_len_mim = 20
        self.datas = list(set(datas))
        self.picsrc = Picsrc(url, num)
        self.is_data = False

    def huoqushif(self, data_str):
        tr = data_str[-1]
        if tr == "。" or \
                tr == "？" or tr == "！":
            data_str += ''
        elif is_Chinese(data_str[-1]):
            data_str += '。'
        elif tr == "." or tr == ',' or tr == '：' or tr == '，' or tr == '、' or tr == ';' or tr == '；':
            data_str = data_str[:-1] + '。'
        else:
            data_str += '。'
        return data_str

    # 随机
    def shuffle_datas(self):
        shuffle(self.datas)

    # 随机段落
    def shuffle_paragraph(self):
        self.paragraph_cur = random.randint(min_paragraph_count, max_paragraph_count)

    # 标记段落
    def sign_paragraph(self):
        alen = len(self.datas)
        self.sign_indexs = random.sample(range(0, alen), self.paragraph_cur)

    def get_tail(self):
        d = random.randint(0, 2)
        a = ["，", "，", "，"]
        return a[d]

    def ge(self, data_paragraph):
        if not data_paragraph:
            return data_paragraph
        if is_Chinese(data_paragraph[-1]):
            data_paragraph += self.get_tail()
        else:
            data_paragraph = data_paragraph[:-1] + self.get_tail()
        return data_paragraph

    def get_data(self, fs, n_max, n_min, sentence_advertising):
        self.paragraph_len_max = n_max
        self.paragraph_len_mim = n_min
        if not self.is_data:
            self.shuffle_datas()
        self.shuffle_paragraph()
        inde = 0
        pics = self.picsrc.get_pics()
        qstr = '<p style="text-indent:2em;">'
        if self.picsrc.num > self.paragraph_cur:
            self.picsrc.num = self.paragraph_cur
        while True:
            self.sign_paragraph()
            pics_idnex = 0
            pics_indexs = random.sample(self.sign_indexs, self.picsrc.num)
            # 图片的
            data_str = ""
            data_paragraph = ''
            bpic = False
            for data_index, data in enumerate(self.datas):

                if data_index in pics_indexs:
                    if not bpic:
                        if pics_idnex < len(pics):
                            data_str += pics[pics_idnex]
                            data_str += "\n"
                            pics_idnex += 1
                            bpic = True

                b = False
                if data_index in self.sign_indexs:  #
                    data_paragraph_len = len(data_paragraph)
                    if data_paragraph_len < self.paragraph_len_mim:
                        data_paragraph += (data)
                        data_paragraph = self.ge(data_paragraph)
                        continue
                    if data_paragraph_len > self.paragraph_len_max:
                        data_paragraphs = re.split('[,，？。、|：；.\n]+', data_paragraph)
                        dlen = int(len(data_paragraphs) / 2)
                        for i in range(dlen):
                            data_str += data_paragraphs[i]
                            if i + 1 == dlen:
                                data_str = self.ge(data_str)
                                data_str = data_str[:-1] + '。\n'
                            else:
                                data_str += self.get_tail()
                        for i in data_paragraphs[dlen:]:
                            data_str += i
                            if i == data_paragraphs[len(data_paragraphs) - 1]:
                                data_str = self.ge(data_str)
                                data_str = data_str[:-1] + '。\n'
                            else:
                                data_str += self.get_tail()

                        data_paragraph = ""
                        b = True
                    else:
                        data_str += data_paragraph
                        data_paragraph = ""
                        data_paragraph += (data)
                        data_paragraph = self.ge(data_paragraph)
                        data_str = data_str[:-1] + '。\n'
                        b = True

                if b:
                    bpic = False
                    continue
                data_paragraph += (data)
                data_paragraph = self.ge(data_paragraph)

            if data_paragraph:
                data_str += data_paragraph
                data_str = data_str[:-1] + '。\n'

            if pics_idnex < len(pics):
                data_str += pics[pics_idnex]
                data_str += "\n"
                pics_idnex += 1
            n = data_str.count("\n")
            if n >= 8:
                break
            inde += 1
            if inde >= 3:
                break

        data_strs = data_str.split('\n')
        data_strs = [i for i in data_strs if i != '']
        data_strs = process_min_sentence(data_strs, n_min)

        strs_len = len(data_strs) - 1
        bsrandom = []
        while True:
            b1 = random.randint(1, strs_len)
            b2 = random.randint(1, strs_len)
            sb = abs(b2 - b1)
            if sb > 1:
                bsrandom.append(b1)
                bsrandom.append(b2)
                break

        fs_idnex = 0
        # 获取插入广告的索引
        ad_index = get_ad_index(data_strs)
        final_data = ''
        for i, data in enumerate(data_strs):
            data_max = ""
            b = False
            for q in bsrandom:
                if i == q:
                    # data_max += qstr + '<strong>{}</strong>\n'.format(fs[fs_idnex])
                    data = insert_search_str(data, fs[fs_idnex])
                    fs_idnex += 1
                    break
            for dd in pics:
                if data.find(dd) != -1:
                    b = True
                    break
            if b:
                data_max += data
                data_max += "\n"
            else:
                for dete in dete_list:
                    data = data.replace(dete, '')
                data_max += qstr
                data_max += data

                if i in ad_index:
                    data_max = sentence_advertising.Advertising(data_max)

                data_max += "\n"

            final_data += data_max
        return final_data

    def get_data_gai0(self, fs, n_max, n_min, sentence_advertising, advertising):
        self.paragraph_len_max = n_max
        self.paragraph_len_mim = n_min
        if not self.is_data:
            self.shuffle_datas()
        self.shuffle_paragraph()
        inde = 0
        pics = self.picsrc.get_pics()
        qstr = '<p style="text-indent:2em;">'
        if self.picsrc.num > self.paragraph_cur:
            self.picsrc.num = self.paragraph_cur
        while True:
            self.sign_paragraph()
            pics_idnex = 0
            pics_indexs = random.sample(self.sign_indexs, self.picsrc.num)
            # 图片的
            data_str = ""
            data_paragraph = ''
            bpic = False
            for data_index, data in enumerate(self.datas):

                if data_index in pics_indexs:
                    if not bpic:
                        if pics_idnex < len(pics):
                            data_str += pics[pics_idnex]
                            data_str += "\n"
                            pics_idnex += 1
                            bpic = True

                b = False
                if data_index in self.sign_indexs:  #
                    data_paragraph_len = len(data_paragraph)
                    if data_paragraph_len < self.paragraph_len_mim:
                        data_paragraph += (data)
                        data_paragraph = self.ge(data_paragraph)
                        continue
                    if data_paragraph_len > self.paragraph_len_max:
                        data_paragraphs = re.split('[,，？。、|：；.\n]+', data_paragraph)
                        dlen = int(len(data_paragraphs) / 2)
                        for i in range(dlen):
                            data_str += data_paragraphs[i]
                            if i + 1 == dlen:
                                data_str = self.ge(data_str)
                                data_str = data_str[:-1] + '。\n'
                            else:
                                data_str += self.get_tail()
                        for i in data_paragraphs[dlen:]:
                            data_str += i
                            if i == data_paragraphs[len(data_paragraphs) - 1]:
                                data_str = self.ge(data_str)
                                data_str = data_str[:-1] + '。\n'
                            else:
                                data_str += self.get_tail()

                        data_paragraph = ""
                        b = True
                    else:
                        data_str += data_paragraph
                        data_paragraph = ""
                        data_paragraph += (data)
                        data_paragraph = self.ge(data_paragraph)
                        data_str = data_str[:-1] + '。\n'
                        b = True

                if b:
                    bpic = False
                    continue
                data_paragraph += (data)
                data_paragraph = self.ge(data_paragraph)

            if data_paragraph:
                data_str += data_paragraph
                data_str = data_str[:-1] + '。\n'

            if pics_idnex < len(pics):
                data_str += pics[pics_idnex]
                data_str += "\n"
                pics_idnex += 1

            n = data_str.count("\n")
            if n >= 8:
                break
            inde += 1
            if inde >= 3:
                break

        data_strs = data_str.split('\n')
        data_strs = [i for i in data_strs if i != '']
        data_strs = process_min_sentence(data_strs, n_min)

        strs_len = len(data_strs) - 1
        bsrandom = []
        while True:
            b1 = random.randint(1, strs_len)
            b2 = random.randint(1, strs_len)
            sb = abs(b2 - b1)
            if sb > 1:
                bsrandom.append(b1)
                bsrandom.append(b2)
                break

        # 生成了段落 - data_strs
        fs_idnex = 0
        ad_index = get_ad_index(data_strs)
        final_data = ''
        for i, data in enumerate(data_strs):
            data_max = ""
            b = False
            for q in bsrandom:
                if i == q:
                    # data_max += qstr + '<strong>{}</strong>\n'.format(fs[fs_idnex])
                    data = insert_search_str(data, fs[fs_idnex])
                    fs_idnex += 1
                    break
            for dd in pics:
                if data.find(dd) != -1:
                    b = True
                    break
            if b:
                data_max += data
                data_max += "\n"
            else:
                for dete in dete_list:
                    data = data.replace(dete, '')
                data_max += qstr
                data_max += advertising.Advertising(data)

                if i in ad_index:
                    data_max = sentence_advertising.Advertising(data_max)

                data_max += "\n"
            final_data += data_max
        return final_data

    def get_data_gai(self, fs, n_max, n_min, advertising):
        self.paragraph_len_max = n_max
        self.paragraph_len_mim = n_min
        if not self.is_data:
            self.shuffle_datas()
        self.shuffle_paragraph()
        inde = 0
        pics = self.picsrc.get_pics()
        qstr = '<p style="text-indent:2em;">'
        if self.picsrc.num > self.paragraph_cur:
            self.picsrc.num = self.paragraph_cur
        while True:
            self.sign_paragraph()
            pics_idnex = 0
            pics_indexs = random.sample(self.sign_indexs, self.picsrc.num)
            # 图片的
            data_str = ""
            data_paragraph = ''
            bpic = False
            for data_index, data in enumerate(self.datas):

                if data_index in pics_indexs:
                    if not bpic:
                        if pics_idnex < len(pics):
                            data_str += pics[pics_idnex]
                            data_str += "\n"
                            pics_idnex += 1
                            bpic = True

                b = False
                if data_index in self.sign_indexs:  #
                    data_paragraph_len = len(data_paragraph)
                    if data_paragraph_len < self.paragraph_len_mim:
                        data_paragraph += (data)
                        data_paragraph = self.ge(data_paragraph)
                        continue
                    if data_paragraph_len > self.paragraph_len_max:
                        data_paragraphs = re.split('[,，？。、|：；.\n]+', data_paragraph)
                        dlen = int(len(data_paragraphs) / 2)
                        for i in range(dlen):
                            data_str += data_paragraphs[i]
                            if i + 1 == dlen:
                                data_str = self.ge(data_str)
                                data_str = data_str[:-1] + '。\n'
                            else:
                                data_str += self.get_tail()
                        for i in data_paragraphs[dlen:]:
                            data_str += i
                            if i == data_paragraphs[len(data_paragraphs) - 1]:
                                data_str = self.ge(data_str)
                                data_str = data_str[:-1] + '。\n'
                            else:
                                data_str += self.get_tail()

                        data_paragraph = ""
                        b = True
                    else:
                        data_str += data_paragraph
                        data_paragraph = ""
                        data_paragraph += (data)
                        data_paragraph = self.ge(data_paragraph)
                        data_str = data_str[:-1] + '。\n'
                        b = True

                if b:
                    bpic = False
                    continue
                data_paragraph += (data)
                data_paragraph = self.ge(data_paragraph)

            if data_paragraph:
                data_str += data_paragraph
                data_str = data_str[:-1] + '。\n'

            if pics_idnex < len(pics):
                data_str += pics[pics_idnex]
                data_str += "\n"
                pics_idnex += 1

            n = data_str.count("\n")
            if n >= 8:
                break
            inde += 1
            if inde >= 3:
                break

        data_max = ""
        data_strs = data_str.split('\n')
        data_strs = [i for i in data_strs if i != '']
        strs_len = len(data_strs) - 1
        bsrandom = []
        while True:
            b1 = random.randint(1, strs_len)
            b2 = random.randint(1, strs_len)
            sb = abs(b2 - b1)
            if sb > 1:
                bsrandom.append(b1)
                bsrandom.append(b2)
                break

        # 生成了段落 - data_strs
        fs_idnex = 0
        for i, data in enumerate(data_strs):
            b = False
            for q in bsrandom:
                if i == q:
                    # data_max += qstr + '<strong>{}</strong>\n'.format(fs[fs_idnex])
                    data = insert_search_str(data, fs[fs_idnex])
                    fs_idnex += 1
                    break
            for dd in pics:
                if data.find(dd) != -1:
                    b = True
                    break
            if b:
                data_max += data
                data_max += "\n"
            else:
                for dete in dete_list:
                    data = data.replace(dete, '')
                data_max += qstr
                data_max += advertising.Advertising(data)
                data_max += "\n"
        return data_max

    def get_datas(self, n_max, n_min):
        self.paragraph_len_max = n_max
        self.paragraph_len_mim = n_min
        inde = 0
        zis = ',，！!\t？?。|;、：:；\n '
        while True:
            self.shuffle_paragraph()
            self.sign_paragraph()
            data_str = ""
            data_paragraph = ''

            for data_index, data in enumerate(self.datas):
                b = False

                if data_index in self.sign_indexs:  #
                    # self.sign_indexs.remove(data)
                    data_paragraph_len = len(data_paragraph)
                    if data_paragraph_len < self.paragraph_len_mim:
                        data_paragraph += (data)
                        data_paragraph = self.ge(data_paragraph)
                        continue
                    if data_paragraph_len > self.paragraph_len_max:
                        print(len(data_paragraph))
                        data_paragraphs = re.split('[,，？。、|：；.\n]+', data_paragraph)
                        dlen = int(len(data_paragraphs) / 2)
                        for i in range(dlen):
                            data_str += data_paragraphs[i]
                            if i + 1 == dlen:
                                if zis.find(data_str[-1]) != -1:
                                    data_str = self.ge(data_str)
                                    data_str = data_str[:-1] + '。\n'
                                else:
                                    data_str += '。\n'
                            else:
                                data_str += self.get_tail()
                        for i in data_paragraphs[dlen:]:
                            data_str += i
                            if i == data_paragraphs[len(data_paragraphs) - 1]:
                                if zis.find(data_str[-1]) != -1:
                                    data_str = self.ge(data_str)
                                    data_str = data_str[:-1] + '。\n'
                                else:
                                    data_str += '。\n'
                            else:
                                data_str += self.get_tail()
                        data_paragraph = ""
                        b = True
                    else:
                        data_str += data_paragraph
                        data_paragraph = ""
                        data_paragraph += (data)
                        data_paragraph = self.ge(data_paragraph)
                        # print(data_str[-6:-1])

                        data_str = data_str[:-1] + '。\n'

                        b = True
                if b:
                    continue

                data_paragraph += (data)
                data_paragraph = self.ge(data_paragraph)
            if data_paragraph:
                data_paragraph = self.ge(data_paragraph)
                data_str += data_paragraph
                data_str = data_str[:-1] + '。\n'
            n = data_str.count("\n")
            if n >= 8:
                break

            inde += 1
            if inde >= 5:
                break

        for dete in dete_list:
            data_str = data_str.replace(dete, '')
        list_t = data_str.split("\n")
        list_t = [i for i in list_t if len(i) > 1]
        if len(list_t[-1]) < 100:
            a = list_t[-1] + list_t[-2]
            list_t[-2] = a
            list_t = list_t[:-1]

        return list_t

    def get_datasss(self, n_max, n_min, advertising):
        self.paragraph_len_max = n_max
        self.paragraph_len_mim = n_min
        inde = 0
        zis = ',，！!\t？?。|;、：:；\n '
        while True:
            self.shuffle_paragraph()
            self.sign_paragraph()
            data_str = ""
            data_paragraph = ''

            for data_index, data in enumerate(self.datas):
                b = False

                if data_index in self.sign_indexs:  #
                    # self.sign_indexs.remove(data)
                    data_paragraph_len = len(data_paragraph)
                    if data_paragraph_len < self.paragraph_len_mim:
                        # data_paragraph +=      advertising.Advertising(data_paragraph)
                        data_paragraph = self.ge(data_paragraph)
                        continue
                    if data_paragraph_len > self.paragraph_len_max:
                        print(len(data_paragraph))
                        data_paragraphs = re.split('[,，？。、|：；.\n]+', data_paragraph)
                        dlen = int(len(data_paragraphs) / 2)
                        for i in range(dlen):
                            data_paragraphs[i] = advertising.Advertising(data_paragraphs[i])
                            data_str += data_paragraphs[i]
                            if i + 1 == dlen:
                                if zis.find(data_str[-1]) != -1:

                                    data_str = self.ge(data_str)
                                    data_str = data_str[:-1] + '。\n'
                                else:
                                    data_str += '。\n'
                            else:
                                data_str += self.get_tail()
                        for i in data_paragraphs[dlen:]:
                            data_str += i
                            if i == data_paragraphs[len(data_paragraphs) - 1]:
                                if zis.find(data_str[-1]) != -1:
                                    data_str = self.ge(data_str)
                                    data_str = data_str[:-1] + '。\n'
                                else:
                                    data_str += '。\n'
                            else:
                                data_str += self.get_tail()
                        data_paragraph = ""
                        b = True
                    else:
                        data_paragraph = advertising.Advertising(data_paragraph)
                        data_str += data_paragraph
                        data_paragraph = ""
                        data_paragraph += (data)
                        data_paragraph = self.ge(data_paragraph)
                        # print(data_str[-6:-1])

                        data_str = data_str[:-1] + '。\n'

                        b = True
                if b:
                    continue

                data_paragraph += (data)
                data_paragraph = self.ge(data_paragraph)
            if data_paragraph:
                data_paragraph = self.ge(data_paragraph)
                data_paragraph = advertising.Advertising(data_paragraph)
                data_str += data_paragraph
                data_str = data_str[:-1] + '。\n'
            n = data_str.count("\n")
            if n >= 8:
                break

            inde += 1
            if inde >= 5:
                break

        for dete in dete_list:
            data_str = data_str.replace(dete, '')
        list_t = data_str.split("\n")
        list_t = [i for i in list_t if len(i) > 1]
        if len(list_t[-1]) < 100:
            a = list_t[-1] + list_t[-2]
            list_t[-2] = a
            list_t = list_t[:-1]

        return list_t

    def get_datass(self, n_max, n_min, advertising):
        self.shuffle_datas()
        return self.get_datasss(n_max, n_min, advertising)

    def get_data5(self, fs, n_max, n_min, sentence_advertising):
        self.is_data = True
        ret = self.get_data(fs, n_max, n_min, sentence_advertising)
        self.is_data = False
        return ret


def getTail():
    d = random.randint(0, 3)
    a = ["：", "，", "；", "\n"]
    return a[d]
