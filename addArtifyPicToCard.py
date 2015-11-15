###############WilliamGillihan#######################*
# these function calls are just for testing #########*
pic = makePicture(pickAFile())#######################*
target = makeEmptyPicture(700,500)###################*
#####################################################*
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
######### usage example ###########*
show(addArtifyToCard(pic, target))#*
###################################*
