import sys
import os
from PIL import Image, ImageChops
import glob


def trim(im):
    bg = Image.new(im.mode, im.size, im.getpixel((0,0)))
    diff = ImageChops.difference(im, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    #Bounding box given as a 4-tuple defining the left, upper, right, and lower pixel coordinates.
    #If the image is completely empty, this method returns None.
    bbox = diff.getbbox()
    if bbox:
        return im.crop(bbox)

def add_margin(im):
    w,h = im.size
    new_im = Image.new('RGB', (w+40, h+40), color="white")
    new_im.paste(im, (20,20))
    return new_im

# list of pics names
def pic_concat(pics, out_name):
    images = [trim(x) for x in pics]
    
    widths, heights = zip(*(i.size for i in images))
   
    max_width = max(widths)
    total_height = sum(heights)
   
    new_im = Image.new('RGB', (max_width, total_height), color="white")
   
    y_offset = 0
    for im in images:
        new_im.paste(im, (max_width-im.size[0],y_offset))
        y_offset += im.size[1]
    new_im = add_margin(new_im)
    new_im.show()
    new_im.save(out_name)

def odd_pic(p_name):
    im = Image.open(p_name)
    w,h = im.size 
    top = 60
    top = 77

    right = 53
    right = 66

    m = (w-right)/2 + w/70 + 10
    #m = (w-right)/2 + w/70 + 14

    print(im.size)
    
    im1 = im.crop((0,top,m,h))
    im2 = im.crop((m,top,w-right,h))
    pic_concat([im1,im2],"m-"+p_name)

def even_pic(p_name):
    im = Image.open(p_name)
    w,h = im.size 
    top = 60
    #top = 68

    left = 55
    left = 75
    
    m = (w-left) / 2 + left - w/70
    #m = (w-left) / 2 + left - w/70 - 8
    print(im.size)
    
    im1 = im.crop((left,top,m,h))
    im2 = im.crop((m,top,w,h))
    pic_concat([im1,im2],"m-"+p_name)
#1657
def cut(i):
    p_name = "larousse-%04d.png"%i
    print(i)
    if i % 2 == 1:
        odd_pic(p_name)
    else:
        even_pic(p_name)

cut(220)
