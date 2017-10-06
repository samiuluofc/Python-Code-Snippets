# Working with all image maniplation functions from simple graphics
# and Creating Mirror image of the given gif image. 

from SimpleGraphics import *


# This function will take an image object as parameter, return another
# image which is actually the mirror version of the given image. 
def mirror_image(img):
    
    h = getHeight(img);
    w = getWidth(img);

    # Remember: Image coordinate starts from (0,0) ends at (w-1,h-1).
    xleft = 0
    xright = w-1
    res_img = createImage(w, h)
    
    while(xleft <= xright):
        for y in range(0,h,1):

            r,g,b = getPixel(img, xleft, y)
            putPixel(res_img, xright, y, r, g, b)
            r,g,b = getPixel(img, xright, y)
            putPixel(res_img, xleft, y, r, g, b)
            
        xleft = xleft + 1
        xright = xright - 1
        
    return res_img

def main():
    # For simplicity, keep the image file (.gif) into the same directory having
    # the current python file (.py).
    image_name = input("Enter the name of the image :")
    img_obj = loadImage(image_name)

    h = getHeight(img_obj)
    w = getWidth(img_obj)
    resize(w*2,h);
    drawImage(img_obj,1,1)

    result = mirror_image(img_obj)
    drawImage(result,w+1,1)

main()



