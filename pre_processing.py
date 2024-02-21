from PIL import Image
import cv2
import numpy as np
# import os

def preprocess_image(image_path:str,ctype:str='svgcaptcha')->Image.Image:
    """Preprocess the image to make it easier to read by the OCR"""
    result = cv2.imread(image_path, 0)
    if ctype == 'svgcaptcha':
        #remove 25% from each side
        p25 = result.shape[0]/100*28
        w,h = result.shape
        #precrop
        result = result[int(p25*1.43):w-int(p25*0.95), int(p25):h-int(p25*0.9)]# top,bottom left:right
        # canny = cv2.Canny(result, 50,50)
        mask = np.full(result.shape, 255, dtype=np.uint8)
        result_not = cv2.bitwise_not(result)
        result_not = cv2.threshold(result_not, 202, 255, cv2.THRESH_BINARY)[1]
        baw = cv2.erode(result_not, np.ones((3,3), np.uint8), iterations=1)
        contours, hierarchy = cv2.findContours(baw, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)#find the contours
        for contour in contours:
            if cv2.contourArea(contour) < 2100:#remove the big contours (line that are along the border of the image)
                cv2.drawContours(mask, [contour], -1, 0, -1)
        baw = cv2.bitwise_and(baw, baw, mask=mask)
        kernel = np.ones((1,1), np.uint8)
        dilatation = cv2.dilate(mask, kernel, iterations=1)
        masked_img = cv2.threshold(dilatation, 240, 255, cv2.THRESH_BINARY)[1]
        r = 11#radius of the circle
        kernel = np.zeros((r*2,r*2), np.uint8)#create a circle
        cv2.circle(kernel, (r-2,r-2), r, 255, -1)#-2 => décalage pour le bas droit des lettres
        #dilate the image (to expand the text mask)
        masked_img = cv2.erode(masked_img, kernel, iterations=2)#erode to expend on white
        #apply the mask on the original image
        masked_img = cv2.bitwise_not(masked_img)
        result_not[masked_img == 0] = 255#apply the mask and replace the black pixels by white pixels
        result = result_not
        #find the first pixel of the image who has 0 value
        x, y = np.where(result == 0)
        result = result[x.min():x.max(), y.min():y.max()]
        new_img = np.zeros((120, 529), dtype=np.uint8)
        new_img.fill(255)
        center_left = (529 - result.shape[1])//2
        center_top = (120 - result.shape[0])//2#center the image and embed it in a 120x529 image
        new_img[center_top:center_top+result.shape[0], center_left:center_left+result.shape[1]] = result
        return Image.fromarray(new_img)
    elif ctype == 'pythoncaptcha':
        result = cv2.bitwise_not(result)
        result = cv2.threshold(result, 35, 255, cv2.THRESH_BINARY)[1]
        result = cv2.erode(result, np.ones((2,2), np.uint8), iterations=1)
        x,y = np.where(result == 0)
        result = result[x.min():x.max(), y.min():y.max()]
        #embed it in a 122 by 56 image
        new_img = np.zeros((56,122), dtype=np.uint8)
        new_img.fill(255)
        center_left = (122 - result.shape[1])//2
        center_top = (56 - result.shape[0])//2
        new_img[center_top:center_top+result.shape[0], center_left:center_left+result.shape[1]] = result
        return Image.fromarray(new_img)
        # start_top = int(result.shape[1]/100)
        # start_left = int(result.shape[0]/100*15)
        # result = result[int(start_left):result.shape[0]-int(start_left), int(start_top):result.shape[1]-int(start_top)]
