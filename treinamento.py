import cv2
import os
import numpy as np

# Classificadores (3 algoritmos diferentes)
eigenface = cv2.face.EigenFaceRecognizer_create()
fisherface = cv2.face.FisherFaceRecognizer_create()
lbph = cv2.face.LBPHFaceRecognizer_create()

# Método responsável por percorrer o banco de imagens de treinamento, e retorna os respetivos IDs de cada pessoa e as
# respetivas imagens. Exemplo: { pessoa_1: [img1, im2, img3] }
def getImagemComid():
    caminhos = [os.path.join('photos', f) for f in os.listdir('photos')]
    # print(caminhos)
    faces = []  # guardar as faces de cada pessoa "xpto"
    ids = []  # guardar os IDs de cada pessoa "xpto"

    # Ler as imagens
    for caminhoImagem in caminhos:
        # imread() faz a leitura de uma imagem no doretório
        imagemFace = cv2.cvtColor(cv2.imread(caminhoImagem), cv2.COLOR_BGR2GRAY)

        # Get ids de todas as imagens
        id = os.path.split(caminhoImagem)[-1].split('.')[1]  # erro ao fazer cast para int
        # print(id)
        ids.append(id)  # add ID na lista de IDs
        faces.append(imagemFace)  # add face na lista de faces

        # Pega a imagem e converte para escala de cinza
        # Testing: existe todas as imagens da pasta de imagens
        # cv2.imshow('Face', imagemFace)
        # cv2.waitKey(10)
    return np.array(ids), faces  # converte a lista de ids para o tipo np.array (tipo de dado requerido para fazer o treinamento)

ids, faces = getImagemComid()
print(ids)

print(faces)