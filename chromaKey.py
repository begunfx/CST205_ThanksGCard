
############## Brian Begun ###########################
# chromakey
# ver. 11/15/15
# 
# extract blue screen from our foreground image and
# composite it over the background
######################################################

#use the following: chromakey(255, 145, 700)
def chromakey(refX, refY, threshold):
  
  #foreground = pic
  #leaves = "images/LeavesBannerOverBlue_700x500.png"
  
  file1 = pickAFile()
  file2 = pickAFile()
  foreground = makePicture(file1)
  background = makePicture(file2)
  
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
      
  show(foreground)
  return(foreground)