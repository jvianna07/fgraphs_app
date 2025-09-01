# Load libraries 
from keras.models import load_model 
import numpy as np
import cv2


# Main class for Math Graph Classifier
class MathGraph:
    def __init__(self, path:str)->None:
        self.GF_Model = load_model(path)


    # Fazer previsões
    def predict_graph(self, img_url:str)->str:
        # transforma a image em um array, redimensiona e faz a prediction
        imagem = cv2.imread(img_url)
        imagem = cv2.resize(imagem,(128,128), interpolation = cv2.INTER_AREA)
        discover:int = np.argmax(self.GF_Model.predict(imagem.reshape(1,128,128,3)))

        # Dicionario com  nome das classes
        classes: dict = {0:'linear', 1: 'quadrática', 2:'cúbica', 3:'exponencial', 4:'logarítmica',
                            5:'raíz', 6:'seno', 7:'cosseno', 8:'tangente', 9:'cotangente'}
        
        return classes[discover]
