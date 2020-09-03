import numpy as np
import scipy

def create_radial_distance_map(N_img):
    """

    TODO: IMPLEMENT ME

    create disk-like filter footprint with given radius

    Args:
        N_img (int): how big the image should be
    Returns:
        Radial_distance_map (np.ndarray): the disk-like filter, with given radius.
    """
    raise NotImplementedError

def gaussian_psf(R,sigma):
    """
    TODO: IMPLEMENT ME
    
    finds the point spread function by calculating a convolutional
    kernel which is guassian. This gives us the blur.

    read more at:
    https://en.wikipedia.org/wiki/Point_spread_function

    Args:
        R (np.ndarray): the radial map, which is a meshgrid
        sigma (float): the blur radius
    Returns:
        psf_gauss (np.ndarray): the PSF
    """
    raise NotImplementedError


    

def calc_angle_of_view(sensor_size_mm,focal_length):
    """
    TODO: IMPLEMENT ME

    Calcualte Angle of View
    
    According to: https://shuttermuse.com/calculate-field-of-view-camera-lens/

    Args:
        sensor_size_mm (float): sensor size of camera
        focal_length (float): focal length of camera
    Returns:
        angle of view of specific camera
    """
    raise NotImplementedError

def calc_field_of_view(sensor_size_mm,o_obj,focal_length):
    """
    TODO: IMPLEMENT ME

    Calcualte linear field of view at specific distance away from the lens
    
    You have to transform the equation given in https://en.wikipedia.org/wiki/Magnification#Photography

    Args:
        sensor_size_mm (float): sensor size of camera
        o_obj (float): distance where object is located
        focal_length (float): focal length of objetive lens
    Returns:
        angle of view of specific camera
    """
    raise NotImplementedError


def calc_blur_radius(f,D,o_foc,o_obj):
    """

    TODO: IMPLEMENT ME

    Calcualte the blur radius according to
    lecture 1 - image formation

    Args:
        f (float): the focal length
        D (float): apeture diameter
        o_foc (float): focus distance 
        o_obj  (float)= distance of object
    Returns:
        blur_radius (float): blur radius
    """
    raise NotImplementedError

def crop_background_image_sensor_ratio(sensor_size_mm,img):
    """"

    TODO: IMPLEMENT ME
    
    This functions crops an image of arbitrary to size to a specific aspect ratio defined 
    by the sensor size of the camera
    
    This might come in handy    
    https://stackoverflow.com/questions/273946/how-do-i-resize-an-image-using-pil-and-maintain-its-aspect-ratio/273962
    
    Input:
        sensor_size (float) : array containing the height and width of the image sensor which defines the aspect ratio
        img (int,float) : the image that should be cropped to the specific aspect ratio
    Output:
        resized_img (int,loat): The cropped image that now has the correct aspect ratio
    """

    raise NotImplementedError

def convolve_image(img,PSF):
    """

    TODO: IMPLEMENT ME
    this applies a convolution utilizing the guassian psf on the image

    Args:
        img (np.ndarray): the image to apply the PSF on
        PSF (np.ndarray): the PSF
    Returns:
        filtered_img (np.ndarray): the blurred image after the PSF has been applied.
    """
    raise NotImplementedError

