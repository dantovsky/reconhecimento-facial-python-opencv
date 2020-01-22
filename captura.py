import cv2

classificador = cv2.CascadeClassifier("classifiers/haarcascade-frontalface-default.xml")
camera = cv2.VideoCapture(0)  # 0 is the number of the first cam (of computer)

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
    facesDetectadas = classificador.detectMultiScale(imagemCinza, scaleFactor=1.5, minSize=(100,100))

    # Cicle to draw the rectangle (or square) envolving the face
    # l :: width, a :: height
    for (x, y, l, a) in facesDetectadas:
        # params :: (image to aplay rectangle, start point, end point, rectangle's color, border to draw
        cv2.rectangle(imagem, (x, y), (x + l, y + a), (0, 0, 255), 2)

    # Show them webcam image
    cv2.imshow("Face", imagem)
    cv2.waitKey(1)  # ???

camera.release()  # flush memory
cv2.destroyAllWindows()

# haarcascade-frontalface-default => XML file to do the face training detection (arquivo para fazer o treinamento de deteção de faces)