from PIL import Image
import PIL.ImageOps
# import os

def preprocess_image(image_path:str):
    result = Image.open(image_path)
    result = result.convert('RGB')
    result = PIL.ImageOps.invert(result)
    result = result.convert('L')
    #contraast at 255
    # result = result.point(lambda x: 0 if x < 50 else 255, '1')
    result = result.point(lambda x: 0 if x < 205 else 255, '1')
    #resize to the size/2
    result = result.resize((result.size[0]//2, result.size[1]//2))
    #crop the image
    P = result.size[0]//100*10
    P2 = result.size[1]//100*40
    result = result.crop((P, P2, result.size[0]-P, result.size[1]-P2))
    return result
