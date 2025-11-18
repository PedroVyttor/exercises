import cv2

def tirar_foto(nome_arquivo):
    cam = cv2.VideoCapture(3)

    ret, frame = cam.read()
    if ret:
        cv2.imwrite('foto.png', frame)

#desabilito a webcam ou libero a webcam
    cam .release()