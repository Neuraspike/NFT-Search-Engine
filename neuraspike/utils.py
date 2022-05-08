# import the necessary library
import os

def load_images_from_folder(folder):
    # load all the images within a folder into memory
    image_list = []
    for filename in os.listdir(folder):
        path = os.path.join(folder, filename)
        image_list.append(path)

    return image_list


def extract_filename(path):
    # extract the filename from an absolute path
    return os.path.basename(path)
