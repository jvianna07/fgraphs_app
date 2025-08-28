"""Este codigo abaixo deverá ser tranferido e modificado para um ficheior final na main APP
Depois disso deverá ser descartado
"""
from classifier import MathGraph

# Definir o caminho do modelo e da imagem 
caminho_do_modelo ='models/LID_gf_modelV7.keras'
caminho_da_imagem = 'demo_imgs/func0.png'

# Classificar 
classificador = MathGraph(caminho_do_modelo)

# Imprimir o resultado 
print(classificador.predict_graph(caminho_da_imagem))