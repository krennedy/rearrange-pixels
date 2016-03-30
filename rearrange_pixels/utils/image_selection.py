""" This module contains some utility functions which are
"""

import Image

from random import shuffle


def check_sizes_equal(im_path_1, im_path_2):
    """ Check sizes equal. Return True if so, False if not.
    If problem opening the images, return False and say so
    """
    try:
        im_1 = Image.open(im_path_1)
        im_2 = Image.open(im_path_2)
        area_1 = im_1.size[0] * im_1.size[1]
        area_2 = im_2.size[0] * im_2.size[1]
        sizes_equal = area_1 == area_2
        return sizes_equal

    except IOError:
        print 'Problems opening file - were these even images?'
        return False


def select_random_image_pair():
    """ These are all just hardcoded from a known set.
    Pick a random set.
    """
    bank_path = 'image_bank'

    # all the images below are 500 X 353 pixels
    im_list = ['beaux.jpg', 'vangogh.jpg', 'gauguin.jpg', 'seurat.jpg']
    shuffle(im_list)
    two_random_ims = im_list[:2]
    imfile_1, imfile_2 = ['/'.join([bank_path, im]) for im in two_random_ims]
    return imfile_1, imfile_2



