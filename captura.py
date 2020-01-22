import cv2

"""
Tabalho 3 - Parte Bônus
Professor: Armando Pinho
Alunos: Borys Chystov, Dante Marinho e Francisco Santos
"""

classificador = cv2.CascadeClassifier("classifiers/haarcascade-frontalface-default.xml")
camera = cv2.VideoCapture(0)  # 0 is the number of the first cam (of computer)
amostra = 1  # number of photos taken when press a certain key
numeroAmostras = 25
id = input('Digite seu identificador: ')
largura, altura = 220, 220  # size of samples
print('Capturando as faces (25 amostras) ...')
# Message to

while (True):
    conectado, imagem = camera.read()  # reading the webcam

    # var to detect image in gray scale => better algorithm perforcance
    imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

    # facesDetectadas => saves all faces found by the algorithm (this var have a matrix with positions x and y (start point of a face) and the face width and height
    # classificator was trained with the haarcascade-frontalface-default.xml file
    # params:
    # imagemCinza :: image where I want to detect faces
    # scaleFactor :: indicate the image scale
    # minSize :: min to do the face detection
    facesDetectadas = classificador.detectMultiScale(imagemCinza, scaleFactor=1.5, minSize=(150, 150))

    # Cicle to draw the rectangle (or square) envolving the face
    # l :: width, a :: height
    for (x, y, l, a) in facesDetectadas:
        # params :: (image to aplay rectangle, start point, end point, rectangle's color, border to draw
        cv2.rectangle(imagem, (x, y), (x + l, y + a), (0, 0, 255), 2)

        # Saving one sample (image of the moment) when press key "q"
        if cv2.waitKey(1) & 0xFF == ord('q'):
            # Resizing the image
            imagemFace = cv2.resize(imagemCinza[y:y + a, x:x + l], (largura, altura))

            # Save the sample
            # cv2.imshow("Imagem", imagem)
            cv2.imwrite("photos/pessoa." + str(id) + "." + str(amostra) + ".jpg", imagemFace)
            print("[foto " + str(amostra) + " capturada com sucesso]")
            amostra += 1

    # Show them webcam image
    cv2.imshow("Face", imagem)
    cv2.waitKey(1)  # "wainting for a key" (uncomment if running with problems)

    # Stop capturing from webcam when taken 25 samples
    if (amostra >= numeroAmostras + 1):
        break

print("Amostras da face capturadas com sucesso.")
camera.release()  # flush memory
cv2.destroyAllWindows()

# haarcascade-frontalface-default => XML file to do the face training detection (arquivo para fazer o treinamento de deteção de faces)