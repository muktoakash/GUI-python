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
from kivy.properties import StringProperty, BooleanProperty

class WidgetsExample(GridLayout):
    """"""
    count = 0
    count_enabled = BooleanProperty(False)
    my_text = StringProperty("Hello!")
    # slider_value_txt = StringProperty("Value")
    text_input_str = StringProperty("foo")

    def on_button_click(self):
        print("button clicked")
        # self.my_text = "You clicked!"
        if self.count_enabled:
            self.count += 1
            self.my_text = f'{self.count}'

    def on_toggle_button_state(self, widget):
        print("toggle_state:" + widget.state)
        if widget.state == "normal":
            widget.text = "OFF"
            self.count_enabled = False
        else:
            widget.text = "ON"
            self.count_enabled = True

    def on_switch_active(self, widget):
        print("Switch: " + str(widget.active))

    # def on_slider_value(self, widget):
    #     print("Slider: " + str(int(widget.value)))
    #     # self.slider_value_txt = str(int(widget.value))

    def on_text_validate(self, widget):
        self.text_input_str = widget.text

class MainWidget(Widget):
    pass

class TheLabApp(App):
    pass

if __name__ == '__main__':
    TheLabApp().run()
