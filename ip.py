import cv2
import imutils
import numpy as np
import requests

while True:
    images = requests.get("http://192.168.2.149:8080/shot.jpg")
    vedionp = np.array(bytearray(images.content),dtype=np.uint8)
    ved = cv2.imdecode(vedionp,-1)
    img = imutils.resize(ved,width=1000)
    cv2.imshow("Mobile IPCamera",img)
    if ord("q") == cv2.waitKey(1):
        exit(0)
