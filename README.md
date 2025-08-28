# Math Graph Classifier App
## Descrição
Este é um projecto de aplicativo mobile para o math graph classifier. O App ainda em construçao se propõe a fazer a classificação de imagens em dez classes pré-definidas:
* 0 - linear
* 1 - quadrática
* 2 - cúbica
* 3 - exponencial
* 4 - logarítmica
* 5 - raíz
* 6 - seno
* 7 - cosseno
* 8 - tangente
* 9 - cotangente

## Instruções de uso
Clone este repositório:
```bash
git@github.com:jvianna07/fgraphs_app.git
```
Entre na pasta:
```bash
cd fgraphs_app/
```

Crie um ambiente virtual com python>=3.10. Ative o ambiente virtual e instale as dependências.
```bash
pip install requirements.txt
```

## Execução
O app ainda está em construção. Porém a estrutura de arquivos é a seguinte:
```bash
.
├── classifier.py
├── demo_imgs
│   └── func0.png
├── fotos/
├── homescreen.kv
├── main.py
├── models
│   └── LID_gf_modelV7.keras
├── README.md
├── requirements.txt
└── test.py
```
### Arquivos *.py
- `main.py` - classe principal do App.
- `classifier.py` - contém a classe principal do modelo classificador.
- `test.py` - ficheiro de teste apenas. Será descartado futuramente.
- `requirements.txt` - dependências do app.
- `homescreen.kv` - classe de manipulaçoa de widgets do kivy App.
- `README.md` - ficheito de instruções.

### Directórios
- `demo_imags/` - contém algumas imagens demo. Será descartada futuramente.
- `fotos/` - contém as fotos que são capturadas pela câmara.
- `models/ ` - contém o(s) modelo(s) pré-treinado(s).

## Futuras implementações
* capturar foto para depois processar e classificar
* optimizar o App
* empacotamento do App para apk versão mobile (android e ios)
