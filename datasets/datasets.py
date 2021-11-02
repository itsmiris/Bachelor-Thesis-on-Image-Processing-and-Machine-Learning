from typing import *
import os
import glob

import numpy as np
from numpy.typing import *

from config import config


def get_images_filepaths_list() -> List[str]:
    return sorted(glob.glob(config["datasets"]["paths"]["images"] + "*.jpg"))


def get_train_image_paths() -> NDArray[str]:
    train_image_paths = []
    with open(config["datasets"]["paths"]["ava"], mode='r') as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            token = line.split()
            id = int(token[0])

            file_path = config["datasets"]["paths"]["images"] + str(id) + '.jpg'
            if os.path.exists(file_path):
                train_image_paths.append(file_path)

    return np.array(train_image_paths)


def get_train_and_val_image_paths_and_write_scores(split_size=config["datasets"]["train_val_split_size"], scores_out_filename=config["misc"]["scores_filepath"])\
        -> Tuple[NDArray[str], NDArray[str]]:
    train_image_paths = []

    print("Loading training set and val set")
    with open(config["datasets"]["paths"]["ava"], mode='r') as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            token = line.split()
            nume = int(token[1])
            values = np.array(token[2:12], dtype='float32')
            score = 0.0
            for i in range(len(values)):
                score += values[i] * (i + 1)
            score /= values.sum()
            score = round(score, 2)

            file_path = config["datasets"]["paths"]["images"] + str(nume) + '.jpg'
            if os.path.exists(file_path):
                train_image_paths.append(file_path)

            with open(scores_out_filename, "a") as g:
                g.write(str(score) + '\n')

    train_image_paths = np.array(train_image_paths)
    val_image_paths = train_image_paths[-split_size:]
    train_image_paths = train_image_paths[:-split_size]

    print('Train set size : ', train_image_paths.shape)
    print('Val set size : ', val_image_paths.shape)
    print('Train and validation datasets ready !')
    return train_image_paths, val_image_paths
