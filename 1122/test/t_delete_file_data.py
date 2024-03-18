from tkinter.filedialog import askdirectory, askopenfilename
import os


def getFileData(url):
    try:
        with open(url) as f:

            configs = f.read().splitlines()
            return configs
    except  Exception as e:
        print(e)
        pass
    return None


def getData(u):
    try:
        with open(u) as f:
            # configs = f.read().splitlines()
            configs = f.read()
            return configs
            # print(configs)
    except  Exception as e:
        print(e)
        pass
    return None


dete = getFileData("删除.txt")
folder_path = askdirectory()
listDir = os.listdir(folder_path)

for x in listDir:
    if x.find(".txt") != -1:
        data = getData(x)
        for d in dete:
            data = data.replace(d, '')
        try:
            with open(x, 'w') as f:
                f.write(data.encode("gbk", 'ignore').decode("gbk", "ignore"))
        except:
            pass
        print(x)
