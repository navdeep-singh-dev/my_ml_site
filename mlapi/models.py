from sklearn.linear_model import SGDClassifier
import cv2
import numpy as np


# Create your models here.
class DigitRecognition:
    instance = None
    def __init__(self):
        self.seed = 40
    def train(self, train,test):
        self.model = SGDClassifier(random_state=self.seed)
        self.model.fit(train, test)
    def readImage(self,imageBytes):
        img = cv2.imdecode(np.frombuffer(imageBytes, np.uint8), -1)
        #Converting to Binary Image
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        #Thresholding
        ret, th = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV,      cv2.THRESH_OTSU)
        # find image main content corners
        contoursAll = cv2.findContours(th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contours = contoursAll[0]
        for cnt in contours:
            x, y, w, h = cv2.boundingRect(cnt)
            # create rectangle
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 1)
            print(x,y,w,h)
            top = int(0.05 * th.shape[0])
            bottom = top
            left = int(0.05 * th.shape[1])
            right = left
            th_up = cv2.copyMakeBorder(th, top, bottom, left, right, cv2.BORDER_REPLICATE)
            print('Ractangle')
            print(top,bottom,left,right,th_up)
            # Extract the image's region of interest
            roi = th[y - top : y + h + bottom, x - left : x + w + right]
            digit, acc = self.predict_digit(roi)
            return digit, acc

    def predict_digit(self,reshapedImage):
            print(reshapedImage.shape)
            return (0,0)
            # return DigitRecognition.instance.model.predict(reshapedImage)
    