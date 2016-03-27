import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

#
# Or get average color of image, and map distance to that color?
# Identify bottlenecks
# Convert whole thing to enhanced dataframe object?
# Handle different sized inputs

fig = plt.figure(figsize=(14,10))
ax1 = fig.add_subplot(221)
ax3 = fig.add_subplot(223)

class Animator():


    def __init__(self):
        # im1 : the imshow at ax1
        # rgb1: the pixel map displayed in im1
        pass

    def load(self, pix_1, pix_2):
        """ Wow, we need a docstring!
        """
        self.rgb_1 = convert_to_imshow_format(pix_1.RGB, pix_1.shape)
        #self.rgb_2 = convert_to_imshow_format(pix_2)

        # Initalize new canvasses as all white, in the shape of targets
        #self.rgb_B_new = np.ones(self.rgb_B.shape).astype('uint8') * 255
        #self.rgb_A_new = np.ones(self.rgb_A.shape).astype('uint8') * 255

        # Initialize
        kwargs = dict(animated=True, interpolation='none')
        self.im1 = ax1.imshow(self.rgb_1, **kwargs)
        #self.im3 = ax3.imshow(self.rgb_B_new, **kwargs)

        #nsteps = 10
        #self.npix = self.rgb_A.shape[0] * self.rgb_A.shape[1]
        #self.nstep = int(self.npix/float(nsteps))

    def draw(self,):
        #ani = animation.FuncAnimation(
        #    fig, self.updatefig,
        #    np.arange(0, self.npix, self.nstep),
        #    interval=100, blit=False, repeat=False)
        plt.show()

    def updatefig(self, j):
        """ Update att 4
        """
        new_1 = take_out(self.rgb_A, j, self.nstep)
        #new_2 = take_out(self.rgb_B, j, self.nstep)
        #new_3 = put_in(self.rgb_B_new, self.rgb_A,
        #               self.df_A_sorted, j)
        #new_4 = put_in(self.rgb_A_new, self.rgb_B_original,
        #               self.df_B_sorted, j)
        self.im1.set_array(new_1)
        #self.im2.set_array(new_2)
        #self.im3.set_array(new_3)
        #self.im4.set_array(new_4)

        # return top row to original state if at end of animation
        #if j+self.nstep >= len(self.df_A_sorted):
        #    self.im1.set_array(self.rgb_A_original)
        #    self.im2.set_array(self.rgb_B_original)


def take_out(img, i, nstep):
    """ Add docstring
    """
    img_shape = img.shape
    img = img.reshape(img_shape[0]* img_shape[1], img_shape[2])
    img[i:i+nstep] = np.array([155,155,155]).astype('uint8')
    img = img.reshape(img_shape)
    return img


def put_in(img_put, img_pull, x_new, y_new, i):
    """ Here, you want to put in a few pixels of new image
    But using the values input from another image
    FIXME: !!! img_pull shouldnt need to have to be flattened each time
    """
    img_shape = img_put.shape
    new_shape = (img_shape[0]* img_shape[1], img_shape[2])

    img_put = img_put.reshape(new_shape)
    img_pull = img_pull.reshape(new_shape)

    #x_new = df_sorted.x_new
    #y_new = df_sorted.y_new
    x_dim = x_new.max() + 1

    positions = y_new * x_dim + x_new  # or reverse x's and y's
    positions_this_time = positions[i:i+self.nstep]

    img_put[positions_this_time] = img_pull[i:i+self.nstep]

    img_put = img_put.reshape(img_shape)
    return img_put


def sort_rgb_into_new_order(rgb, x, y):
    """ We are given an rgb array of pixels, and the xy-coord they are to be at.
    From this, reorder rgb so it can be displayed
    """
    idx_sort = np.lexsort((y, x))
    rgb_sorted = rgb[idx_sort]
    return rgb_sorted


def convert_to_imshow_format(rgb, image_shape):
    """ PM what it says. Takes almost no time!
    rgb is pixel LIST in format XXX.
    Reshape to XXX and convert to unsigned 8-bit integers.
    """
    xdim, ydim = image_shape
    rgb_display = rgb.reshape((ydim, xdim, 3))
    rgb_display = rgb_display.astype(np.uint8)
    return rgb_display



