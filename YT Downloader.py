from pytube import YouTube
from kivy.uix.relativelayout import RelativeLayout
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image

from kivy.core.window import Window

Window.size = (500,600)
Window.clearcolor = (1,0,1,1)

class MyApp(App):
    def build(self):
        layout = RelativeLayout()
        
        return layout
    
if __name__ == "__main__":
    
    MyApp().run()