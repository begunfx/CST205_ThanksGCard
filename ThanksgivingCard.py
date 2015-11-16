#CST205: Thanksgiving Day Card - Group Project
#Team: Startup Solutions Inc. SSI

#Brian Begun: Green Screen Border Leaves
#Wendy Gray: Repeating Background Pattern
#Christopher Dixon: Header Banner and Thanksgiving Greeting Text
#William Gillihan: Artify Center Photo

############## Wendy Gray ############################
# Repeating Background Pattern
# ver. 11/14/15
# 
# call backgroundPattern(pic) where pic is the picture
# for the pattern
######################################################
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
########### End Background Pattern Section ###########

###############William Gillihan#######################*
## these function calls are just for testing #########*
#pic = makePicture(pickAFile())#######################*
#target = makeEmptyPicture(700,500)###################*
######################################################*
# main function to scale, and artify picture, and then place in card
def addArtifyToCard(pic, target):
  scl = sclValue(pic, target)
  pic = sclDwn(pic, scl)
  pic = artify(pic)
  card = placeCenter(pic, target)
  return card
# get scale value
def sclValue(pic, target):
  pH = getHeight(pic)
  tH = getHeight(target)
  if pH > tH:
    sV = (pH / (tH/2))
  elif pH > (tH/2):
    sV = 2
  else:
    sV = 1
  return sV    
# place artify picture in center of target
def placeCenter(pic, target):
  targetX =(getWidth(target)/2) - (getWidth(pic)/2)
  targetY = (getHeight(target)/2) - (getHeight(pic)/2)
  for x in range (0, getWidth(pic)):
    for y in range (0, getHeight(pic)):
      px = getColor(getPixel(pic, x, y))
      setColor(getPixel(target, targetX+x, targetY+y), px)
  return target
# make a copy of a picture that is scaled down version of the original.
def sclDwn(pic, scl):
  sclPic = makeEmptyPicture((getWidth(pic)/scl), (getHeight(pic)/scl))
  if(scl % 2 == 0):
    adj = 0
  else:
    adj = 1
  for x in range (1, getWidth(pic)- adj, scl):
    for y in range (1, getHeight(pic)- adj, scl):
      color =  getColor(getPixel(pic, x, y))
      setColor(getPixel(sclPic, x/scl, y/scl), color)
  return sclPic
# artify picture
def artify(pic):
  #pic = makePicture(pickAFile())
  pixels = getPixels(pic)  
  for p in getPixels(pic):
    r = getRed(p)
    b = getBlue(p)
    g = getGreen(p)
    #change red, green, and blue values
    if (r < 64):
      r = 31
    elif (r > 63 and r < 128):
      r = 95    
    elif (r > 127 and r < 192):
      r = 159
    else: 
      r = 223
    if (b < 64):
      b = 31
    elif (b > 63 and b < 128):
      b = 95    
    elif (b > 127 and b < 192):
      b = 159
    else: 
      b = 223
    if (g < 64):
      g = 31
    elif (g > 63 and g < 128):
      g = 95    
    elif (g > 127 and g < 192):
      g = 159
    else: 
      g = 223
    setRed(p, r)    
    setGreen(p, g)
    setBlue(p, b) 
  return pic
########## usage example ###########*
#show(addArtifyToCard(pic, target))#*
####################################*



############## Brian Begun ###########################
# chromakey
# ver. 11/15/15
# 
# extract blue screen from our foreground image and
# composite it over the background
######################################################

#use the following: chromakey(255, 145, 700)
def chromakey(foreground, pic, refX, refY, threshold):
  
  background = pic
  #leaves = "images/LeavesBannerOverBlue_700x500.png"
  
  #file1 = pickAFile()
  #file2 = pickAFile()
  #foreground = makePicture(file1)
  #background = makePicture(file2)
  
  fWidth = getWidth(foreground)
  fHeight = getHeight(foreground)
  
  fRefPixel = getPixel(foreground, refX, refY)
  fRefColor = getColor(fRefPixel)
  
  for x in range(0, fWidth):
    for y in range(0, fHeight):
      fgPx = getPixel(foreground, x, y)
      bgPx = getPixel(background, x, y)
      
      fColor = getColor(fgPx)    
      fR = getRed(fgPx)
      fG = getGreen(fgPx)
      fB = getBlue(fgPx)
      
      bColor = getColor(bgPx)
      
      refDistance = distance(fRefColor, fColor)
      if fB > max(fG,fR) and refDistance < threshold:
        newColor = bColor
      else:
        newColor = fColor
      
      setColor(fgPx, newColor)
      
  #show(foreground)
  return(foreground)
  
  
############## Christopher Dixon #####################
# addGreeting
# ver. 11/15/15
# 
# 
# 
###################################################### 
  
def addGreeting(pic):
  cardWidth = 700  
  cardHeight = 500
  greeting = "Happy Thanksgiving"
  textShadowColor = makeColor(144, 71, 8)
  textColor = makeColor(255, 225, 8)
  textStyle = makeStyle(serif, italic + bold, 48)
  bannerColor = makeColor(232, 101, 5)
  addTextWithStyle(pic, 162, 52, greeting, textStyle, textShadowColor)
  addTextWithStyle(pic, 160, 50, greeting, textStyle, textColor)
  return pic
  

############## Christopher Dixon #####################
# makeBanner
# ver. 11/15/15
# 
# 
# 
###################################################### 
def makeBanner(pic):
  cardWidth = 700  
  cardHeight = 500
  bannerColor = makeColor(232, 101, 5) #used colord from background leaves
  addRectFilled(pic, 0, 0, cardWidth, int(cardHeight * 0.15), bannerColor)
  #show(pic)
  return pic 
# order as follows ----- LeavesBannerOverBlue_700x500 -- Artify Photo -- background Photo
card = addGreeting(makeBanner(chromakey(makePicture(pickAFile()), addArtifyToCard(makePicture(pickAFile()), backgroundPattern(makePicture(pickAFile()))), 255, 145, 700)))
show(card)
