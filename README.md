# Captcha_solving
All about creating a dataset, preprocessing images, and creating an actual model to solve captcha
<br>
<br>
<br>
# STEP 1 - creating a dataset
2 Méthodes : 
- unzip the captcha.7z archive, and put all image under the `captcha` folder
- OR use generator.js to create your own captcha(s)

## generator.js usage
- install generator.js dependencies by using `npm install` inside the same directory as package.json
- change `out = './temp'` to whatever temporary folder you want. Change `SIZE = [720,360]` to the size you want (its in width,height) and then change the `FORMAT = "webp"` to the format you want.
- run it : `node generator.js` , wait until its finished generating captcha.
<br>

 # STEP 2 - pre-processing images for training
 - install `pillow` using pip, then run process_images by using `python process_images.py` command.
<br>

# STEP 3 - creation a model
I based my creation on keras [documentation](https://keras.io/examples/vision/captcha_ocr/)
## configuration stuff:
- first download requirements : `pip install -r requirements.txt`
- second try to run it and see if it detect any gpu devices (if you have one), if it tells you that you have 0 available gpu and you are on windows,
I strongly recommand you to use wsl 2 by following tensorflow [tutorial](https://www.tensorflow.org/install/pip)<br><br> ![image](https://github.com/NotTrueFalse/Captcha_solving/assets/122208389/f238564d-583d-47a3-a698-38221c7d2ca5)
If you are on other platform and don't see any gpus, use tensorflow tutorial as well, I'm not an expert in this kind of situation

now we are going to talk about actually running the model:
- use `python MODEL_CREATION.py` then wait
- check if there is any problem with the sizen it'll tell you `img_width: [with], img_height: [height], Press Enter to continue...`
if its the good size (I made it so it resize the image to be 2 times smaller and does some cropping, so if you have in input a 720, 360 size, you'll see 300 by 100 size) then press enter.
<br>if it doesn't fit, try creating an issue and ask me why.
- if everything is fine, you'll have a popup with image and their labels, if the text doesn't correspond, create an issue.
- after some wait you'll have a text `Train, Press Enter to continue...`, this is the good part, where all the magic happens, after pressing enter it will train your model, all you have to do is wait until its finished.
- then it'll automaticly save the model, and show you a panel of image with their corresponding prediction. At this point you're pretty much done

# STEP 4 - Re-use the model
- put test captcha as unprocessed (as normal, not preprocessed) in a directory named `test`, then simply run `python main.py` and voilaa, you should see the prediction and the label of the image
- if prediction is bad, try to add more captcha to your dataset

That's all, if you have any problem or question, create an issue!
