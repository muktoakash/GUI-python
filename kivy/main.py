import kivy
from kivy.uix.label import Label

from kivy.app import App
from kivy.clock import Clock

class TheLabApp(App):
    def build(self):
        Clock.schedule_once(lambda *args: print("Timer"), 1)
        return Label(text='Hello world')

if __name__=='__main__':
    TheLabApp().run
