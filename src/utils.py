import numpy as np
import pandas as pd
import yaml


def load_config(path):
    """
    Load the configuration from cv_config.yaml.
    """
    return yaml.load(open(path, 'r'), Loader=yaml.SafeLoader)


def augmentation():
    """

    :return:
    """
    return ImageDataGenerator(rotation_range=20,
                              zoom_range=0.15,
                              width_shift_range=0.2,
                              height_shift_range=0.2,
                              shear_range=0.15,
                              horizontal_flip=True,
                              fill_mode="nearest")
