# -*- coding: utf-8 -*-

import argparse
import os
from PIL import Image
import numpy as np


def get_list_files(base_path):
    only_files = [os.path.join(base_path, f) for f in os.listdir(base_path) if os.path.isfile(os.path.join(base_path, f))]

    return only_files


def load_photo(path, weight, length):
    try:
        photo_image_obj = Image.open(path)
        photo_resize = photo_image_obj.resize((weight, length), Image.ANTIALIAS)
    except Exception as e:
        raise e
    return photo_resize


def image_to_np(src_image):
    return np.asarray(src_image, dtype="int32")


class Photo(object):

    def __init__(self, full_path):
        self.full_path = full_path
        self.file_name = os.path.basename(full_path)

        self.width = 1000
        self.length = 1000
        self.image_obj = load_photo(full_path, self.width, self.length)
        self.np_obj = image_to_np(self.image_obj)


class PhotosManipulator(object):

    def __init__(self, base_path):

        self.photos = []
        self.load_photos(base_path)

    def load_photos(self, base_path):
        photos_paths = get_list_files(base_path)
        for photo_path in photos_paths:
            self.photos.append(Photo(photo_path))

    def find_duplicate_photos(self):

        for first_index in range(len(self.photos)):
            for second_index in range(first_index+1, len(self.photos)):
                duplicate_photo = (self.photos[first_index].np_obj == self.photos[second_index].np_obj).all()
                if duplicate_photo:
                    print(self.photos[first_index].file_name, self.photos[second_index].file_name)


def main():

    parser = argparse.ArgumentParser(description='ML_SCHOOL_TASK - Machine Learning Summer School Test Task.')
    parser.add_argument('-p', '--path ', dest='path', required=True, help='Base path to input set photos.')
    args = parser.parse_args()

    f_manipulator = PhotosManipulator(args.path)
    f_manipulator.find_duplicate_photos()


if __name__ == "__main__":
    main()
