from bs4 import BeautifulSoup
import requests
import csv
import tkinter as tk
def getHTMLText(url):
    try:
        myheaders={"user-agent":"Mozilla/5.0"}
        r=requests.get(url,timeout=100,headers=myheaders)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        print("连接成功")
    except:
        print("连接异常")
        return
def get_concents(ulist,rurl):
    soup=BeautifulSoup(rurl,'html.parser')
    trs=soup.find_all('tr')
    for tr in trs:
        ui=[]
        for td in tr:
            ui.append(td.string)
        ulist.append(ui)
def save_contents(filename,urlist):
    with open(filename,'w',newline='')as f:
        writer=csv.writer(f)
        writer.writerows(urlist)
urlist=[]
url="http://www.gaosan.com/gaokao/241219.html"
filename="csvfile1.csv"
rs=['']
def do1():
    rs[0]=getHTMLText(url)
    if rs[0]!='':
        tk.messagebox.showinfo('标题','连接正常！')
def do2():
    get_concents(urlist,rs[0])
    if urlist!='':
        tk.messagebox.showinfo('标题','获取数据正常！')
def do3():
    save_contents(filename,urlist)
    tk.messagebox.showinfo('标题','保存文件成功！')
def do_scrip(rootl):
    top1=tk.Toplevel(rootl)
    top1.title('数据爬取窗体')
    top1.transient(rootl)
    top1.geometry('500x500+500+300')
    bt1=tk.Button(top1,text='连接服务器',command=do1)
    bt2=tk.Button(top1,text='爬取数据',command=do2)
    bt3=tk.Button(top1,text='保存数据',command=do3)
    bt1.place(x=50,y=50,width=100,height=60)
    bt2.place(x=50,y=150,width=100,height=60)
    bt3.place(x=50,y=250,width=100,height=60)
    top1.mainloop()
root = tk.Tk()
do_scrip(root)

