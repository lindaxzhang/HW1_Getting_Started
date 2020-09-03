# Implementation of a simple gradient descent algorithm
def gd(alpha,x,y,PSF,max_it):
    for iter in range(0,max_it):
        cur_grad = alpha*grad_f(x,y,PSF)
        x = x - cur_grad

        fig,(ax1, ax2) = plt.subplots(ncols=2,figsize=(12,6))

        img1 = ax1.imshow(x,cmap='gray')
        ax1.set_title('Reconstruction Nr. ' + str(iter))
        colorbar(img1)

        img2 = ax2.imshow(cur_grad,cmap='gray')
        ax2.set_title('Gradient')
        colorbar(img2)

        plt.show()
    return x


# Implementation of the gradient of the data term
def grad_f(x,y,PSF):
    # Calculate Ax
    Ax = ndimage.convolve(x,PSF,mode='reflect')
    # Calculate A'(y) (Adjoint operator is correlation ==> See wikipedia)
    grad_f_x = ndimage.correlate(Ax - y,PSF,mode='reflect')
    return grad_f_x