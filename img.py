from PIL import Image
import numpy as np


def load_array_from_image(filename):
    print('Loading array from: ', filename)
    img = Image.open(filename, 'r')
    a_img = np.array(img) / 255  # normalize RGB int out of 255
    xs = a_img.shape[1]  # columns
    ys = a_img.shape[0]  # rows
    out_arr_shape = (a_img.shape[0], a_img.shape[1])  # removes RGB tuple
    out_arr = np.zeros(out_arr_shape, dtype='float')
    for y in range(ys):
        for x in range(xs):
            # all channels are the same, so
            out_arr[x, y] = np.linalg.norm(a_img[x, y])
    return out_arr


# load_array_from_image(FILE_PATH)
