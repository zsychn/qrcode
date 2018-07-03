#-*- coding: UTF-8 -*-
import os,sys
import PIL
import numpy as np
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

def downLoadPto(csvDir, fileDir):
    #读取文件夹名称
    if os.path.exists(csvDir):
        rows = open(csvDir,'rU')
        for row in rows:
            row =  row.replace("\n", '')
            url =  'http://qr.liantu.com/api.php?&w=200&text=' + row + ""
            # http://qr.liantu.com/api.php?&w=200&text=0006841277 -O test2.png
            # http://qr.liantu.com/api.php\?\&w\=200\&text\=0006841277 -O test.png
            #url =  """ "http://tool.oschina.net/action/qrcode/generate?data='"""+row+"""'&output=image%2Fpng&error=L&type=0&margin=0&size=4'}" """
            com = 'wget '+url+' -O '+fileDir+'/'+row+".png"
            os.popen(com)
    else:
        print '文件不存在'
    #批量下载

def draw(text, formFile, toFile):
    width = 200
    height = 200
    image = Image.new("RGBA",(width,height),(255,255,255))
    #创建绘制对象
    draw = ImageDraw.Draw(image)
    #复制二维码
    loc = (0, -10)
    fromImge = Image.open(formFile)
    image.paste(fromImge, loc)
    #绘制字体
    length = len(text)*14
    tWidth = (width-length)/2
    theight = 175
    font = ImageFont.truetype("/System/Library/Fonts/Apple Symbols.ttf", 30)
    draw.text((tWidth, theight), text, (0,0,0), font)
    image.save(toFile)


def createPto(fileDir, resDir):
    names = []
    for root, dirs, files in os.walk(fileDir):
        for file in files:
            if os.path.splitext(file)[1] == '.png':
                name = os.path.splitext(file)[0]
                formFile = fileDir+'/'+file
                toFile = resDir+'/'+file
                draw(name, formFile, toFile)
                print file+'已完成'

#-----start-----
fileDir = './data'
resDir = './res'
csvDir = './csv/nums.csv'
print "-----start-----"
downLoadPto(csvDir, fileDir)
# createPto(fileDir, resDir)
print "-----end-----"
