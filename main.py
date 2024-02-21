from pre_processing import preprocess_image
from prediction import predict
import keras
import os
model = keras.saving.load_model('predi_model.h5')
test_directory = './test'

for image_path in os.listdir(test_directory):
    img = preprocess_image(f"{test_directory}/{image_path}")
    prediction = predict(img, model)
    label = image_path.split('.')[0].split('/')[-1]
    print("Prediction: ", prediction, "Label: ", label)
