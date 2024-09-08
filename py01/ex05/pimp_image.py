import numpy as np
import matplotlib.pyplot as plt


def ft_invert(nd: np.ndarray):
    """
    Inverts the color of the image received.
    """
    output = 255 - nd
    plt.imshow(output)
    plt.axis('off')
    plt.show()


def ft_red(nd: np.ndarray):
    red_only = nd.copy()
    red_only[:,:,1] = 0
    red_only[:,:,2] = 0
    plt.imshow(red_only)
    plt.axis('off')
    plt.show()

def ft_green(nd: np.ndarray):
    green_only = nd.copy()
    green_only[:,:,0] = 0
    green_only[:,:,2] = 0
    plt.imshow(green_only)
    plt.axis('off')    
    plt.show()


def ft_blue(nd: np.ndarray):
    blue_only = nd.copy()
    blue_only[:,:,0] = 0
    blue_only[:,:,1] = 0
    plt.imshow(blue_only)
    plt.axis('off')
    plt.show()

def ft_grey(nd: np.ndarray):
    grey = nd.copy()
    grey = 0.2989 * nd[:, :, 0] + 0.5870 * nd[:, :, 1] + 0.1140 * nd[:, :, 2]
    grey_stacked = np.stack((grey, grey, grey), axis=-1)
    grey_stacked = grey_stacked / 255.0
    plt.imshow(grey_stacked)
    plt.axis('off')
    plt.show()