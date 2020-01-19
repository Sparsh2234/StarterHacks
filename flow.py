import tensorflow as tf

from tensorflow.keras.callbacks import TensorBoard

NAME = "Cats-vs-dogs-CNN"

tensorboard = TensorBoard(log_dir="logs/{}".format(NAME))

# model.fit(x, y,
 #          batch_size=32,
  #         epochs=3,
   #        validation_split=0.3,
    #       callbacks=[tensorboard])

from tensorflow.keras.datasets import cifar10
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten
from tensorflow.keras.layers import Conv2D, MaxPooling2D
# more info on callbakcs: https://keras.io/callbacks/ model saver is cool too.
from tensorflow.keras.callbacks import TensorBoard
import pickle
import time
import csv
import numpy

NAME = "Heart Attack Risk"

pickle_in = csv.DictReader(open("my_csv_file.csv","r"))


pickle_in = [line for line in pickle_in]


headers = pickle_in[0].keys()



with open('filename.pickle', 'wb') as handle:
    pickle.dump(pickle_in, handle, protocol=pickle.HIGHEST_PROTOCOL)

with open('filename.pickle', 'rb') as handle:
    pickle_in = pickle.load(handle)

print(pickle_in)



#X = pickle.load(pickle_in)

#pickle_in = open("y.pickle","rb")
#y = pickle.load(pickle_in2)

X = pickle_in
X = X/255.0


model = Sequential()

model.add(Conv2D(256, (3, 3), input_shape=X[0].shape[1:]))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(256, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())  # this converts our 3D feature maps to 1D feature vectors
model.add(Dense(64))

model.add(Dense(1))
model.add(Activation('sigmoid'))

tensorboard = TensorBoard(log_dir="logs/{}".format(NAME))

model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['accuracy'],
              )

model.fit(X, y,
          batch_size=32,
          epochs=3,
          validation_split=0.3,
          callbacks=[tensorboard])
