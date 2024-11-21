#  Previous copy of com.py
try :
    from PIL import Image
except ImportError:
    import Image

from demo import *
# from plate import * 
from loc1 import *
import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def recText(filename):
    text = pytesseract.image_to_string(filename,lang='eng')
    return text

while True:
    # cap()
    if cv2.waitKey(1) == ord('q'):
        break
    info = recText('1.png')
    text = ''.join(e for e in info if e.isalnum())
    print("Number is:",text)
    

    
    ## <- testing 
    num = "RJ14CV0002"
    ## -> testing
    if text == "" :
        print('Not Found')
    if text==num:
        winsound.Beep(frequency, duration)
        while time.time() < end_time:
            beepy.beep(sound=1)
        send(text)
    break
      
cv2.destroyAllWindows()