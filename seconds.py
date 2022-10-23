from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.textinput import TextInput


# напиши модуль для реализации секундомера

class Seconds(Label):
   
    def __init__(self, total, **kwargs):
        pass

    def restart(self, total, **kwargs):
        pass

    def start(self):
        pass

    def change(self, dt):
        pass