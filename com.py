try :
    from PIL import Image
except ImportError:
    import Image

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
    text = ""
    num = ""
    ## -> testing
    if text==num:
        while time.time() < end_time:
          beepy.beep(sound=1)
    send()
        
      
cv2.destroyAllWindows()