# -*- coding: utf-8 -*-
"""CNNs_with_Keras.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CPTn36dFAuMJvtDaZ2mpNB1un4xCiDZl

# Deep Learning with Keras and Tensorflow

## Getting Prepared

Download and extract the dataset
"""

!wget 'https://github.com/sadeepj/eth-80/releases/download/0.0.1/eth-80.tar.gz'

!tar xvf eth-80.tar.gz

"""Verify that the data is there"""

from PIL import Image
from IPython.display import display

im = Image.open('eth-80/train_set/dog/dog4/dog4-066-207.png')

!pip install tensorboardcolab

display(im)

import numpy as np
image_arr = np.array(im)
image_arr.shape
image_arr

"""## Module import and variable initialization

"""

import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorboardcolab import TensorBoardColab, TensorBoardColabCallback
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# dimensions of our images.
img_width, img_height = 128, 128



train_data_dir = 'eth-80/train_set'
validation_data_dir = 'eth-80/val_set'
nb_train_samples = 2952
nb_validation_samples = 328
epochs = 50
batch_size = 32

"""## Define the CNN model"""



#New Tensorflow model
input_shape = (img_width, img_height, 3)
model = tf.keras.Sequential()
model.add(tf.keras.layers.Conv2D(32, (3, 3),activation='relu',input_shape=input_shape))
model.add(tf.keras.layers.MaxPool2D(pool_size=(2, 2)))
model.add(tf.keras.layers.Conv2D(32, (3, 3),activation='relu'))
model.add(tf.keras.layers.MaxPool2D(pool_size=(2, 2)))
model.add(tf.keras.layers.MaxPool2D(pool_size=(2, 2)))

model.add(tf.keras.layers.Conv2D(64, (3, 3),activation='relu'))
model.add(tf.keras.layers.MaxPool2D(pool_size=(2, 2)))

model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dense(64,activation='relu'))


d2 = tf.keras.layers.Dense(64,activation='relu')
model.add(d2)

model.add(tf.keras.layers.Dropout(0.5))
d3 =  tf.keras.layers.Dense(8,activation='softmax')
model.add(d3)

model.compile(
    loss='categorical_crossentropy',
    optimizer='rmsprop',
    metrics=['accuracy']
)

weights = d3.get_weights()
weights[1].shape

"""## Prepare data feeders"""

# this is the data augmentation configuration we will use for training
train_datagen = ImageDataGenerator(
    rescale=1. / 255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True
)

from google.colab import drive
drive.mount('/content/drive')

# this is the augmentation configuration we will use for testing:
# only rescaling
test_datagen = ImageDataGenerator(rescale=1. / 255)

train_generator = train_datagen.flow_from_directory(
    train_data_dir,
    target_size=(img_width, img_height),
    batch_size=batch_size,
    class_mode='categorical'
)

validation_generator = test_datagen.flow_from_directory(
    validation_data_dir,
    target_size=(img_width, img_height),
    batch_size=batch_size,
    class_mode='categorical'
)

"""## Test the data feeders"""

datum = next(train_generator)
image_batch, label_batch = datum
image_batch.shape
k = 3
image = image_batch[k, ...]
label = label_batch[k, ...]

label

display(Image.fromarray((image * 255).astype(np.uint8)))

image_batch.shape

# Commented out IPython magic to ensure Python compatibility.


import datetime
# Load the TensorBoard notebook extension
# %load_ext tensorboard

# Clear any logs from previous runs
!rm -rf ./logs/


log_dir = "logs/fit/" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=log_dir, histogram_freq=1)

"""## Fit the model"""

# tbc = TensorBoardColab()
model.fit_generator(
    train_generator,
    steps_per_epoch=nb_train_samples // batch_size,
    epochs=epochs,
    validation_data=validation_generator,
    validation_steps=nb_validation_samples // batch_size,
    callbacks = [tensorboard_callback]
)

# Commented out IPython magic to ensure Python compatibility.
# %tensorboard --logdir logs/fit

"""## Save the weights"""

model.save_weights('saved_weights.h5')

# model.load_weights('source_file.h5')

"""## Make predictions with the trained CNN!"""

im = Image.open(/images.jfif')

img = np.array(im) / 255.

img.shape

img = img[np.newaxis, ...]

img.shape

out = model.predict_on_batch(img)

out

np.sum(out)

np.argmax(out)

