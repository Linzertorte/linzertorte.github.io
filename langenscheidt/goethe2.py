#take picture x.png and split the words from Japanese dictionary.

import sys
import os
from PIL import Image, ImageChops
import glob

name_prefix = "JP-"

start = 709

cat = []
#cat.append((708,2))


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

def pic_concat(pics, out_name):
    images = [trim(Image.open(x)) for x in pics]
    
    widths, heights = zip(*(i.size for i in images))
   
    max_width = max(widths)
    total_height = sum(heights)
   
    new_im = Image.new('RGB', (max_width, total_height), color="white")
   
    y_offset = 0
    for im in images:
        new_im.paste(im, (max_width-im.size[0],y_offset))
        y_offset += im.size[1]
    add_margin(new_im).save(out_name)
    for pic in pics:
        os.system("rm %s"%pic)

def main():
    pics = sorted(glob.glob("*.png"))
    i,j = 0, 0
    cnt = start
    while i < len(pics):
        if j < len(cat) and cnt == cat[j][0]:
            #cat
            cat_pics = []
            for k in range(cat[j][1]):
                os.system('mv "%s" %s%05d-%d.png'%(pics[i],name_prefix, cnt, k))
                cat_pics.append("%s%05d-%d.png"%(name_prefix,cnt,k))
                i += 1
            pic_concat(cat_pics,"%s%05d.png"%(name_prefix,cnt))
            j += 1
            cnt += 1
        else:
            add_margin(trim(Image.open(pics[i]))).save("%s%05d.png"%(name_prefix,cnt))
            os.system('rm "%s"'%pics[i])
            i += 1
            cnt += 1

#main()

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
    add_margin(new_im).show()

def get_top(im,tp):
    (w,h) = im.size
    box = (0, 0, w, tp)
    cropped = im.crop(box)
    return cropped

def cut_top(im,tp):
    (w,h) = im.size
    box = (0, tp, w, h)
    cropped = im.crop(box)
    return cropped

word = []
is_first = True
im = trim(Image.open("x.png"))
W = im.size[0]
i = 1
j = 1
while True:
    if is_first:
        im = trim(cut_top(im,0))
        is_first = False
    else:
        im = trim(cut_top(im,i))

    if im is None or im.size[1] < 5:
        concat(word, "tmp-%03d.png"%j)
        j+=1
        break
    i = 1
    while (trim(cut_top(im,i)) is not None) and cut_top(im,i).size[1] == trim(cut_top(im,i)).size[1]:
        i += 1
    #print i
    #print "---",trim(get_top(im,i)).size[0]
    if W - trim(get_top(im,i)).size[0] <= 10:
        #print "concat",len(word)
        concat(word, "tmp-%03d.png"%j)
        j+=1
        word = [get_top(im,i)]
    else:
        word.append(get_top(im,i))
