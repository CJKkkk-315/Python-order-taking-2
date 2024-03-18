# -*- coding: UTF-8 -*-
import os
from cv2 import cv2# pip install opencv-python
import sys
import numpy as np
from PIL import Image

from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtWidgets

from aip import AipBodyAnalysis
import requests
import base64

""" 你的 APPID AK SK """
APP_ID = '21664164' #申请的ID
API_KEY = '6BmoqUL4LMeGqDPXu3PQgI7p'   #申请的AK
SECRET_KEY = 'lkA3paiFbDCfDFE3bApeLhowg5MafWrH'  #申请的SK

client = AipBodyAnalysis(APP_ID, API_KEY, SECRET_KEY)

fileName_choose=""
dir_choose=""
font = QtGui.QFont()
font.setFamily('微软雅黑')
font.setBold(True)
font.setPointSize(13)
font.setWeight(75)

#  获取 access_token，通行证
def get_access_token():
    """
    获取 access_token
    """
  
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=6BmoqUL4LMeGqDPXu3PQgI7p&client_secret=lkA3paiFbDCfDFE3bApeLhowg5MafWrH'
    response = requests.get(host)
    if response:
        return response.json()['access_token']

# 人像分割处理部分
def get_foreground(originalImagePath,outputpath):
    """
    人像分割
    """
    # 二进制方式打开图片文件
    f = open(originalImagePath, 'rb')
    img = base64.b64encode(f.read())
    # 请求 百度 AI 开放平台
    request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/body_seg?access_token=" + get_access_token()
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    params = {"image": img}
    response = requests.post(request_url, data=params, headers=headers)
    # 保存照片
    try:
        foreground = response.json()['foreground']
        img_data = base64.b64decode(foreground)
        img_path = outputpath # 保存照片地址和名称，修改处
        with open(img_path, 'wb') as f:
            f.write(img_data)
    except:
        pass
def koutu():
        # 图片路径
        path = dir_choose
        # 判断路径是否存在
        if os.path.exists(path):
            files = os.listdir(path)
            for item in files:
                get_foreground(path + "/"+item,str(fileName_choose)+"/"+item)
            # 批量抠图
            print("---- 程序结束 ----")
        else:
            print("输入的路径不存在！！！")
            print("---- 程序结束 ----")
                # 图片路径
        path = fileName_choose

        # 判断路径是否存在
        if os.path.exists(path):
            files = os.listdir(path)
            #imgs = []
            for item in files:
                #img=cv2.imread(path + "/"+item,-1)
                img=cv2.imdecode(np.fromfile(path + "/"+item,dtype=np.uint8),cv2.IMREAD_UNCHANGED)
                print(item)
        print("完成!!!")

class MainForm(QWidget):
    def __init__(self, name = 'MainForm'):
        super(MainForm,self).__init__()
        self.setWindowTitle(name)
        self.cwd = os.getcwd() # 获取当前程序文件位置
        self.resize(400,600)   # 设置窗体大小
        # btn 1
        self.btn_chooseDir = QPushButton(self)
        self.btn_chooseDir.setObjectName("btn_chooseDir")
        self.btn_chooseDir.setText("选择源文件夹")
        self.btn_chooseDir.setFont(font)
        # btn 2
        self.btn_koutu = QPushButton(self)
        self.btn_koutu.setObjectName("btn_chooseFile")
        self.btn_koutu.setText("开始抠图")
        self.btn_koutu.setFont(font)
        # btn 4
        self.btn_saveFile = QPushButton(self)
        self.btn_saveFile.setObjectName("btn_saveFile")
        self.btn_saveFile.setText("选择文件保存目录")
        self.btn_saveFile.setFont(font)
        # 设置布局
        layout = QVBoxLayout()
        layout.addWidget(self.btn_chooseDir)
        layout.addWidget(self.btn_saveFile)
        layout.addWidget(self.btn_koutu)

        layout_h=QHBoxLayout()
        layout.addLayout(layout_h)

        self.setLayout(layout)
        # 设置信号
        self.btn_chooseDir.clicked.connect(self.slot_btn_chooseDir)
        self.btn_koutu.clicked.connect(self.slot_btn_koutu)
        #self.btn_chooseMutiFile.clicked.connect(self.slot_btn_chooseMutiFile)
        self.btn_saveFile.clicked.connect(self.slot_btn_saveFile)

    def slot_btn_chooseDir(self):
        global dir_choose
        dir_choose = QFileDialog.getExistingDirectory(self,
                                    "选取文件夹",
                                    self.cwd) # 起始路径
        if dir_choose == "":
            print("\n取消选择")
            return
        print("\n你选择的文件夹为:")
        print(dir_choose)

    def slot_btn_koutu(self):
        try:
            koutu()
        except Exception as e:
            print(e)





    def slot_btn_saveFile(self):
        global fileName_choose
        fileName_choose= QFileDialog.getExistingDirectory(self,
                                    "选取文件夹",
                                    self.cwd) # 输出路径
        if fileName_choose == "":
            print("\n取消选择")
            return
        print("\n你选择的文件夹为:")
        print(fileName_choose)


if __name__=="__main__":
    app = QApplication(sys.argv)
    mainForm = MainForm('自动批量抠图神器')
    mainForm.show()
    sys.exit(app.exec_())
