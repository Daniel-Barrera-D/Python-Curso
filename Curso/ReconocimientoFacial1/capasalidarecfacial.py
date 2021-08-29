import cv2 as cv
import os
import imutils
dataRuta = 'D:\Proyectos Python\Curso\ReconocimientoFacial1\Data'
listaData = os.listdir(dataRuta)
entrenamientoEigenFaceRecognize = cv.face.EigenFaceRecognizer_create()
entrenamientoEigenFaceRecognize.read('D:\Proyectos Python\Curso\ReconocimientoFacial1\EntrenamientoEigenFaceRecognize.xml')
ruidos = cv.CascadeClassifier('D:\Proyectos Python\Curso\Entrenamientos OpenCV Ruidos\opencv-master\data\haarcascades\haarcascade_frontalface_default.xml')
#camara = cv.VideoCapture('D:\Proyectos Python\Curso\ReconocimientoFacial1/ElonMusk.mp4')
camara = cv.VideoCapture(0)
while True:
    respuesta,captura = camara.read()
    if respuesta == False:break
    captura = imutils.resize(captura, width=640)
    grises = cv.cvtColor(captura, cv.COLOR_BGR2GRAY)
    idCaptura = grises.copy()
    cara = ruidos.detectMultiScale(grises,1.3,5)
    
    for(x,y,e1,e2) in cara:
        rostroCapturado = idCaptura[y:y+e2,x:x+e1 ]
        rostroCapturado = cv.resize(rostroCapturado, (160,160), interpolation=cv.INTER_CUBIC)
        resultado = entrenamientoEigenFaceRecognize.predict(rostroCapturado)
        cv.putText(captura, '{}'.format(resultado), (x,y-5), 1,1.3, (0,255,0),1,cv.LINE_AA)
        if resultado[1]<9000:
            cv.putText(captura, "No encontrado", (x,y-20), 2,1.1, (0,255,0),1,cv.LINE_AA)
            cv.rectangle(captura, (x,y), (x+e1,y+e2), (255,0,0),2)
        else:
            cv.putText(captura, '{}'.format(listaData[resultado[0]]), (x,y-20), 2,0.7, (0,255,0),1,cv.LINE_AA)
            cv.rectangle(captura, (x,y), (x+e1,y+e2), (255,0,0),2)

    cv.imshow("Resultados", captura)
    if cv.waitKey(1) == ord ('q'):
        break
camara.release()
cv.destroyAllWindows()