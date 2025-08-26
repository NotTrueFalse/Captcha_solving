import tensorflow as tf
import keras
from decoder import decode_batch_predictions
from PIL import Image

def predict(impath:str|Image.Image, model:keras.Model):
    if type(impath) != str:
        impath.save('temp.png')
        impath = 'temp.png'
    img = tf.io.read_file(impath)
    img = tf.io.decode_png(img, channels=1)
    img = tf.image.convert_image_dtype(img, tf.float32)
    img_height, img_width = img.shape[0], img.shape[1]
    # img_height, img_width = 360, 720
    img = tf.image.resize(img, [img_height, img_width])
    img = tf.transpose(img, perm=[1, 0, 2])
    img = tf.expand_dims(img, axis=0)
    predi = model.predict(img, verbose=0)
    pred_texts = decode_batch_predictions(predi)
    return pred_texts