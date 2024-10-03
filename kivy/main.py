import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.metrics import dp
from kivy.properties import StringProperty

class WidgetsExample(GridLayout):
    """"""
    count = 0
    my_text = StringProperty("Hello!")

    def on_button_click(self):
        print("button clicked")
        # self.my_text = "You clicked!"
        self.count += 1
        self.my_text = f'{self.count}'

    def on_toggle_button_state(self, widget):
        print("toggle_state:" + widget.state)
        if widget.state == "normal":
            widget.text = "OFF"
        else:
            widget.text = "ON"

class MainWidget(Widget):
    pass

class TheLabApp(App):
    pass

if __name__ == '__main__':
    TheLabApp().run()
