import cv2
import os
import numpy as np
from PIL import Image

# Script disponibilizado no curso https://www.udemy.com/course/reconhecimento-facial-com-python-e-opencv/

eigenface = cv2.face.EigenFaceRecognizer_create(40, 8000)
fisherface = cv2.face.FisherFaceRecognizer_create(3, 2000)
lbph = cv2.face.LBPHFaceRecognizer_create(2, 2, 7, 7, 50)

def getImagemComId():
    caminhos = [os.path.join('yalefaces/treinamento', f) for f in os.listdir('yalefaces/treinamento')]
    faces = []
    ids = []
    for caminhoImagem in caminhos:
       imagemFace = Image.open(caminhoImagem).convert('L')
       imagemNP = np.array(imagemFace, 'uint8')
       id = int(os.path.split(caminhoImagem)[1].split(".")[0].replace("subject", ""))
       ids.append(id)
       faces.append(imagemNP)

    return np.array(ids), faces

ids, faces = getImagemComId()

print("Treinando...")
# eigenface.train(faces, ids)
# eigenface.write('classifications/classificadorEigenYale.yml')

# fisherface.train(faces, ids)
# fisherface.write('classifications/classificadorFisherYale.yml')

lbph.train(faces, ids)
lbph.write('classifications/classificadorLBPHYale.yml')

print("Treinamento realizado")