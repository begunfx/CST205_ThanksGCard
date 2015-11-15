import math  #import math module for ceiling function

# function backgroundPattern
def backgroundPattern(pic):    #takes given pic, scales down, quad mirrors, 
                            #and patterns over card size
  cardWidth = 700   #card size currently hardcoded
  cardHeight = 500
  ultPicWidth = 75  #scaled pic size currently hardcoded
  
  background = makeEmptyPicture(cardWidth, cardHeight)
  pic = sizeBGpic(pic, ultPicWidth) #resize pic
  ultPicHeight = getHeight(pic)
  pattern = quadMirror(pic)         #quad mirror pic
  xPic = 0                        #to loop through pic width
  for x in range(0, cardWidth):   #loop through background
    yPic = 0                      #to loop through pic height
    for y in range(0, cardHeight):#loop through background
      color = getColor(getPixel(pic, xPic, yPic))
      setColor(getPixel(background, x, y), color)
      yPic = yPic + 1           #loop through pic height, 
      if yPic == ultPicHeight:  #reset if at end
        yPic = 0
    xPic = xPic + 1             #loop through pic width,
    if xPic == ultPicWidth:     #reset if at end
      xPic = 0
  #show(background)
  return background     #return background

# function sizeBGpic
def sizeBGpic(pic, ultPicWidth):  #scale given pic to given width
  picWidth = getWidth(pic)
  picHeight = getHeight(pic)
  if ultPicWidth > picWidth:  #if desired width is larger than original,
    return(pic)               #return original pic
  scaleNum = int(math.ceil(picWidth/ultPicWidth))  #number to scale down by
  newHeight = int(math.ceil(picHeight/scaleNum))   #new height
  newPic = makeEmptyPicture(ultPicWidth, newHeight)
  for x in range(0, ultPicWidth):
    for y in range(0, newHeight):
      color = getColor(getPixel(pic, x*scaleNum, y*scaleNum))
      setColor(getPixel(newPic, x, y), color)
  return(newPic)               #return new pic

# function verticalMirror
def verticalMirror(pic):  #mirror left side of given pic to right
  width = getWidth(pic)
  height = getHeight(pic)
  for x in range(0, width/2):
    for y in range (0, height):
      px = getPixel(pic, x, y)
      px2 = getPixel(pic, width-1- x, y)
      color = getColor(px)
      setColor(px2, color)
  return pic
  
# function horizTopMirror
def horizTopMirror(pic):  #mirror top part of given pic to bottom
  width = getWidth(pic)
  height = getHeight(pic)
  for x in range(0, width):
    for y in range(0, height/2):  #for every pixel on top half, copy 
      px = getPixel(pic, x, y)    #to respective pixel on bottom
      px2 = getPixel(pic, x, height-1-y)
      color = getColor(px)
      setColor(px2, color)
  return pic
  
# function quadMirror
def quadMirror(pic):  #mirror top left quadrant to right, then top half to bottom
  pic = verticalMirror(pic)
  pic = horizTopMirror(pic)
  return pic
