# !/usr/bin/python
# -*-coding:utf-8-*-

from kivy.core.text import LabelBase
LabelBase.register('Roboto', './fonts/WeiRuanYaHei-1.ttf')

from kivy.app import App
from kivy.core.text import Label as CoreLabel
from kivy.uix.behaviors import button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty

from ticket import ticket
from ticket import control
from ticket import lottery

from kivy.core.window import Window
Window.size = (1080  , 1920)
class ScreenManager(ScreenManager):
    pass


class LotteryScreen(GridLayout, Screen):
    pass

class TktScreen(Screen):

    oneTktScreen_instance = StringProperty()

    def __init__(self, **kwargs):
        super(TktScreen, self).__init__(**kwargs)
        self.oneTktScreen_instance = "请选择购买方式"
    
    def printReslut(self, num):
    
        lot = control.gen1(False,0,False,[0])
        
        tkts = control.genN(num,False,0,False,[0])
        for tkt in tkts:
            lottery.win(lot,tkt)


        result = ("一等奖 " + str(lottery.first) + '\n' +
                 "二等奖 " + str(lottery.second) + '\n' +
                 "三等奖 " + str(lottery.third) + '\n' +
                 "四等奖 " + str(lottery.forth) + '\n' +
                 "五等奖 " + str(lottery.fifth) + '\n' +
                 "六等奖 " + str(lottery.sixth) + '\n' + 
                 "慈善 " + str(lottery.welfare) + '\n' +
                 "购买总数 " + str(lottery.count) + '\n' +
                 "===========================" + '\n' +
                 "一共赚了  " + str(lottery.first * 5000000 + lottery.second * 2500000 + lottery.third * 3000 + lottery.forth * 200 + lottery.fifth * 10 + lottery.sixth * 5) + "￥" + '\n' +
                 "一共花了 " + str(lottery.count * 2) + "￥")


        self.oneTktScreen_instance = result

        
    def cleanData(self):
        lottery.first = 0
        lottery.second = 0
        lottery.third = 0
        lottery.forth = 0
        lottery.fifth = 0
        lottery.sixth = 0
        lottery.welfare = 0
        lottery.count = 0
        lottery.lucky = False
        self.oneTktScreen_instance = "请选择购买方式"



class printTkt(Screen):
    
    tktScreen_instance = StringProperty()

    def __init__(self, **kwargs):
        super(printTkt, self).__init__(**kwargs)
        self.tktScreen_instance = "请选择生成方式"
    
    def printReslut(self, num):
    
        tkts = control.genN(num,False,0,False,[0])
        result = ""
        for tkt in tkts:
            result += str(tkt) + '\n'

        self.tktScreen_instance = result

    def cleanData(self):
        self.tktScreen_instance = "请选择生成方式"


class MyApp(App):

    def build(self):
        return ScreenManager()

if __name__ == '__main__':
    MyApp().run()