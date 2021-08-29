import cv2 as cv
import os
import imutils

modelo = 'FotosElon'
ruta1 =  'D:/Proyectos Python/Curso/ReconocimientoFacial1'
rutaCompleta = ruta1+'/'+ modelo
if not os.path.exists(rutaCompleta):
    os.makedirs(rutaCompleta)

camara = cv.VideoCapture('D:\Proyectos Python\Curso\ReconocimientoFacial1/ElonMusk.mp4')
ruidos = cv.CascadeClassifier('D:\Proyectos Python\Curso\Entrenamientos OpenCV Ruidos\opencv-master\data\haarcascades\haarcascade_frontalface_default.xml')
id = 0
while True: 
    respuesta,captura = camara.read()
    if respuesta == False:break
    captura = imutils.resize(captura, width = 640)

    grises = cv.cvtColor(captura, cv.COLOR_BGR2GRAY)
    idCaptura = captura.copy()

    cara = ruidos.detectMultiScale(grises, 1.3,5)

    for(x,y,e1,e2) in cara:
        cv.rectangle(captura, (x,y), (x+e1,y+e2), (0,0,255),2)
        rostroCapturado = idCaptura[y:y+e2,x:x+e1 ]
        rostroCapturado = cv.resize(rostroCapturado, (160,160), interpolation=cv.INTER_CUBIC)
        cv.imwrite(rutaCompleta+'/imagen_{}.jpg'.format(id), rostroCapturado)
        id = id+1

    cv.imshow("Resultado rostro", captura)

    if id == 351:
        break
camara.release()
cv.destroyAllWindows()