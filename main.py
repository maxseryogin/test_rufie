from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.graphics import Color, Rectangle
from kivy.uix.image import Image
from kivy.core.window import Window
from instructions import txt_instruction, txt_test1, txt_test2, txt_test3, txt_sits
from ruffier import test
from timer import Timer
from sits import *
from runner import *

age = ""
name = ""
p1, p2, p3 = 0, 0, 0

def checkInt(val):
    try:
        val = int(val)
        if val < 0:
            return False
        else:
            return True
    except:
        return False

class CustomScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.bind(size=self.update_canvas_size)

        with self.canvas.before:
            self.background = Color(1, 0.8, 0, 1)
            self.rect = Rectangle(size=(Window.width, Window.height), pos=self.pos)

    def update_canvas_size(self, instance, value):
        self.rect.size = instance.size

class FirstScreen(CustomScreen):
    global age, name
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas.before:
            self.background = Color(1, 0.3, 0, 1)
            self.rect = Rectangle(size=(Window.width, Window.height), pos=self.pos)

        self.lbl_info = Label(text=txt_instruction, font_name='shrift.ttf',font_size=25)
        self.lbl_name = Label(text="Введіть ім'я: ", font_name='shrift.ttf',font_size=25)
        self.lbl_age = Label(text="Скільки вам років: ", font_name='shrift.ttf',font_size=25)

        self.input_name = TextInput(text=name, multiline=False, font_name='shrift.ttf',font_size=25)
        self.input_age = TextInput(text=str(age), multiline=False, font_name='shrift.ttf',font_size=25)

        self.btn_next = Button(text="Почати тест!", font_name='shrift.ttf',font_size=25)
        self.btn_next.on_press = self.next

        self.main_layout = BoxLayout(orientation="vertical", padding=8, spacing=8)
        self.line_1 = BoxLayout()
        self.line_2 = BoxLayout()

        self.line_1.add_widget(self.lbl_name)
        self.line_1.add_widget(self.input_name)

        self.line_2.add_widget(self.lbl_age)
        self.line_2.add_widget(self.input_age)

        self.main_layout.add_widget(self.lbl_info)
        self.main_layout.add_widget(self.line_1)
        self.main_layout.add_widget(self.line_2)
        self.main_layout.add_widget(self.btn_next)

        self.add_widget(self.main_layout)

    def next(self):
        global age, name
        if checkInt(self.input_age.text):
            name = self.input_name.text
            age = int(self.input_age.text)
            self.manager.current = "P1"

