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