from pytube import YouTube
from kivy.uix.relativelayout import RelativeLayout
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image

from kivy.core.window import Window

from functools import partial


Window.size = (500,600)
Window.clearcolor = (1,1,1,1)

class MyApp(App):
    
    def getlink(self, event,window):
        self.link = self.linkinput.text
        self.yt = YouTube(self.link)
        
        self.title = str(self.yt.title)
        self.views = str(self.yt.views)
        self.length = str(self.yt.length)
        
        print(f"Title: {self.title}")
        print(f"Views: {self.views}")
        print(f"Length: {self.length}")
    
        self.titleLabel.text = f"Title: {self.title}"
        self.viewsLabel.text = f"Views: {self.views}"
        self.lengthLabel.text = f"Length: {self.length}"
        
        self.titleLabel.pos_hint = {"center_x":.5, "center_y":.45}
        self.viewsLabel.pos_hint = {"center_x":.5, "center_y":.35}
        self.lengthLabel.pos_hint = {"center_x":.5, "center_y":.25}
        
        self.downloadbutton.opacity = 1
        self.downloadbutton.disabled = False
        
    def download(self, event, window):
        yt = YouTube(self.link)
        
        print("Downloading...")
        
        yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download("E:/Cursos/Mobile_app/app-dev-course")
        
        print("Downloaded")
        
        
    
        
    def build(self):
        layout = RelativeLayout()
        
        self.image = Image(source="logo.svg", size_hint=(.5, .5), pos_hint={"center_x":.5, "center_y":.90})
        self.youtubelink = Label(text="Youtube Link", size_hint=(1,1), pos_hint={"center_x":.5, "center_y":.75}, font_size=20, color=(0,0,0,1))
        self.linkinput = TextInput(text="",size_hint=(.8,.05), pos_hint={"center_x":.5, "center_y":.65}, multiline=False, height=50, font_size=15, foreground_color=(0,0,0,1), font_name="Roboto")
        self.linkbutton = Button(text="Getlink", size_hint=(.8,.05), pos_hint={"center_x":.5, "center_y":.55}, background_color=(0,0,0,1), color=(1,1,1,1), font_size=15, font_name="Roboto")
        self.linkbutton.bind(on_press = partial(self.getlink, layout))
        
        self.titleLabel = Label(text=" ", size_hint=(1,1), pos_hint={"center_x":.5, "center_y":.45}, font_size=20, color=(0,0,0,1))
        self.viewsLabel = Label(text=" ", size_hint=(1,1), pos_hint={"center_x":.5, "center_y":.35}, font_size=20, color=(0,0,0,1))
        self.lengthLabel = Label(text=" ", size_hint=(1,1), pos_hint={"center_x":.5, "center_y":.25}, font_size=20, color=(0,0,0,1))
        
        self.downloadbutton = Button(text="Download", size_hint=(.8,.05), pos_hint={"center_x":.5, "center_y":.18}, background_color=(0,0,0,1), color=(1,1,1,1), font_size=15, font_name="Roboto", opacity=0, disabled=True)
        self.downloadbutton.bind(on_press = partial(self.download, layout))
        
    
        widgets = [self.image, self.youtubelink, self.linkinput, self.linkbutton, self.titleLabel, self.viewsLabel, self.lengthLabel, self.downloadbutton]
        for widget in widgets:
            layout.add_widget(widget)
        
        return layout
    
if __name__ == "__main__":
    
    MyApp().run()