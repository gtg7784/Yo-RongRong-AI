
from tensorflow.keras.layers import Input, BatchNormalization, Conv2D, MaxPool2D, Flatten, Dropout, Dense
from tensorflow.keras.models import Model

def ConvBlock(x, filters):
  x = BatchNormalization()(x)
  x = Conv2D(filters, (3, 3), activation='relu', padding='same')
  x = MaxPool2D((2, 2), strides=(2, 2))(x)

  return x

def YRRModel(input_shape, n_classes):
  input_tensor = Input(shape=input_shape)

  x = ConvBlock(input_tensorm, 32)
  x = ConvBlock(x, 64)
  x = ConvBlock(x, 128)
  x = ConvBlock(x, 256)
  x = ConvBlock(x, 512)
  x = BatchNormalization()(x)
  x = Dense(512, activation='relu')(x)
  x = Dense(512, activation='relu')(x)
  x = Dropout(.4)(x)

  output_layer = Dense(n_classes, activation='softmax')(x)

  inputs = [input_tensor]

  model = Model(n_classes, output_layer)

  return model
