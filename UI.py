# !/usr/bin/python
# -*-coding:utf-8-*-

# from kivy.config import Config
 
# Config.set('kivy', 'default_font', [
#     'msgothic',
#     'fonts/txb2.ttf'])


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

class ScreenManager(ScreenManager):
    pass


class LotteryScreen(GridLayout, Screen):
    pass

class OneTktScreen(Screen):

    oneTktScreen_instance = StringProperty()

    def __init__(self, **kwargs):
        super(OneTktScreen, self).__init__(**kwargs)
        self.oneTktScreen_instance = "haven't update yet"
    
    def printReslut(self):
    
        lot = control.gen1(False,0,False,[0])
        
        tkt = control.gen1(False,0,False,[0])
        lottery.win(lot,tkt)


        result = ("first " + str(lottery.first) + '\n' +
                 "second " + str(lottery.second) + '\n' +
                 "third " + str(lottery.third) + '\n' +
                 "forth " + str(lottery.forth) + '\n' +
                 "sixth " + str(lottery.sixth) + '\n' + 
                 "welfare " + str(lottery.welfare) + '\n' +
                 "count " + str(lottery.count) + '\n' +
                 "===========================" + '\n' +
                 "get  " + str(lottery.first * 5000000 + lottery.second * 2500000 + lottery.third * 3000 + lottery.forth * 200 + lottery.fifth * 10 + lottery.sixth * 5) + "￥" + '\n' +
                 "spend " + str(lottery.count * 2) )


        self.oneTktScreen_instance = result


        # print("second " + str(lottery.second))
        # print("third " + str(lottery.third))
        # print("forth " + str(lottery.forth))
        # print("fifth " + str(lottery.fifth))
        # print("sixth " + str(lottery.sixth))
        # print("welfare " + str(lottery.welfare))
        # print("count " + str(lottery.count))
        # print("===========================")
        # print("get  " + str(lottery.first * 5000000 + lottery.second * 2500000 + lottery.third * 3000 + lottery.forth * 200 + lottery.fifth * 10 + lottery.sixth * 5) + "￥")
        # print("spend " + str(lottery.count * 2))
        # for instance_class in self.ids.values():
        #     instance_class.text = 'Exit'
        #     instance_class.bind(on_release=exit)

class TenTktScreen(Screen):

    tenTktScreen_instance = StringProperty()

    def __init__(self, **kwargs):
        super(TenTktScreen, self).__init__(**kwargs)
        self.tenTktScreen_instance = "haven't update yet"

    def printResult(self):

        lot = control.gen1(False,0,False,[0])
        
        tkts = control.genN(10,False,0,False,[0])

        for tkt in tkts:
            lottery.win(lot,tkt)

        result = ("first " + str(lottery.first) + '\n' +
            "second " + str(lottery.second) + '\n' +
            "third " + str(lottery.third) + '\n' +
            "forth " + str(lottery.forth) + '\n' +
            "sixth " + str(lottery.sixth) + '\n' + 
            "welfare " + str(lottery.welfare) + '\n' +
            "count " + str(lottery.count) + '\n' +
            "===========================" + '\n' +
            "get  " + str(lottery.first * 5000000 + lottery.second * 2500000 + lottery.third * 3000 + lottery.forth * 200 + lottery.fifth * 10 + lottery.sixth * 5) + "￥" + '\n' +
            "spend " + str(lottery.count * 2) )

        self.tenTktScreen_instance = result

        # print("first " + str(lottery.first))
        # print("second " + str(lottery.second))
        # print("third " + str(lottery.third))
        # print("forth " + str(lottery.forth))
        # print("fifth " + str(lottery.fifth))
        # print("sixth " + str(lottery.sixth))
        # print("welfare " + str(lottery.welfare))
        # print("count " + str(lottery.count))
        # print("===========================")
        # print("get  " + str(lottery.first * 5000000 + lottery.second * 2500000 + lottery.third * 3000 + lottery.forth * 200 + lottery.fifth * 10 + lottery.sixth * 5) + "￥")
        # print("spend " + str(lottery.count * 2))

class MyApp(App):

    def build(self):
        return ScreenManager()

if __name__ == '__main__':
    MyApp().run()