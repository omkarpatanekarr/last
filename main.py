# File: main.py
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class HelloKivyApp(App):
    def build(self):
        return BoxLayout()

    def button_pressed(self):
        print("Button pressed!")

if __name__ == '__main__':
    HelloKivyApp().run()
