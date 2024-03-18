
# 合并数据
def intoList(endList,startList):
    if(len(startList)>1):
        startList=[",".join(startList)]
    if startList:
        endList.extend(startList)
    else:
        endList.append("NaN")# Nan代表空值

# 数据解析提取
def infoParse(infoDatas):
    authorList = []
    titleList = []
    venueList = []
    volumeList = []
    pagesList = []
    yearList = []
    keyList = []
    typeList = []
    accessList = []
    keyList = []
    doiList = []
    eeList = []
    urlList = []
    print("开始解析数据")
    for info in infoDatas:
        intoList(authorList, info.xpath("./info//author/text()"))
        intoList(titleList, info.xpath("./info//title/text()"))
        intoList(venueList, info.xpath("./info//venue/text()"))
        intoList(volumeList, info.xpath("./info//volume/text()"))
        intoList(pagesList, info.xpath("./info//pages/text()"))
        intoList(yearList, info.xpath("./info//year/text()"))
        intoList(typeList, info.xpath("./info//type/text()"))
        intoList(accessList, info.xpath("./info//access/text()"))
        intoList(keyList, info.xpath("./info//key/text()"))
        intoList(doiList, info.xpath("./info//doi/text()"))
        intoList(eeList, info.xpath("./info//ee/text()"))
        intoList(urlList, info.xpath("./info//url/text()"))

    # 将数据列表存入字典
    infoDict = {
        "author": authorList,
        "title": titleList,
        "vennue": venueList,
        "volume": volumeList,
        "pages": pagesList,
        "year": yearList,
        "type": typeList,
        "access": accessList,
        "key": keyList,
        "doi": doiList,
        "ee": eeList,
        "url": urlList
    }
    print("解析完成，开始写入数据")
    return infoDict

# infoParse(text)
# data=etree.parse("test.xml")
# print(data)
# text=data.xpath(".//hits/hit")
# total=data.xpath(".//hits/@total")[0]
# print(total)
# print(len(text))