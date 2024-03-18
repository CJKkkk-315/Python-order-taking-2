import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.pyplot import MultipleLocator
from collections import Counter
import math
import numpy as np
mpl.rcParams['font.sans-serif'] = [u'simHei']
mpl.rcParams['axes.unicode_minus'] = False
def function1():
    AUNCu = pd.read_csv(r'COVID_AU_national_cumulative.csv')
    AUNCu = AUNCu.iloc[:690]
    con = AUNCu['confirmed'].tolist()
    vacc = AUNCu['vaccines'].tolist()
    time = AUNCu['date'].tolist()
    # fig是图像对象，axes坐标轴对象
    mpl.rcParams['font.sans-serif'] = [u'simHei']
    mpl.rcParams['axes.unicode_minus'] = False
    fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(12,10))
    axes2 = axes.twinx()
    axes2.set_ylim(0, 43343561)
    axes.set_ylim(0,240000)
    line1 = axes.plot(time,con,'k',label = '确诊人数')
    line2 = axes2.plot(time,vacc,'r',label = '疫苗接种人数')
    lns = line1+line2
    labs = [l.get_label() for l in lns]
    axes.legend(lns, labs, loc=0)
    plt.xticks(())
    plt.show()
def function2():
    AUNCu = pd.read_csv(r'COVID_AU_national_cumulative.csv')
    AUNCu = AUNCu.iloc[:690]
    AUDH = pd.read_csv(r'COVID_Data_Hub.csv')
    AUDH = AUDH.iloc[:690]
    people = AUDH['people_vaccinated'].tolist()
    people = [t/1e7 for t in people]
    vacc = AUNCu['vaccines'].tolist()
    vacc = [t / 1e7 for t in vacc]
    time = AUNCu['date'].tolist()
    fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(12, 10))
    plt.ylabel('number(millions)')
    axes2 = axes.twinx()
    axes2.set_ylim(0, 43343561/1e7)
    axes.set_ylim(0, 20000000/1e7)
    axes.plot(time, people, 'k', label='疫苗接种人数')
    axes.legend(loc=2)
    axes2.plot(time, vacc, 'r', label='疫苗接种剂数')
    axes2.legend(loc=4)
    plt.ylabel('number(millions)')
    plt.xticks(())
    plt.show()
def function3():
    AUSCu = pd.read_csv(r'COVID_AU_state_cumulative.csv')
    AUSCu = AUSCu.iloc[-8:]
    data = AUSCu['confirmed'].tolist()
    labels = ['ACT', 'NSW', 'NT', 'QLD', 'SA', 'TAS', 'VIC', 'WA']
    for i in range(len(labels)):
        labels[i] += ': ' + str(data[i])
    plt.figure(figsize=(5, 5))
    plt.pie(data,labels=labels,textprops= {'fontsize':7,'color':'black'})
    plt.show()
def function4():
    AUSCu = pd.read_csv(r'COVID_AU_state_cumulative.csv')
    data = AUSCu.loc[AUSCu["state"] == "New South Wales"]
    time = data['date'].tolist()
    tests = data['tests'].tolist()
    tests = [t/1e7 for t in tests]
    positives = data['positives'].tolist()
    positives = [t / 1e7 for t in positives]
    x_major_locator = MultipleLocator(90)
    fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(12, 10))
    plt.ylabel('number(millions)')
    axes2 = axes.twinx()
    axes.xaxis.set_major_locator(x_major_locator)
    axes2.set_ylim(0, 1109126/1e7)
    axes.set_ylim(0, 30044679/1e7)
    line1 = axes.plot(time, tests, 'k', label='tests')
    axes.legend(loc=2)
    line2 = axes2.plot(time, positives, 'r', label='positives')
    axes2.legend(loc=4)
    plt.ylabel('number(millions)')
    plt.show()
def function5():
    ADH = pd.read_csv(r'COVID_Data_Hub.csv')
    ADH = ADH.iloc[:759]
    hosp = ADH['hosp'].tolist()
    icu = ADH['icu'].tolist()
    time = ADH['date'].tolist()
    micu = max(icu)
    mhosp = max(hosp)
    x_major_locator = MultipleLocator(90)
    fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(12, 10))
    axes.set_ylim(0, mhosp)
    line1 = axes.plot(time, hosp, 'k', label='hosp')
    line2 = axes.plot(time, icu, 'r', label='icu')
    lns = line1 + line2
    labs = [l.get_label() for l in lns]
    axes.legend(lns, labs, loc=0)
    axes.xaxis.set_major_locator(x_major_locator)
    plt.show()
def function6():
    ADH = pd.read_csv(r'COVID_Data_Hub.csv')
    ADH = ADH.iloc[:690]
    confirmed = ADH['confirmed'].tolist()
    deaths = ADH['deaths'].tolist()
    people_fully_vaccinated = ADH['people_fully_vaccinated'].tolist()
    confirmed = [confirmed[i] for i in range(len(confirmed)) if i%10 == 0]
    deaths = [deaths[i] for i in range(len(deaths)) if i % 10 == 0]
    people_fully_vaccinated = [math.log(people_fully_vaccinated[i]+1,10)*30+20 for i in range(len(people_fully_vaccinated)) if i % 10 == 0]
    plt.figure(figsize=(3, 3))
    plt.scatter(confirmed,deaths,people_fully_vaccinated,c=np.random.rand(69))
    plt.xlabel('confirmed')
    plt.ylabel('deaths')
    plt.show()
def function7():
    AUSCu = pd.read_csv(r'COVID_AU_state_cumulative.csv',encoding='gbk')
    state = Counter(AUSCu['state_abbrev'].tolist())
    data = []
    for i in state.keys():
        data.append([i] + AUSCu.loc[AUSCu["state_abbrev"] == i]['deaths'].tolist())
    time = AUSCu.loc[AUSCu["state_abbrev"] == "WA"]['date'].tolist()
    fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(12, 10))
    line = []
    color = ['k','r','y','g','b','pink','m','orange']
    for i,j in zip(data,color):
        line.append(axes.plot(time, i[1:], j, label=i[0]))
    lns = line[0]
    for i in range(1,len(line)):
        lns += line[i]
    labs = [l.get_label() for l in lns]
    axes.legend(lns, labs, loc=0)
    plt.xticks(())
    plt.show()
def function8():
    AUSCu = pd.read_csv(r'COVID_AU_state_cumulative.csv')
    AUSCu = AUSCu.iloc[-8:]
    confirmed = AUSCu['confirmed'].tolist()
    print(confirmed)
    recovered = AUSCu['recovered'].tolist()
    print(recovered)
    labels = ['ACT', 'NSW', 'NT', 'QLD', 'SA', 'TAS', 'VIC', 'WA']
    p1 = plt.bar(labels, confirmed, color='blue')
    p2 = plt.bar(labels, recovered, bottom=confirmed, color='green')
    plt.legend((p1[0], p2[0]), ('confirmed', 'recovered'), loc=2)
    plt.show()
function5()