class SecondScreen(CustomScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        with self.canvas.before:
            self.background = Color(0, 0, 0.5, 1)
            self.rect = Rectangle(size=(Window.width, Window.height), pos=self.pos)
        
        self.lbl_info = Label(text=txt_test1, font_name='shrift.ttf',font_size=25)
        self.timer_lbl = Timer(15)
        self.timer_lbl.bind(done=self.on_timer_done)

        self.lbl_result = Label(text="Введіть результат:", font_name='shrift.ttf',font_size=25)

        self.input_result = TextInput(multiline=False, font_name='shrift.ttf',font_size=25)
        self.input_result.set_disabled(True)

        self.btn_next = Button(text="Продовжити", font_name='shrift.ttf',font_size=25)
        self.btn_next.on_press = self.next
        self.btn_next.set_disabled(True)

        self.main_layout = BoxLayout(orientation="vertical", padding=8, spacing=8)
        self.line = BoxLayout()
        self.line.add_widget(self.lbl_result)
        self.line.add_widget(self.input_result)

        self.main_layout.add_widget(self.lbl_info)
        self.main_layout.add_widget(self.timer_lbl)
        self.main_layout.add_widget(self.line)
        self.main_layout.add_widget(self.btn_next)

        self.add_widget(self.main_layout)
        self.on_enter = self.timer_lbl.start

    def on_timer_done(self, *args):
        self.input_result.set_disabled(False)
        self.btn_next.set_disabled(False)

    def next(self):
        global p1
        if checkInt(self.input_result.text):
            p1 = int(self.input_result.text)
            self.manager.current = "P2"

class ThirdScreen(CustomScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        with self.canvas.before:
            self.background = Color(0.7, 0.5, 0.3, 1)
            self.rect = Rectangle(size=(Window.width, Window.height), pos=self.pos)
        
        self.lbl_info = Label(text=txt_sits, font_name='shrift.ttf',font_size=25)
        self.lbl_sits = Sits(30)
        self.run = Runner(total=30, stepTime=1.75)
        self.run.bind(valueChanged=self.lbl_sits.next)
        self.run.bind(finished=self.on_timer_done)

        self.btn_next = Button(text="Продовжити", font_name='shrift.ttf',font_size=25)
        self.btn_next.on_press = self.next
        self.btn_next.set_disabled(True)

        self.main_layout = BoxLayout(orientation="vertical", padding=8, spacing=8)
        self.main_layout.add_widget(self.lbl_info)
        self.main_layout.add_widget(self.lbl_sits)
        self.main_layout.add_widget(self.run)
        self.main_layout.add_widget(self.btn_next)

        self.add_widget(self.main_layout)
        self.on_enter = self.run.start

    def on_timer_done(self, *args):
        self.btn_next.set_disabled(False)

    def next(self):
        self.manager.current = "P3"

class FourthScreen(CustomScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        with self.canvas.before:
            self.background = Color(1, 0.4, 0.7, 1)
            self.rect = Rectangle(size=(Window.width, Window.height), pos=self.pos)

        self.stage = 0
        self.lbl_info = Label(text=txt_test3, font_name='shrift.ttf',font_size=25)
        self.timer_lbl = Timer(15)
        self.timer_lbl.bind(done=self.on_timer_done)

        self.lbl_p2 = Label(text="Результат: ", font_name='shrift.ttf',font_size=25)
        self.lbl_p3 = Label(text="Результат після відпочинку: ", font_name='shrift.ttf',font_size=25)

        self.input_p2 = TextInput(multiline=False, font_name='shrift.ttf',font_size=25)
        self.input_p2.set_disabled(True)
        self.input_p3 = TextInput(multiline=False, font_name='shrift.ttf',font_size=25)
        self.input_p3.set_disabled(True)

        self.btn_next = Button(text="Продовожити", font_name='shrift.ttf',font_size=25)
        self.btn_next.on_press = self.next
        self.btn_next.set_disabled(True)

        self.main_layout = BoxLayout(orientation="vertical", padding=8, spacing=8)
        self.line_1 = BoxLayout()
        self.line_2 = BoxLayout()

        self.line_1.add_widget(self.lbl_p2)
        self.line_1.add_widget(self.input_p2)

        self.line_2.add_widget(self.lbl_p3)
        self.line_2.add_widget(self.input_p3)

        self.main_layout.add_widget(self.lbl_info)
        self.main_layout.add_widget(self.timer_lbl)
        self.main_layout.add_widget(self.line_1)
        self.main_layout.add_widget(self.line_2)
        self.main_layout.add_widget(self.btn_next)

        self.add_widget(self.main_layout)
        self.on_enter = self.timer_lbl.start

    def on_timer_done(self, *args):
        if self.timer_lbl.done:
            if self.stage == 0:
                self.stage = 1
                self.lbl_info.text = "Відпочивайте"
                self.timer_lbl.restart(30)
                self.input_p2.set_disabled(False)
            elif self.stage == 1:
                self.stage = 2
                self.lbl_info.text = "Рахуйте пульс"
                self.timer_lbl.restart(15)
                self.input_p3.set_disabled(False)
            elif self.stage == 2:
                self.stage = 0
                self.lbl_info.text = "Запишіть дані"
                self.btn_next.set_disabled(False)


    def next(self):
        global p2, p3
        if checkInt(self.input_p2.text) and checkInt(self.input_p3.text):
            p2 = int(self.input_p2.text)
            p3 = int(self.input_p3.text)
            self.manager.current = "Result"

class FifthScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.background = Image(source='background.jpg', allow_stretch=True, keep_ratio=False)
        
        self.lbl_info = Label(text="", font_name='shrift.ttf', font_size=25)

        self.main_layout = BoxLayout(
            orientation="vertical", padding=8, spacing=8)

        self.main_layout.add_widget(self.background) 
        self.main_layout.add_widget(self.lbl_info)

        self.add_widget(self.main_layout)

        self.on_enter = self.loadPage

        self.bind(size=self._update_rect, pos=self._update_rect)

    def _update_rect(self, instance, value):
        self.background.pos = instance.pos
        self.background.size = instance.size

    def loadPage(self):
        global name, p1, p2, p3, age

        if not (name and p1 and p2 and p3 and age):
            self.lbl_info.text = "Ви не ввели інформацію у всі поля"
        else:
            self.lbl_info.text = name + "\n" + test(p1, p2, p3, age)

class RufieApp(App):
    def build(self):
        Window.size = (1400, 730)
        Window.set_icon('icon.png')
        self.screen_manager = ScreenManager()
        self.screen_manager.add_widget(FirstScreen(name="Main"))
        self.screen_manager.add_widget(SecondScreen(name="P1"))
        self.screen_manager.add_widget(ThirdScreen(name="P2"))
        self.screen_manager.add_widget(FourthScreen(name="P3"))
        self.screen_manager.add_widget(FifthScreen(name="Result"))
        return self.screen_manager

    def on_start(self):
        Window.top = (Window.height - Window.minimum_height) // 2
        Window.left = (Window.width - Window.minimum_width) // 2

app = RufieApp()
app.run()
