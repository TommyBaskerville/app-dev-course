from pytube import YouTube
from kivy.uix.relativelayout import RelativeLayout
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image

from kivy.core.window import Window

Window.size = (500,600)
Window.clearcolor = (1,1,1,1)

class MyApp(App):
    def build(self):
        layout = RelativeLayout()
        
        self.image = Image(source="logo.svg", size_hint=(.5, .5), pos_hint={"center_x":.5, "center_y":.90})
        
        self.youtubelink = Label(text="Youtube Link", size_hint=(1,1), pos_hint={"center_x":.5, "center_y":.75}, font_size=20, color=(0,0,0,1))
        
        self.linkinput = TextInput(size_hint=(.8,.05), pos_hint={"center_x":.5, "center_y":.65}, multiline=False)
        
        layout.add_widget(self.linkinput)
        
        layout.add_widget(self.youtubelink)
        
        layout.add_widget(self.image)
        return layout
    
if __name__ == "__main__":
    
    MyApp().run()