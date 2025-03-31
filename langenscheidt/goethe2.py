#take picture x.png and split the words from Japanese dictionary.

import sys
import os
from PIL import Image, ImageChops
import glob


def trim(im):
    bg = Image.new(im.mode, im.size, (255,255,255))#im.getpixel((0,0)))
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

def concat(pics, out_name):
    if len(pics) == 0: 
        return
    images = [ x for x in pics]
    
    widths, heights = zip(*(i.size for i in images))
   
    max_width = max(widths)
    total_height = sum(heights)
   
    new_im = Image.new('RGB', (max_width, total_height + 6*len(pics)-6), color="white")
   
    y_offset = 0
    for im in images:
        new_im.paste(im, (max_width-im.size[0],y_offset))
        y_offset += im.size[1] #+ 1
        new_im.paste(Image.new('RGB', (max_width, 6), color="white"),(max_width,y_offset))
        y_offset += 6
    add_margin(new_im).save(out_name)
    #for pic in pics:
    #    os.system("rm %s"%pic)
    #add_margin(new_im).show()

def get_top(im,tp):
    (w,h) = im.size
    box = (0, 0, w, tp)
    cropped = im.crop(box)
    return cropped

def cut_left(im,lt):
    (w,h) = im.size
    box = (lt, 0, w, h)
    cropped = im.crop(box)
    return cropped

def cut_top(im,tp):
    (w,h) = im.size
    box = (0, tp, w, h)
    cropped = im.crop(box)
    return cropped

word = []
is_first = True
im = trim(Image.open("x-00001.png"))
W = im.size[0]
i = 1
j = 0
while True:
    if is_first:
        im = trim(cut_top(im,0))
        is_first = False
    else:
        im = trim(cut_top(im,i))

    if im is None or im.size[1] < 5:
        concat(word, "t-%04d.png"%j)
        j+=10
        break
    i = 1
    while (trim(cut_top(im,i)) is not None) and cut_top(im,i).size[1] == trim(cut_top(im,i)).size[1]:
        i += 1
    #print i
    #print "---",trim(get_top(im,i)).size[0]
    if i <= 50 and (W - trim(get_top(im,i)).size[0] <= 15 or (W - get_top(im,i).size[0] <= 5 and trim(cut_left(get_top(im,i),15)).size[0] +10 <= trim(get_top(im,i)).size[0])):
        #print "concat",len(word)
        concat(word, "t-%04d.png"%j)
        j+=10
        word = [get_top(im,i)]
    else:
        word.append(get_top(im,i))
