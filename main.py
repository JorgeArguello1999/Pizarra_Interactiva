import cv2
import numpy as np

cap= cv2.VideoCapture(0,cv2.CAP_DSHOW)
celesteBajo= np.array([75, 185, 88], np.uint8)

# Colores para pintar 
colorCeleste= (255,113,82)
colorAmarillo= (89,222,255)
colorRosa= (128,0,255)
colorVerde=(0,255,36)

colorLimpiarPantalla= (29,112,246)

# Grosor de linea 
grosorCeleste= 6
grosorAmarillo= 2
grosorRosa= 2
grosorVerde= 2

# Grosor de linea recuadro
grosorPeque= 6
grosorMedio= 1
grosorGrande= 1

"""
Variables que definen el color del marcador o lapiz
"""
color= colorCeleste
grosor= 3

# Proceso acumulador usado para guardar el trazo
x1=None
y1=None
imAux=None

# Prueba de funcionamiento
while True:
    ret, frame= cap.read()
    if ret==False:break
    cv2.imshow('frame', frame)
    k=cv2.waitKey(1)
    if k==27:
        break
cap.release()
cv2.destroyAllWindows()
