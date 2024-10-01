import sys
import os
from PIL import Image, ImageChops
import glob

debug = False

def cp(i):
    cmd = "cp langenscheidt-%04d.png m-langenscheidt-%04d.png"%(i,i)
    os.system(cmd)
def mv(i):
    cmd = "mv m-langenscheidt-%04d.png DONE"%(i)
    os.system(cmd)

def trim(im):
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
    if debug:
        new_im.show()
    new_im.save(out_name)

def cut_top(start, opti, im):
    im = trim(im)
    #im.show()
    w,h = im.size
    top = start
    while True:
        t = im.crop((0,top,w,h))
        if t.size[1] - trim(t).size[1] > 1:
            break
        top += 1
    if top == 1:
        print("top = 1!")
    else:
        print("top = ",top)
    im = im.crop((0,top,w,h))
    im = trim(im)
    w,h = im.size
    if opti:
        im = im.crop((0,2,w,h))
        im = trim(im)
    return im

def split(im, m_off = 0):
    w,h = im.size
    m = w/2  + m_off
    im1 = im.crop((0,0,m,h))
    im2 = im.crop((m,0,w,h))
    return (im1,im2)

def cut_right(im):
    im = trim(im)
    right = 20
    w,h = im.size
    #im.show()
    while right < 100:
        t = im.crop((0,0,w-right,h))
        if t.size[0] - trim(t).size[0] > 1:
            break
        right += 1
        #print(right)
    right = 37
    right += 1
    print("right = ",right)
    if right == 100:
        exit()
    im = trim(im.crop((0,0,w-right,h)))
    #im.show()
    return im

def cut_left(im):
    im = trim(im)
    left = 20
    w,h = im.size
    #im.show()
    while True:
        t = im.crop((left,0,w,h))
        if t.size[0] - trim(t).size[0] > 1:
            break
        left += 1
    left += 1
    print("left = ",left)
    im = trim(im.crop((left,0,w,h)))
    #im.show()
    return im

def cut(i, m_off = 0):
    p_name = "langenscheidt-%04d.png"%i
    print("id=%d"%i)
    im = Image.open(p_name)
    if debug:
        im.show()
    if i % 2 == 1:
        im = cut_right(im)
    else:
        im = cut_left(im)
    im = cut_top(1, True, im)
    # initial run must not
    #im = cut_top(18, False, im)
    im1,im2 = split(im, m_off)
    pic_concat([im1,im2],"m-"+p_name)
    return
for i in range(1301, 1351):
    #break
    cut(i)


#cut()
#cut()
#cut()
#cut()
#cut()
#cp()
#cp()

