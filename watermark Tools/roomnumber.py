#-*- coding: UTF-8 -*-
import os,sys
import PIL
import numpy as np
import urllib
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

def getData(csvDir, resDir):
    #读取文件夹名称
    if os.path.exists(csvDir):
        rows = open(csvDir,'rU')
        for row in rows:
            row =  row.replace("\n", '')
            draw(row, resDir+'/'+row+'.png')
            print row + '.png---创建成功'
    else:
        print '文件不存在'
#批量下载

def draw(text, toFile):
    width =  360
    height = 240
    image = Image.new("RGBA",(width,height),(255,255,255))
    #创建绘制对象
    draw = ImageDraw.Draw(image)
    length = len(text)*70 + (len(text)-1)*15
    print length
    tWidth = (width-length)/2+5
    theight = height/2-75
    font = ImageFont.truetype("/System/Library/Fonts/SFCompactDisplay-Heavy.otf", 130)
    draw.text((tWidth, theight), text, (0,0,0), font)
    image.save(toFile)


#-----start-----
fileDir = './csv'
resDir = './res'
csvDir = './csv/nums.csv'
print "-----start-----"
getData(csvDir, resDir)
print "-----end-----"
