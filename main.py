from kivymd.app import MDApp
from kivy.uix.video import Video
from kivy.uix.widget import Widget
from kivy.uix .videoplayer import VideoPlayer

class MainApp(MDApp):
    def build(self):
        player = VideoPlayer(source= "video.mp4",size_hint=(None,None),width=250,height=250)
        player.state = 'play'
        player.options = {'eos':'loop'}
        player.allow_stretch = False

        return player



MainApp().run()
