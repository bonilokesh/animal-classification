import numpy as np
import streamlit as st
from tensorflow.keras import models
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.image import img_to_array
from PIL import Image

model = load_model("/content/animal_model.h5")
st.header("ANIMAL CLASSIFICATION")

image_path = st.file_uploader("upload the file" , type=["jpg" , "jpeg" , "png"])

if image_path is not None:
    
    img = image.load_img(image_path, target_size=(48, 48))
    x = img_to_array(img)
    x = np.expand_dims(x, axis=0)
    classes = model.predict(x)

    details = {'antelope': 0,
    'badger': 1,
    'bat': 2,
    'bear': 3,
    'bee': 4,
    'beetle': 5,
    'bison': 6,
    'boar': 7,
    'butterfly': 8,
    'cat': 9,
    'caterpillar': 10,
    'chimpanzee': 11,
    'cockroach': 12,
    'cow': 13,
    'coyote': 14,
    'crab': 15,
    'crow': 16,
    'deer': 17,
    'dog': 18,
    'dolphin': 19,
    'donkey': 20,
    'dragonfly': 21,
    'duck': 22,
    'eagle': 23,
    'elephant': 24,
    'flamingo': 25,
    'fly': 26,
    'fox': 27,
    'goat': 28,
    'goldfish': 29,
    'goose': 30,
    'gorilla': 31,
    'grasshopper': 32,
    'hamster': 33,
    'hare': 34,
    'hedgehog': 35,
    'hippopotamus': 36,
    'hornbill': 37,
    'horse': 38,
    'hummingbird': 39,
    'hyena': 40,
    'jellyfish': 41,
    'kangaroo': 42,
    'koala': 43,
    'ladybugs': 44,
    'leopard': 45,
    'lion': 46,
    'lizard': 47,
    'lobster': 48,
    'mosquito': 49,
    'moth': 50,
    'mouse': 51,
    'octopus': 52,
    'okapi': 53,
    'orangutan': 54,
    'otter': 55,
    'owl': 56,
    'ox': 57,
    'oyster': 58,
    'panda': 59,
    'parrot': 60,
    'pelecaniformes': 61,
    'penguin': 62,
    'pig': 63,
    'pigeon': 64,
    'porcupine': 65,
    'possum': 66,
    'raccoon': 67,
    'rat': 68,
    'reindeer': 69,
    'rhinoceros': 70,
    'sandpiper': 71,
    'seahorse': 72,
    'seal': 73,
    'shark': 74,
    'sheep': 75,
    'snake': 76,
    'sparrow': 77,
    'squid': 78,
    'squirrel': 79,
    'starfish': 80,
    'swan': 81,
    'tiger': 82,
    'turkey': 83,
    'turtle': 84,
    'whale': 85,
    'wolf': 86,
    'wombat': 87,
    'woodpecker': 88,
    'zebra': 89}


    value_to_find = np.argmax(classes)
    for key, value in details.items():
        if value == value_to_find:
            print(key)
            st.write(key)
            st.image(image_path)
            break
      
else:
  st.write("please upload the file")      