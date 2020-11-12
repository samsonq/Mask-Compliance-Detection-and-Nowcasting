import numpy as np
import tensorflow as tf
import keras
from detector import Detector
from utils import load_config


if __name__ == "__main__":
    config = load_config("./models/cv_config.yaml")
    if config["use_gpu"]:
        assert tf.test.is_gpu_available(), "GPU is not available!"

    detector = Detector()
