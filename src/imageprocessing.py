# Include as many packages as you'd like here
import numpy as np
from PIL import Image
import skimage.transform
import cv2
import matplotlib.pyplot as plt

def load_image(path):
    """
    TODO: IMPLEMENT ME
    
    Loads the nortwestern image which is save at "images/northwestern.jpg"
    ps. the whole image should be divided by 255.

    Args:
        path()
    Returns:
        output (np.ndarray): The northwesten image as an RGB image
    """
    raise NotImplementedError

def crop_chicago_from_northwestern(img):
    """
    TODO: IMPLEMENT ME
    
    Crop a region-of-interest (ROI) from the big northwestern image that shows only Chicago
    
    The image size should be (250, 1000) and the the output should be an RGB numpy array
    
    Args:
        input (nd.array): The image of Northwestern and Chicago
    Returns:
        output (np.ndarray): The skyline of chicago with size (250,1000,3)
    """
    raise NotImplementedError
    

def rescale(img,scale):
    """
    TODO: IMPLEMENT ME
    
    rescales an image; look into cv2.resize!

    Args:
        img (np.array): the image you want to rescale
        scale(float): percent you want to scale
    Returns:
        resized(np.array): the resized image
    """
    raise NotImplementedError

def downsample_by_scale_factor(img,scale_factor):
    """
    TODO: IMPLEMENT ME
    
    Downsample the input image img by a scaling factor
    
    E.g. with scale_factor = 2 and img.shape = (200,400)
    
    you would expect the output to be (100,200)
    
    Args:
        input (nd.array): The image of Northwestern and Chicago
    Returns:
        output (np.ndarray): The skyline of chicago with size (250,1000,3)
    """
    raise NotImplementedError



def convert_rgb2gray(rgb):
    """
    TODO: IMPLEMENT ME
    
    rgb2gray converts RGB values to grayscale values by forming a weighted
    sum of the R, G, and B components:

    0.2989 * R + 0.5870 * G + 0.1140 * B 
    
    
    These values come from the BT.601 standard for use in colour video encoding,
    where they are used to compute luminance from an RGB-signal.
    
    Find more information here:
    https://www.itu.int/dms_pubrec/itu-r/rec/bt/R-REC-BT.601-7-201103-I!!PDF-E.pdf

    Args:
        input (nd.array): 3-dimensional RGB where third dimension is ordered as RGB
    Returns:
        output (np.ndarray): Gray scale image of RGB weighted by weighting function from above
    """
    raise NotImplementedError

def plot_chicago_skyline(img):
    """
    TODO: IMPLEMENT ME
    
    This is a simple exercise to learn how to use subplot.
    
    Goal of is to show a 2x2 subplot that shows the Chicagskyline for 
    4 different downsampling factors: 1,2,4,8
    
    Use plt.subplot to create subfigures
    
    You should give a title of the compelte image (use plt.suptitle)
    and each subfigure should have a corresponding title as well.

    Args:
        input (nd.array): 2-dimensional gray scale image
    Returns:
        
    """
    raise NotImplementedError






def pad_image(img,pad_size):
    """

    TODO: IMPLEMENT ME

    this gives the image some padding.
    
    Args:
        img (np.ndarray): the image to be padded
        pad_size (int): the amount of pixels to pad
    Returns:
        padded_img (np.ndarray): the padded image
    """
    raise NotImplementedError

def add_alpha_channel(img):
    """

    TODO: IMPLEMENT ME

    this adds an additional channel, an alpha channel, which are all 1s.

    Args:
        img (np.ndarray): image with 3 channels
    output:
        img (np.ndarray): the image with an additional alpha channel
    """
    raise NotImplementedError

def overlay_two_images_of_same_size(img1,img2):
    """

    TODO: IMPLEMENT ME

    this function overlays two images by using the alpha channels of the two images.

    an approach for this function:
        make a mask using the alpha channel of the foreground

        because the background alpha values are 1s, use that with the fact that the foreground
        image contains the outline of the object to change img1 and img2, and use the addition
        of these two images as the overlay.

    Args:
        img1 (np.ndarray): this should be the background
        img2 (np.ndarray): this should be the foreground/object 
    """
    raise NotImplementedError

def overlay_two_images(img1,img2,location):
    """

    TODO: IMPLEMENT ME

    this function should overlay these two images at the location signified. don't forget
    to use the helper overlay_two_images_of_same_size. The process should look something like:
        
        taking a section of the background that you want from using location

        use that image with the foreground image with the overlay_two_images_of_same_size function
        to overlay, let's call this overlayed_img

        make that section of the background = overlayed_img

    Args:
        img1 (nd.array): this image should be the background
        img2 (nd.array): this image should be the foreground
        location (nd.array): x,y coordinates of the top-left of the image you want to overlay
    Returns:
        output (np.ndarray): The overlayed image
    """    
    raise NotImplementedError


    