from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from kivy.uix.image import Image
import time
import os
import cv2
from kivy.core.window import Window


Window.size = (350,900)

Builder.load_file("homescreen.kv")

class Homescreen(MDScreen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

        self.mycamera = self.ids.camera
        self.last_photo = self.ids.last_photo

    def captureyouface(self):
        self.directory = "fotos"
        if not os.path.exists(self.directory):
            os.mkdir(self.directory)

        timenow = time.strftime("%Y%m%d_%H%M%S")
        self.filename = os.path.join(self.directory, "myimage_{}.png".format(timenow))
        
        self.mycamera.export_to_png(self.filename)
        self.last_photo.source = self.filename


class MyApp(MDApp):
    def build(self):
        return Homescreen()

if __name__ == "__main__":
    MyApp().run()