'''
TODO 实现对DBLP的爬取功能和类别
'''
# 样例https://dblp.dagstuhl.de/search/publ/inc?q=computer&h=200&f=0

'''
DBLPApi
https://dblp.org/search/publ/api for publication queries
https://dblp.org/search/author/api for author queries
https://dblp.org/search/venue/api for venue queries

https://dblp.org/search/publ/api?q=internet&format=json&h=10&b=3
'''
import requests,math,time
from lxml import etree
from userAgents import ua
from xmlParse import infoParse
from fileOperate import writeToCsv,judgeSearchType


startUrl="https://dblp.org/search/publ/api?format=xml&h=40&q="

# 获取关键词的总数
def firstRequest(startUrl,question,wantDataTotal=2000):
        hearder = {
            "User-Agent": ua.random
        }
        requestsUrl=startUrl+question+f"&f=0"
        response=requests.get(requestsUrl,hearder)
        # print(response.text)
        # print(type(response.text))
        if(response.status_code==200):
            print("请求成功")
            xmlData=etree.XML(response.content)
            dataTotal = int(xmlData.xpath(".//hits/@total")[0]) # 关键词命中总数
            print(f"该关键词的相关数据有：{dataTotal}条")
            # 防止请求的数目过大，默认设定为2000
            if(dataTotal>wantDataTotal):
                dataTotal=wantDataTotal
                print(f"该关键词的相关数据大于{dataTotal}条，默认爬取最新的{dataTotal}条数据。")
            return dataTotal
        else:
            print("首次请求失败，请稍后重试")
            return -1

# 请求所有的网页
def goToRe(startUrl,question,num):
    hearder = {
        "User-Agent": ua.random
    }
    requestUrl = startUrl + question + f"&f={num}"
    print(f"接下来请求的网址为:{requestUrl}")
    re=requests.get(requestUrl, hearder)
    if(re.status_code==200):
        infoData = infoParse(etree.XML(re.content).xpath(".//hits/hit"))# 完成了数据提取
        return infoData # 返回数据，用于csv的存储
    else:
        print("被封了，换个IP吧")
        return -1


# 请求所有需要的数据
def traversideRequest(startUrl,question,dataTotal,searchType):
    infoData=-1
    # 判断返回的请求是否正确
    if(dataTotal==-1):
        print("失败了")
        return
    # 遍历获取所需要的所有数据
    for i in range(0,math.ceil(dataTotal/40)):
        infoData=goToRe(startUrl,question,i*40)
        if(infoData==-1):
            print("被封了，换个IP吧")
            break
        else:
            writeToCsv(infoData,judgeSearchType(searchType,question))
            time.sleep(1)
            # break
    # 判断数据是否正确
    if(infoData==-1):
        print("没有数据可以写入")
    else:
        print("写入数据完成")

# 运行调用函数
def generalMain(question,searchType,wantDataTotal):
    dataTotal = firstRequest(startUrl, question,wantDataTotal)
    traversideRequest(startUrl, question, dataTotal, searchType)


