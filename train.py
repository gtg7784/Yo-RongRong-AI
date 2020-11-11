from .model import *
from tensorflow.keras.optimizers import Adam

def train():
  input_height = 48
  input_width = 48
  input_channel = 3
  input_shape = (input_height, input_width, input_channel)
  n_classes = 6

  model = YRRModel(input_shape, n_classes)
  adam = Adam()
  model.compile(
  optimizer=adam,
  loss='categorical_crossentropy', metrics=['acc'])

  data_dir = './data'