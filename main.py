from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
import time
import os
from kivy.core.window import Window
from classifier import MathGraph

Window.size = (350,800)

# Define o arquivo do modelo de classificação
caminho_do_modelo = 'models/LID_gf_modelV7.keras'


Builder.load_file("homescreen.kv")

# Cria a tela inicial
class Homescreen(MDScreen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
    
    # Inicializa a câmera e a última foto
        self.mycamera = self.ids.camera
        self.last_photo = self.ids.last_photo

    # Cria a pasta "fotos" caso ela não exista
    def captureyouface(self):
        self.directory = "fotos"
        if not os.path.exists(self.directory):
            os.mkdir(self.directory)

    # Verifica se a pasta "fotos" contém mais de 2 imagens
    # Caso haja mais de 2 imagens, a mais antiga será removida
        archives = len(os.listdir(self.directory))
        if archives >= 2:
            oldest_file = min([os.path.join(self.directory, f) for f in os.listdir(self.directory)], key=os.path.getctime)
            os.remove(oldest_file)

    # Cria um nome de arquivo único para a nova imagem e salva em png
        timenow = time.strftime("%Y%m%d_%H%M%S")
        self.filename = os.path.join(self.directory, "myimage_{}.png".format(timenow))
        
        self.mycamera.export_to_png(self.filename)
        self.last_photo.source = self.filename

    # Classifica a ultima imagem capturada
        caminho_da_imagem = self.filename
        classificador = MathGraph(caminho_do_modelo)
        resposta = classificador.predict_graph(caminho_da_imagem)   
        self.ids.tipo.text = "A função é: {}".format(resposta)


class MyApp(MDApp):
    def build(self):
        return Homescreen()
 
# executar o app
if __name__ == "__main__":
    MyApp().run()