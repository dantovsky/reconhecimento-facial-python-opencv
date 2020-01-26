import cv2

# Ideia geral: 1º faz a detecção da face para depois fazer o reconhecimento
# Captura a imagem que está atualmente na webcam e classifica em uma das classes feita no treinamento anteriormente

detectorFace = cv2.CascadeClassifier('classifiers/haarcascade-frontalface-default.xml')
reconhecedor = cv2.face.EigenFaceRecognizer_create()
reconhecedor.read('classificadorEigein.yml')
larrgura, altura = 220, 220
font = cv2.FONT_HERSHEY_COMPLEX_SMALL
camera = cv2.VideoCapture(0)

while (True):
    conectado, imagem = camera.read()
    imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    facesDetectadas = detectorFace.detectMultiScale(imagemCinza, scaleFactor=1.5, minSize=(30, 30))  # Colocar minSize baixo se tiver capturado a face de uma imagem pequena (150 seria um valor normal para capturas de um rosto normal)

    # Message to user (how to exit the program)
    cv2.putText(imagem, 'Press "q" to exit.', (larrgura, altura + (altura + 30)), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0))

    for (x, y, l, a) in facesDetectadas:
        imagemFace = cv2.resize(imagemCinza[y:y + a, x:x + l], (larrgura, altura))  # var para obter a imagem convertida para o tamanho 220x220

        # Desenhar o retangulo em volta da face
        cv2.rectangle(imagem, (x, y), (x + l, y + a), (0, 0, 255), 2)

        # Code que vai fazer o reconhecimento facial
        id, confianca = reconhecedor.predict(imagemFace)
        if id == 1:  # Implementar o Nome da pessoa junto do
            nome = 'Dante'
        else:
            nome = 'Caio'
        cv2.putText(imagem, nome, (x, y + (a + 30)), font, 2, (0, 0, 255))  # Params: imagem, posicionamento do texto, fonte a usar, tamanho da fonte, cor da fonte
        # cv2.putText(imagem, str(id), (x, y + (a + 30)), font, 2, (0, 0, 255))  # Params: imagem, posicionamento do texto, fonte a usar, tamanho da fonte, cor da fonte

    cv2.imshow('Face', imagem)
    if cv2.waitKey(1) == ord('q'):  # Break the cicle when click "q" key
        break

camera.release()
cv2.destroyAllWindows()