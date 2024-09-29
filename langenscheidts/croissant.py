import sys
import os
from PIL import Image, ImageChops
import glob


def trim(im):
    bg = Image.new(im.mode, im.size, (255, 255, 255))    
    diff = ImageChops.difference(im, bg)
    diff = ImageChops.add(diff, diff, 2.0, -30)
    #Bounding box given as a 4-tuple defining the left, upper, right, and lower pixel coordinates.
    #If the image is completely empty, this method returns None.
    bbox = diff.getbbox()
    if bbox:
        return im.crop(bbox)

def trim1(im):
    bg = Image.new(im.mode, im.size, (255, 255, 255))
    diff = ImageChops.difference(im, bg)
    diff = ImageChops.add(diff, diff, 2.0, -30)
    #Bounding box given as a 4-tuple defining the left, upper, right, and lower pixel coordinates.
    #If the image is completely empty, this method returns None.
    bbox = diff.getbbox()
    if bbox:
        return im.crop(bbox)

def add_margin(im):
    w,h = im.size
    new_im = Image.new('RGB', (w+100, h+100), color="white")
    new_im.paste(im, (50,50))
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

def cut_top(im):
    im = trim1(im)
    #im.show()
    w,h = im.size
    top = 5
    while True:
        t = im.crop((0,top,w,h))
        print(top)
        if t.size[1] - trim1(t).size[1] > 1:
            break
        top += 1
    print("top = ",top)
    im = im.crop((0,top,w,h))
    im = trim1(im)
    w,h = im.size
    im = im.crop((0,2,w,h))
    im = trim1(im)
    return im
def split(im):
    w,h = im.size
    m = w/2
    im1 = im.crop((0,0,m,h))
    im2 = im.crop((m,0,w,h))
    return (im1,im2)
def cut_right(im):
    im = trim1(im)
    right = 120
    w,h = im.size
    im.show()
    while True:
        t = im.crop((0,0,w-right,h))
        if t.size[0] - trim1(t).size[0] > 2:
            break
        right += 4
        print("right = ",right)
    print("right = ",right)
    im = trim1(im.crop((0,0,w-right,h)))
    im.show()
    return im

def cut_left(im):
    im = trim(im)
    left = 120
    w,h = im.size
    im.show()
    while True:
        t = im.crop((left,0,w,h))
        if t.size[0] - trim(t).size[0] > 2:
            break
        left += 4
        print("left = ",left)
    print("left = ",left)
    im = trim(im.crop((left,0,w,h)))
    im.show()
    return im

def cut(i):
    p_name = "langenschiedts-%03d.png"%i
    print("id=%d"%i)
    im = Image.open(p_name)
    if i % 2 == 1:
        im = cut_right(im)
    else:
        im = cut_left(im)
    im = cut_top(im)
    im = cut_top(im)
    im1,im2 = split(im)
    pic_concat([im1,im2],"m-"+p_name)
    return
#for i in range(2,30):
#    if i in [2,27]:
#        continue
#    cut(i)
cut(36)