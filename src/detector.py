import os
import numpy as np
import random
from matplotlib import pyplot as plt

import tensorflow as tf
import keras
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.layers import Dense, Dropout, Flatten, Input, AveragePooling2D
from tensorflow.keras.models import Sequential, Model
from tensorflow.keras.optimizers import Adam, RMSprop
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array, load_img
from tensorflow.keras.utils import to_categorical
from sklearn.preprocessing import LabelBinarizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from imutils import paths
from utils import load_config

import argparse
import warnings
warnings.filterwarnings("ignore")


class Detector:
    """
    Mask detector
    """
    def __init__(self, config):
        self.img_size = config["img_size"]
        self.epochs = config["epochs"]
        self.learning_rate = config["learning_rate"]
        self.batch_size = config["batch_size"]
        self.parameters = {"Image Size": self.img_size, "Epochs": self.epochs, "Learning Rate": self.learning_rate,
                           "Batch Size": self.batch_size}

        transfer_model = MobileNetV2(weights="imagenet", include_top=False,
                                     input_tensor=Input(shape=(self.img_size, self.img_size, 3)))
        head = transfer_model.output
        head = AveragePooling2D(pool_size=(7, 7))(head)
        head = Flatten(name="flatten")(head)
        head = Dense(128, activation="relu")(head)
        head = Dropout(0.5)(head)
        head = Dense(2, activation="softmax")(head)

        self.model = Model(inputs=transfer_model.input, outputs=head)

        # freeze pre-trained layers during first training process
        for layer in transfer_model.layers:
            layer.trainable = False

    def __str__(self):
        """

        :return:
        """
        return self.parameters

    def train(self, X_train, y_train, X_valid, y_valid):
        """

        :return:
        """
        opt = Adam(lr=self.learning_rate, decay=self.learning_rate / self.epochs)
        self.model.compile(loss="binary_crossentropy", optimizer=opt,
                           metrics=["accuracy"])

        # train the head of the network
        history_head = self.model.fit(aug.flow(X_train, y_train, batch_size=self.batch_size),
                                      steps_per_epoch=len(X_train) // self.batch_size,
                                      validation_data=(X_valid, y_valid),
                                      validation_steps=len(X_valid) // self.batch_size,
                                      epochs=self.epochs)

    def detect(self):
        """

        :return:
        """
        pass
