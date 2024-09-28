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
    #new_im.show()
    new_im.save(out_name)

def odd_pic(p_name):
    im = Image.open(p_name)
    im = trim(im)
    w,h = im.size 
    top = 5
    while True:
        t = im.crop((0,top,w,h))
        print(t.size)
        if t.size[1] - trim(t).size[1] > 5:
            break
        top += 1
    print(top)

    right = 30
    while True:
        t = im.crop((0,top,w-right,h))
        if t.size[0]-trim(t).size[0] > 5:
            break
        right += 1
    print(right)
    
    im = im.crop((0,top,w-right,h))
    w,h = im.size
    m = w/2 + 20

    while True:
        t = im.crop((0,0,m,h))
        if t.size[0]-trim(t).size[0] > 4:
            break
        m -= 1
    print(m)
    print(im.size)
    
    im1 = im.crop((0,0,m,h))
    im2 = im.crop((m,0,w,h))
    #im2.show()
    pic_concat([im1,im2],"m-"+p_name)

def even_pic(p_name):
    im = Image.open(p_name)
    im = trim(im)
    w,h = im.size 
    top = 5
    while True:
        t = im.crop((0,top,w,h))
        if t.size[1] - trim(t).size[1] > 5:
            break
        top += 1
    print(top)
    left = 30
    while True:
        t = im.crop((left,0,w,h))
        if t.size[0]-trim(t).size[0] > 5:
            break
        left += 1
    print(left)
    
    im = im.crop((left,top,w,h))
    w,h = im.size
    m = w/2 - 10

    while True:
        print(m,w)
        t = im.crop((m,0,w,h))
        if t.size[0]-trim(t).size[0] > 4:
            break
        m += 1
    print(m)
    print(im.size)
    
    im1 = im.crop((0,0,m,h))
    im2 = im.crop((m,0,w,h))
    #pic_concat([im1,im2],"m-"+p_name)
#1657
def cut(i):
    p_name = "larousse-%04d.png"%i
    print("id=%d"%i)
    if i % 2 == 1:
        odd_pic(p_name)
    else:
        even_pic(p_name)

for i in range(10000,1657,2):
    if i in [68,470,740,846,892,1362]:
        continue
    cut(i)

for i in range(1655,1657,2):
    if i in [167,263,327,385,617,757,845,861,1261,1431,1447,1459,1479,1507,1527,1531,1535,1575,1591,1625,1629,1639,1655]:
        continue
    cut(i)  