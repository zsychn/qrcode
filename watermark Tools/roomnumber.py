#-*- coding: UTF-8 -*-
import os,sys
import PIL
import numpy as np
import urllib
import re
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
    width =  330 #背景宽度 
    height = 210 #背景高度
    image = Image.new("RGBA",(width,height),(255,255,255))
    #创建绘制对象
    draw = ImageDraw.Draw(image)

    fontSize = 120 #字号大小
    font = ImageFont.truetype("/System/Library/Fonts/SFCompactDisplay-Heavy.otf", fontSize)
    w, h = font.getsize(text)
    draw.text(((width-w)/2, (height-h-36)/2), text, (0,0,0), font)
    image.save(toFile)

#-----start-----
fileDir = './csv'
resDir = './res'
csvDir = './csv/nums.csv'
print "-----start-----"
getData(csvDir, resDir)
print "-----end-----"
