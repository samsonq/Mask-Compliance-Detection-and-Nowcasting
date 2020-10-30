import numpy as np
import tensorflow as tf
import keras


class NowcastModel:
    """

    """
    def __init__(self, config):
        """
        Initialize model hyperparameters.
        :param config: .yaml file containing model specifications
        """
        self.path = config["model_path"]
        self.gpu = config["use_gpu"]
        if self.gpu:
            assert tf.test.is_gpu_available(), "GPU is not available!"
        self.epochs = config["epochs"]
