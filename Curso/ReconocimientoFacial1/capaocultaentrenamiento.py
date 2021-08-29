import cv2 as cv
import os
import numpy as np
from time import time

dataRuta = 'D:\Proyectos Python\Curso\ReconocimientoFacial1\Data'
listaData = os.listdir(dataRuta)
#print('Data', listaData)
ids = []
rostrosData  = []
id = 0
tiempoInicial = time()

for fila in listaData:
    rutaCompleta = dataRuta+'/'+ fila
    print('Iniciando lectura...')
    for archivo in os.listdir(rutaCompleta):

        print('Imagenes: ', fila + '/'+ archivo)

        ids.append(id)
        rostrosData.append(cv.imread(rutaCompleta+'/'+archivo,0))
    
    id = id+1
    tiempoFinallLectura = time()
    tiempoTotalLectura = tiempoFinallLectura-tiempoInicial
    print('Tiempo total lectura: ',tiempoTotalLectura)

entrenamientoEigenFaceRecognize = cv.face.EigenFaceRecognizer_create()
print('Iniciando el entrenamiento... Espere')
entrenamientoEigenFaceRecognize.train(rostrosData, np.array(ids))
tiempoFinalEntrenamiento = time()
tiempoTotalEntrenamiento = tiempoFinalEntrenamiento-tiempoTotalLectura
print('Tiempo entrenamiento total: ', tiempoTotalEntrenamiento)
entrenamientoEigenFaceRecognize.write('EntrenamientoEigenFaceRecognize.xml')
print('Entrenamiento finalizado')