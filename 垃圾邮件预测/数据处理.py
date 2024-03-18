import re
import jieba
import codecs
import os
# 去掉非中文字符

def clean_str(string):
    string = re.sub(r"[^\u4e00-\u9fff]", " ", string)
    string = re.sub(r"\s{2,}", " ", string)
    return string.strip()


def get_data_in_a_file(original_path, save_path='all_email.txt'):
    files = os.listdir(original_path)
    for file in files:
        if os.path.isdir(original_path + '/' + file):
                get_data_in_a_file(original_path + '/' + file, save_path=save_path)
        else:
            email = ''
            f = codecs.open(original_path + '/' + file, 'r', 'gbk', errors='ignore')
            for line in f:
                line = clean_str(line)
                email += line
            f.close()
            f = open(save_path, 'a', encoding='utf8')
            email = [word for word in jieba.cut(email) if word.strip() != '']
            f.write(' '.join(email) + '\n')


get_data_in_a_file('data', save_path='all_email.txt')


def get_label_in_a_file(original_path, save_path='all_email.txt'):
    f = open(original_path, 'r')
    label_list = []
    for line in f:
        # spam
        if line[0] == 's':
            label_list.append('0')
        # ham
        elif line[0] == 'h':
            label_list.append('1')

    f = open(save_path, 'w', encoding='utf8')
    f.write('\n'.join(label_list))
    f.close()


get_label_in_a_file('index', save_path='label.txt')