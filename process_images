from pre_processing import preprocess_image
import os
i = 0
l = len(os.listdir("out"))
for img in os.listdir("out"):
    i += 1
    if img.endswith(".png"):
        #reverse the color
        result = preprocess_image('out/'+img)
        result.save('captcha/'+img)
        try:
            os.remove('out/'+img)
        except:pass
        print(f"[*] {i} images processed {i}/{l}, {round(i/l*100, 2)}%"," "*20, end="\r")
