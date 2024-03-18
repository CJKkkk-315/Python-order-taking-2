from time import sleep
import os
from random import randint
lv = 0
life = 0
attck = 0
alive = 0
now = 0
userflag = 0
type_item = 0
def init():
    global lv
    global life
    global attck
    global alive
    global now
    lv = 1
    life = 5
    attck = 1
    alive = [1,1,1,1,1,1,1]
    now = []
def randnow():
    global now
    while len(now) != 6:
        i = randint(0,3)
        now.append(i)
    now.append(4)
    return
def inititem():
    global type_item
    type_item = {0:'小怪物',1:'大怪物',2:'回血药',3:'攻击药',4:'BOSS'}
    return
def start():
    init()
    randnow()
    inititem()
    return
def chooseuser():
    global userflag
    userflag = int(input('请输入你的选择（1 or 2）:'))
    return
def fightsmall():
    global life
    global attck
    slife = 2
    sattack = 1
    while True:

        print('怪物血量：{}'.format(slife))
        sleep(2)
        if userflag == 2:
            if randint(1,3)%3 == 0:
                print('你发动了连续攻击！怪物扣了{}滴血'.format(2*attck))
                slife -= 2*attck
            else:
                print('你发动了攻击！怪物扣了{}滴血'.format(attck))
                slife -= attck
            if slife <= 0:
                return 1
            life -= sattack
            print('怪物对你发动了攻击！你扣了{}滴血'.format(sattack))
            if life <= 0:
                return 0
        else:
            slife -= attck
            print('你发动了攻击！怪物扣了{}滴血'.format(attck))
            if slife <= 0:
                print('成功击杀了怪物！你发动技能恢复了1滴血')
                life += 1
                return 1
            life -= sattack
            print('怪物对你发动了攻击！你扣了{}滴血'.format(sattack))
            if life <= 0:
                return 0
def fightbig():
    global life
    global attck
    slife = 4
    sattack = 2
    while True:

        print('怪物血量：{}'.format(slife))
        sleep(2)
        if userflag == 2:
            if randint(1,3)%3 == 0:
                print('你发动了连续攻击！怪物扣了{}滴血'.format(2*attck))
                slife -= 2*attck
            else:
                print('你发动了攻击！怪物扣了{}滴血'.format(attck))
                slife -= attck
            if slife <= 0:
                return 1
            life -= sattack
            print('怪物对你发动了攻击！你扣了{}滴血'.format(sattack))
            if life <= 0:
                return 0
        else:
            slife -= attck
            print('你发动了攻击！怪物扣了{}滴血'.format(attck))
            if slife <= 0:
                print('成功击杀了怪物！你发动技能恢复了1滴血')
                life += 1
                return 1
            life -= sattack
            print('怪物对你发动了攻击！你扣了{}滴血'.format(sattack))
            if life <= 0:
                return 0
def fightboss():
    global life
    global attck
    slife = 8
    sattack = 3
    while True:
        print('怪物血量：{}'.format(slife))
        sleep(2)
        if userflag == 2:
            if randint(1,3)%3 == 0:
                print('你发动了连续攻击！怪物扣了{}滴血'.format(2*attck))
                slife -= 2*attck
            else:
                print('你发动了攻击！怪物扣了{}滴血'.format(attck))
                slife -= attck
            if slife <= 0:
                return 1
            life -= sattack
            print('怪物对你发动了攻击！你扣了{}滴血'.format(sattack))
            if life <= 0:
                return 0
        else:
            slife -= attck
            print('你发动了攻击！怪物扣了{}滴血'.format(attck))
            if slife <= 0:
                print('成功击杀了怪物！你发动技能恢复了1滴血')
                life += 1
                return 1
            life -= sattack
            print('怪物对你发动了攻击！你扣了{}滴血'.format(sattack))
            if life <= 0:
                return 0
start()
print('+++++++++++++++++++++++++++++++++++')
print('游戏开始，请选择你的角色：')
print('角色1：杀死怪物回复1点血量  角色2：有几率打出2次攻击')
chooseuser()
print('+++++++++++++++++++++++++++++++++++')
print('游戏开始，现在在你面前的选项是：')
while True:
    f = 0
    for i in now:
        if alive[f]:
            print(str(f+1) + '.' + type_item[i], end='  ')
        else :
            print(type_item[i] + '(已消失)', end='  ')
        f += 1
    c = int(input('\n请做出你的选择：'))-1
    if not alive[c]:
        print('当前怪物或物品已经消失，请重新选择')
    else:
        if now[c] == 0:
            res = fightsmall()
            if res:
                print('击杀小怪物成功！等级提升一级！')
                lv += 1
                life += 2
                attck += 1
                print('你现在的等级为：' + str(lv))
                print('你现在的生命值为：' + str(life))
                print('你现在的攻击力为：' + str(attck))
                alive[c] = 0
            else:
                print('你被怪物击杀了，游戏失败！')
                break
        if now[c] == 1:
            res = fightbig()
            if res:
                print('击杀大怪物成功！等级提升一级！')
                lv += 1
                life += 2
                attck += 1
                print('你现在的等级为：' + str(lv))
                print('你现在的生命值为：' + str(life))
                print('你现在的攻击力为：' + str(attck))
                alive[c] = 0
            else:
                print('你被怪物击杀了，游戏失败！')
                break
        if now[c] == 2:
            print('吃下了回血药，你的生命值提高了2点！')
            life += 2
            print('你现在的等级为：' + str(lv))
            print('你现在的生命值为：' + str(life))
            print('你现在的攻击力为：' + str(attck))
            alive[c] = 0
        if now[c] == 3:
            print('吃下了攻击药，你的攻击力提高了1点！')
            attck += 1
            print('你现在的等级为：' + str(lv))
            print('你现在的生命值为：' + str(life))
            print('你现在的攻击力为：' + str(attck))
            alive[c] = 0
        if now[c] == 4:
            res = fightboss()
            if res:
                print('击杀boss成功！你成功通关了！')
                alive[c] = 0
                break
            else:
                print('你被怪物击杀了，游戏失败！')
                break



