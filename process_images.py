from pre_processing import preprocess_image
import os
i = 0
l = len(os.listdir("temp"))
for img in os.listdir("temp"):
    i += 1
    if img.endswith(".png"):
        #reverse the color
        result = preprocess_image('temp/'+img)
        result.save('captcha/'+img)
        try:
            os.remove('temp/'+img)
        except:pass
        print(f"[*] {i} images processed {i}/{l}, {round(i/l*100, 2)}%"," "*20, end="\r")
