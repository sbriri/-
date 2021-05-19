from kivy.app import App
from kivy.core import text
from kivy.uix.behaviors import button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from ticket import ticket
from ticket import control

class LoginScreen(GridLayout):


    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.rows = 2
        # self.cols = 2
        # self.add_widget(Label(text='User Name'))
        # self.username = TextInput(multiline=False)
        # self.add_widget(self.username)
        # self.add_widget(Label(text='password'))
        # self.password = TextInput(password=True, multiline=False)
        # self.add_widget(self.password)
        self.button1 = Button(text='get 1 ticket')
                
        def callback(instance):
            print('The button <%s> is being pressed' % instance.text)
            print(control.gen1(False,0,False,[0]))

        self.button1.bind(on_press=callback)
        self.add_widget(self.button1)
    


        self.button10 = Button(text = 'get 10 tickets')

        self.button10.bind(on_press=callback)
        self.add_widget(self.button10)


class MyApp(App):

    def build(self):
        return LoginScreen()

if __name__ == '__main__':
    MyApp().run()