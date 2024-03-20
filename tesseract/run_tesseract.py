import argparse
parser = argparse.ArgumentParser('test.py')
parser.add_argument('--img')
parser.add_argument('--scale')
parser.add_argument('--bin')
args = parser.parse_args()
import pytesseract
from pytesseract import Output
import cv2
import os

def show_img(img, name):
    name = os.path.join('results', name + '.png')
    
    d = pytesseract.image_to_data(img, output_type=Output.DICT, lang="rus+eng")
    n_boxes = len(d['level'])

    img = cv2.resize(img, None, fx=cof, fy=cof)

    for i in range(n_boxes):
        (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])

        (x, y, w, h) = (x*cof, y*cof, w*cof, h*cof)
        
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 1)

        img = cv2.putText(img, (str(d['conf'][i]) + "% " + str(d['text'][i])), (x, y), 
            cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
        #print(str(d['text'][i]))
    cv2.imshow('img', img)
    cv2.waitKey(0)
    cv2.imwrite(name, img)
    print('Written:', name)




if args.img == None:
    img = cv2.imread('imgs//Пример//1330.jpg')
else:
    img = cv2.imread(args.img)
cof = 1
if args.scale != None:
    cof = args.scale
    cof = int(cof)



show_img(img, 'default')



if args.bin != None:
    val = 255
    im_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    show_img(im_gray, 'GREY')

    _, im_bw = cv2.threshold(im_gray, 128, val, cv2.THRESH_OTSU)
    print("OTSU", _)
    im_bw = cv2.cvtColor(im_gray, cv2.COLOR_GRAY2BGR)
    show_img(im_bw,"OTSU")

    _, im_bw =  cv2.threshold(im_gray, 92, val, cv2.THRESH_BINARY)
    print("BINARY", _)
    im_bw = cv2.cvtColor(im_gray, cv2.COLOR_GRAY2BGR)
    show_img(im_bw,"BINARY")

    im_bw = cv2.adaptiveThreshold(im_gray,val,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,11,2)
    print("ADPTIVE GAUSSIAN", _)
    im_bw = cv2.cvtColor(im_gray, cv2.COLOR_GRAY2BGR)
    show_img(im_bw, "ADPTIVE GAUSSIAN")

    im_bw = cv2.adaptiveThreshold(im_gray,val,cv2.ADAPTIVE_THRESH_MEAN_C,\
            cv2.THRESH_BINARY,11,2)
    print("ADPTIVE MEAN_C", _)
    im_bw = cv2.cvtColor(im_gray, cv2.COLOR_GRAY2BGR)
    show_img(im_bw, "ADPTIVE MEAN_C")








