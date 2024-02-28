
import pytesseract
from pytesseract import Output
import cv2

class Model():
    # input is a cv2 image
    def predict(img):
        output = pytesseract.image_to_data(img, output_type=Output.DICT, lang="rus+eng")
        #this will return array of words
        return output['text']

