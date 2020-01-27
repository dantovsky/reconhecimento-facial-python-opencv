import cv2
import os
import numpy as np
from PIL import Image
import tkinter as tk
from tkinter import filedialog

# Experimento para reconhecer uma imagem
# Dado um caminho de uma imagem, verificar se exista a pessoa no banco de imagens e dizer quem é.

detectorFace = cv2.CascadeClassifier("classifiers/haarcascade-frontalface-default.xml")
# reconhecedor = cv2.face.EigenFaceRecognizer_create()
# reconhecedor.read("classifications/classificadorEigenYale.yml")
# reconhecedor = cv2.face.FisherFaceRecognizer_create()
# reconhecedor.read("classifications/classificadorFisherYale.yml")
reconhecedor = cv2.face.LBPHFaceRecognizer_create()
reconhecedor.read("classifications/classificadorLBPHYale.yml")
root = tk.Tk()
root.withdraw()

# Obtem uma imagem
caminhoImagem = filedialog.askopenfilename()
# caminhoImagem = 'img/dante1.jpg'

imagemFace = Image.open(caminhoImagem).convert('L')
imagemFaceNP = np.array(imagemFace, 'uint8')
facesDetectadas = detectorFace.detectMultiScale(imagemFaceNP)
font = cv2.FONT_HERSHEY_COMPLEX_SMALL

print('Detect:', facesDetectadas)

if len(facesDetectadas) == 0:
    print('Nenhuma face detectada!')
else:
    for (x, y, l, a) in facesDetectadas:
        idprevisto, confianca = reconhecedor.predict(imagemFaceNP)

        nome = ''
        if idprevisto == 1:  # Implementar o Nome da pessoa junto do
            nome = 'Dante'
        elif idprevisto == 2:
            nome = 'Leonardo'
        elif idprevisto == 3:
            nome = 'Leonardo'
        else:
            nome = 'Desconhecido...'

        print('Encontrou a imagem de {}!'.format(nome))
        print('ID previsto {}!'.format(idprevisto))

        cv2.rectangle(imagemFaceNP, (x, y), (x + l, y + a), (0, 0, 255), 2)
        cv2.putText(imagemFaceNP, nome, (x, y + (a + 30)), font, 2, (0, 255, 0))  # Params: imagem, posicionamento do texto, fonte a usar, tamanho da fonte, cor da fonte
        cv2.putText(imagemFaceNP, str(confianca), (x, y + (a + 50)), font, 1, (0, 255, 0))  # Params: imagem, posicionamento do texto, fonte a usar, tamanho da fonte, cor da fonte

        cv2.imshow("Face", imagemFaceNP)
        cv2.waitKey(10000)
