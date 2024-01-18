
import kivy
kivy.require("1.9.1")
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.core.window import Window
Window.size = (360, 700)



class ButtonApp(App):

    def build(self):
        box = FloatLayout()



        btn = Button(text="Кн",
                     font_size="20sp",
                     background_color=(1, 1, 1, 1),
                     color=(1, 1, 1, 1),
                     size=(32, 32),
                     size_hint=(.2, .1),
                     pos=(5, 300))
        btn1 = Button(text="Мн",
                     font_size="20sp",
                     background_color=(1, 1, 1, 1),
                     color=(1, 1, 1, 1),
                     size=(32, 32),
                     size_hint=(.2, .1),
                     pos=(75, 300))
        btn2 = Button(text="кДж",
                     font_size="20sp",
                     background_color=(1, 1, 1, 1),
                     color=(1, 1, 1, 1),
                     size=(32, 32),
                     size_hint=(.2, .1),
                     pos=(145, 300))
        btn3 = Button(text="мДж",
                     font_size="20sp",
                     background_color=(1, 1, 1, 1),
                     color=(1, 1, 1, 1),
                     size=(32, 32),
                     size_hint=(.2, .1),
                     pos=(215, 300))
        btn4 = Button(text="кВт",
                     font_size="20sp",
                     background_color=(1, 1, 1, 1),
                     color=(1, 1, 1, 1),
                     size=(32, 32),
                     size_hint=(.2, .1),
                     pos=(285, 300))
        self.textinput1 = TextInput(
                     font_size="20sp",
                     size=(32, 32),
                     size_hint=(.5, .1),
                     pos=(95, 600))





        btn.bind(on_press=self.callback)
        btn1.bind(on_press=self.callback1)
        btn2.bind(on_press=self.callback2)
        btn3.bind(on_press=self.callback3)
        btn4.bind(on_press=self.callback4)


        box.add_widget(btn)
        box.add_widget(btn1)
        box.add_widget(btn2)
        box.add_widget(btn3)
        box.add_widget(btn4)
        box.add_widget(self.textinput1)
        box.add_widget(self.label)









        return box

    def __init__(self):
        super().__init__()
        self.label = Label(font_size="20sp",
                     size=(32, 32),
                     size_hint=(.5, .1),
                     pos=(95, 400))


    def callback(self, event):
        text = self.textinput1.text
        my_list_str = int(int(text))
        text2 = my_list_str * 1000
        self.label.text = str(text2) + "Н"

    def callback1(self, event):
        text = self.textinput1.text
        my_list_str = int(int(text))
        text2 = my_list_str * 100000
        self.label.text = str(text2) + "Н"

    def callback2(self, event):
        text = self.textinput1.text
        my_list_str = int(int(text))
        text2 = my_list_str * 1000
        self.label.text = str(text2) + "Дж"

    def callback3(self, event):
        text = self.textinput1.text
        my_list_str = int(int(text))
        text2 = my_list_str * 100000
        self.label.text = str(text2) + "Дж"

    def callback4(self, event):
        text = self.textinput1.text
        my_list_str = int(int(text))
        text2 = my_list_str * 1000
        self.label.text = str(text2) + "Вт"






















root = ButtonApp()
root.run()