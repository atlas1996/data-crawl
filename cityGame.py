from urllib.request import urlopen
from bs4 import BeautifulSoup
import random
import time


def get_city():
    html = urlopen("http://weather.com.cn/radar")
    bsObj = BeautifulSoup(html, "lxml")
    print("城市名称采集中……")
    time.sleep(3)
    cityList = bsObj.findAll("a", href="#")
    with open('city.txt', 'w') as file:
        for city in cityList:
            file.write(city.string+'\n')
            print(city.string)


def chinese_to_alphabet(chinese):
    """参数为字符串，返回为该字符串对应的汉语拼音"""
    alphabet = ''
    dic = {}
    with open("unicode_pinyin.txt") as file:
        for i in file.readlines():
            dic[i.split()[0]] = i.split()[1]
    for i in chinese:
        i = str(i.encode('unicode_escape'))[-5:-1].upper()
        try:
            alphabet += dic[i] + ' '
        except:
            alphabet += 'XXXX ' #非法字符我们用XXXX代替
    return alphabet


def city_exists(city):
    """判断是否为城市的函数，参数为字符串，判断该字符串是否在成语库中"""
    with open('city.txt','r') as file:
        for i in set(file.readlines()):
            if city == i.strip():
                return True
        return False

def city_confirm(city1, city2):
    """判断两个成语是否达成接龙条件"""
    #为了可读性，我把它分开写，比较清晰
    if chinese_to_alphabet(city2[0])[:-2] != chinese_to_alphabet(city1[-1])[:-2]:
        return False
    return True

def city_select(city):
    """核心代码部分，参数x为成语，返回该成语的接龙匹配成语"""
    if city == None:
        with open('city.txt','r') as file:
            return random.choice(file.readlines())[:-1]
    else:
        with open('city.txt','r') as file:
            #以下六行代码，通过索引排除无效循环，显著提升运行效率
            alphabet = chinese_to_alphabet(city[-1])
            base = file.readlines()
            random.shuffle(base)
            for i in base:
                if i[:-1] == city:
                    continue
                if chinese_to_alphabet(i[0])[:-2] == alphabet [:-2]:
                    return i[:-1]
        return None

def start(start = 0):
    """start参数表示先后手，0表示电脑先手，1表示玩家先手；返回值代表游戏结果，为0表示玩家失败，为1代表玩家胜利"""
    memory = set()  #记忆集合，用于判断成语是否被重复使用
    get_city()
    if start == 0:
        while True:
            city1 = city_select(None)
            if city_select(city1) != None:
                break
        print(city1)
    else:
        city1 = input("请输入城市名：")
        if city1.strip() == '':
            print("游戏结束！你输了")
            return 0
        if city_exists(city1) == False:
            print("游戏结束！该城市名称不存在")
            return 0
        memory.add(city1)
        cycle_flag = 0  #控制while True循环次数
        while True:
            city2 = city_select(city1)
            cycle_flag += 1
            if city2 not in memory:
                break
            if cycle_flag == 10:
                city2 = None
                break
        if city2 == None:
            print("恭喜你，你赢了！")
            return 1
        else:
            print(city2)
            memory.add(city2)
    while True:
        city2 = input("请输入城市名:")
        if city2.strip() == '':
            print("游戏结束！你输了")
        if city_exists(city2) == False:
            print("游戏结束！该城市名不存在")
            return 0
        if city2 in memory:
            print("游戏结束！该城市名已被使用过")
            return 0
        if city_confirm(city1, city2) == False:
            print("游戏结束！你未遵守游戏规则")
            return 0
        memory.add(city2)
        cycle_flag = 0
        while True:
            city1 = city_select(city2)
            cycle_flag += 1
            if city1 not in memory:
                break
            if cycle_flag == 10:
                city1 = None
                break
        if city1 == None:
            print("恭喜你，你赢了！")
            return 1
        else:
            print(city1)
            memory.add(city1)

#测试运行，修改参数使其变为规则更加宽松的接龙（mode和opt默认为0则为简易版的成语接龙）
start(start=1)
