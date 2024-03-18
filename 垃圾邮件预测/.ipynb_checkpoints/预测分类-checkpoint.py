import jieba
from sklearn.feature_extraction.text import TfidfVectorizer
def tokenizer_jieba(line):
    # 结巴分词
    return [li for li in jieba.cut(line) if li.strip() != '']

def get_data_tf_idf(email_file_name):
    # 通过jieba分词，创造tfidf词频空间向量
    vectoring = TfidfVectorizer(input='content', tokenizer=tokenizer_jieba, analyzer='word')
    content = open(email_file_name, 'r', encoding='utf8').readlines()
    x = vectoring.fit_transform(content)
    return x, vectoring


from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
import numpy as np
def get_label_list(label_file_name): #获取标签列表
    content = open(label_file_name, 'r', encoding='utf8').readlines()
    return content
if __name__ == "__main__":
    np.random.seed(1)
    email_file_name = 'content.txt'
    label_file_name = 'labels.txt'
    x, vectoring = get_data_tf_idf(email_file_name)
    y = get_label_list(label_file_name)
    y = np.array(y)

    # 随机打乱所有样本
    index = np.arange(len(y))
    np.random.shuffle(index)
    x = x[index]
    y = y[index]

    # 划分训练集和测试集
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

    mlp = MLPClassifier()
    mlp.fit(x_train, y_train)
    y_pred = mlp.predict(x_test)
    print('Accuracy:', metrics.accuracy_score(y_test, y_pred))
