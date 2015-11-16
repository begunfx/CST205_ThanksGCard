def makeBanner(pic):
  cardWidth = 700  
  cardHeight = 500
  bannerColor = makeColor(232, 101, 5) #used colord from background leaves
  addRectFilled(pic, 0, 0, cardWidth, int(cardHeight * 0.15), bannerColor)
  show(pic)
  return pic