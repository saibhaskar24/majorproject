import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import models
from tensorflow.keras.preprocessing import image
import numpy as np

model = keras.models.load_model("my_model.h5")

print(model)

def predictImage(filename):
    img1 = image.load_img(filename,target_size=(150,150))
 
    Y = image.img_to_array(img1)
    
    X = np.expand_dims(Y,axis=0)
    val = int(model.predict(X))
    if val == 0:
        return 0
    elif val == 1:
        return 1

#/Users/pbbhsk/Documents/mycode/blogapp/images/bad/alcohol.jpg
# predictImage("/Users/pbbhsk/Documents/mycode/blogapp/images/bad/alcohol.jpg")