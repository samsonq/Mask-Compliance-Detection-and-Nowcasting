import numpy as np
import pandas as pd
import yaml


def load_config(path):
    """
    Load the configuration from cv_config.yaml.
    """
    return yaml.load(open(path, 'r'), Loader=yaml.SafeLoader)
