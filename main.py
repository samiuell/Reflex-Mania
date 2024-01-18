from tkinter import *
from math import *
import math
from time import *
from random import *

root = Tk()
screen = Canvas(root, width=800, height=800, background= "white")



#Sets initial values 
def setInitialValues(): 
  
  global xLeft, yLeft, xUp, yUp, xDown, yDown, xRight, yRight, cScore, score, combo, heart, lives, cHeart, yLeftFall, yUpFall, yDownFall, yRightFall, yLeftSpeed, yUpSpeed, yDownSpeed, yRightSpeed, mode, triviaChances, triviaBack, gameOverBack, highestCombo, firstBack, secondBack, changeBack, thirdBack, fourthBack

  #Arrows 
  xLeft = 100 
  yLeft = 650
  xUp = 300
  yUp = 600 
  xDown = 450
  yDown = 700
  xRight = 650 
  yRight = 650


  #Falling arrows 
  yLeftFall = 40
  yUpFall = -150
  yDownFall = -250
  yRightFall = -90
    
  if mode == "Normal":
    yLeftSpeed = 1.5
    yUpSpeed = 1.5
    yDownSpeed = 1.5
    yRightSpeed = 1.5

  if mode == "Hard": 
    yLeftSpeed = 2
    yUpSpeed = 2
    yDownSpeed = 2
    yRightSpeed = 2

  if mode == "Extreme": 
    yLeftSpeed = 2.5
    yUpSpeed = 2.5 
    yDownSpeed = 2.5
    yRightSpeed = 2.5


  #Score / combo
  cScore = 725
  score = 0 
  combo = 0 
  highestCombo = 0 


  #Lives
  lives = 6
  cHeart = 675 
  triviaChances = 0 


  #Uploads 
  heart = PhotoImage(file="heart.gif")
  triviaBack = PhotoImage(file = "trivBox.gif" )
  gameOverBack = PhotoImage(file = "gameOverBackdrop.gif")
  firstBack = PhotoImage(file = "first.gif")
  secondBack = PhotoImage(file = "second.gif")
  thirdBack = PhotoImage(file = "third.gif")
  fourthBack = PhotoImage(file = "fourth.gif")

  changeBack = 0 



#Creates Background Depending on how Many Points the Player has 
def createBackground():
  global xLeft, yLeft, xUp, yUp, xDown, yDown, xRight, yRight, firstBack, secondBack, changeBack, firstDrop, secondDrop, thirdBack, thirdDrop, fourthDrop

  if score < 4000: 

    firstDrop = screen.create_image(400, 400, image = firstBack)

  elif 4000 < score < 8000: 

    secondDrop = screen.create_image(400, 400, image = secondBack)

  elif 8000 < score < 12000: 

    thirdDrop = screen.create_image(400, 400, image = thirdBack)

  elif score > 12000: 

    fourthDrop = screen.create_image(400, 400, image = fourthBack)

  changeBack = changeBack + 1
  
  
  #Arrows 
  left = screen.create_polygon(xLeft, yLeft, xLeft+30, yLeft-30, xLeft+30, yLeft-15, xLeft+100, yLeft-15, xLeft+100, yLeft+15, xLeft+100, yLeft+15, xLeft+30, yLeft+15, xLeft+30, yLeft+30, outline = "white", fill = "", width = 4)
  
  up = screen.create_polygon(xUp, yUp, xUp+30, yUp+30, xUp+15, yUp+30, xUp+15, yUp+100, xUp-15, yUp+100, xUp-15, yUp+30, xUp-30, yUp+30, outline = "White", fill = "", width = 4)
  
  down = screen.create_polygon(xDown, yDown, xDown+30, yDown-30, xDown+15, yDown-30, xDown+15, yDown-100, xDown-15, yDown-100, xDown-15, yDown-30, xDown-30, yDown-30, fill = "", outline = "white", width = 4)
  
  right = screen.create_polygon(xRight, yRight, xRight-30, yRight-30, xRight-30, yRight-15, xRight-100, yRight-15, xRight-100, yRight+15, xRight-30, yRight+15, xRight-30, yRight+30, outline = "white", fill = "", width = 4)


#Checks if Background Should be Changed
def checkBack(): 
  global score, changeBack, firstDrop, secondDrop, thirdDrop, fourthDrop

  if 4000 < score < 8000 and changeBack == 1: 
    screen.delete(firstDrop)
    createBackground()

  elif 8000 < score < 12000 and changeBack == 2: 
    screen.delete(secondDrop)
    createBackground()

  elif 12000 < score and changeBack == 3: 
    screen.delete(thirdDrop)
    createBackground()
    
#Updates the Scoreboard 
def updateScore():
  global score, scoreboard

  scoreboard = screen.create_text(725, 70, text = str(score), font = "times 20", fill = "white")


#Deletes Scoreboard  
def deleteScore():
  global scoreboard
  
  screen.delete(scoreboard)



#Updates the Current Combo
def updateCombo(): 
  global comboDisplay
  
  comboDisplay = screen.create_text(725, 120, text = str(combo), font = "times 20", fill = "white" )


#Deletes Combo Display
def deleteCombo(): 
  global comboDisplay

  screen.delete(comboDisplay)



#Displays Lives
def drawLives():
  global lives, cHeart, numLives

  numLives = screen.create_text(725, 170, text = str(lives), font = "times 20", fill = "white")


#Deletes Lives
def deleteHearts():
  global numLives

  screen.delete(numLives)



#***** ARROWS *****

#Chooses Random Colour for Arrows 
def colArrow():
  global colArray, colArrowChoice

  colArrowChoice = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "black", "salmon", "orchid", "grey", "maroon", "brown", "aquamarine", "cadetblue", "forestgreen", "rosybrown", "slateblue", "seagreen", "gold", "silver", "firebrick", "coral", "palevioletred", "plum"]

  colLeft()
  colDown()
  colUp()
  colRight()


def colLeft(): 
  global numColLeft

  numColLeft = randint(0, len(colArrowChoice)-1) 
  
def colDown(): 
  global numColDown
  
  numColDown = randint(0, len(colArrowChoice)-1) 
  
def colUp():
  global numColUp
  
  numColUp = randint(0, len(colArrowChoice)-1) 
  
def colRight():
  global numColRight
  
  numColRight = randint(0, len(colArrowChoice)-1) 



#Draws Arrows 
def drawArrows():
  global xLeft, xUp, xDown, xRight, yLeftFall, yUpFall, yDownFall, yRightFall, colFall, leftArrows, upArrows, downArrows, rightArrows, numColLeft, numColUp, numColDown, numColRight, colArrowChoice

  leftArrows= screen.create_polygon(xLeft, yLeftFall, xLeft+30, yLeftFall-30, xLeft+30, yLeftFall-15, xLeft+100, yLeftFall-15, xLeft+100, yLeftFall+15, xLeft+100, yLeftFall+15, xLeft+30, yLeftFall+15, xLeft+30, yLeftFall+30, fill = colArrowChoice[numColLeft], outline = "black", width = 2)

  upArrows = screen.create_polygon(xUp, yUpFall, xUp+30, yUpFall+30, xUp+15, yUpFall+30, xUp+15, yUpFall+100, xUp-15, yUpFall+100, xUp-15, yUpFall+30, xUp-30, yUpFall+30, fill = colArrowChoice[numColUp], outline = "black", width = 2)

  downArrows = screen.create_polygon(xDown, yDownFall, xDown+30, yDownFall-30, xDown+15, yDownFall-30, xDown+15, yDownFall-100, xDown-15, yDownFall-100, xDown-15, yDownFall-30, xDown-30, yDownFall-30, fill = colArrowChoice[numColDown], outline = "black", width = 2)

  rightArrows = screen.create_polygon(xRight, yRightFall, xRight-30, yRightFall-30, xRight-30, yRightFall-15, xRight-100, yRightFall-15, xRight-100, yRightFall+15, xRight-30, yRightFall+15, xRight-30, yRightFall+30, fill = colArrowChoice[numColRight], outline = "black", width = 2)



#Moves Arrows
def updateArrows():
  global yLeftFall, yUpFall, yDownFall, yRightFall, leftArrows, yLeftSpeed, yRightSpeed, yDownSpeed, yUpSpeed, lives, combo, highestCombo

  yLeftFall = yLeftFall + yLeftSpeed
  yUpFall = yUpFall + yLeftSpeed 
  yDownFall = yDownFall + yDownSpeed 
  yRightFall = yRightFall + yRightSpeed 


  if yLeftFall > 790:
    lives = lives - 1 
    combo = 0
    colLeft()
    yLeftFall = -10 
    if yLeftSpeed < 7.5:
      yLeftSpeed = yLeftSpeed * 1.1

  if yUpFall > 790: 
    lives = lives - 1 
    combo = 0 
    colUp()
    yUpFall = -50
    if yUpSpeed < 7.5: 
      yUpSpeed = yUpSpeed* 1.1
  
  if yDownFall > 790: 
    lives = lives - 1 
    combo = 0 
    colDown()
    yDownFall = -10 
    if yDownSpeed < 7.5: 
      yDownSpeed = yDownSpeed * 1.1

  if yRightFall > 790: 
    lives = lives - 1 
    combo = 0 
    colRight()
    yRightFall = -10
    if yRightSpeed < 7.5: 
      yRightSpeed = yRightSpeed * 1.1
    

#Deletes Arrows 
def deleteArrows():
  global leftArrows, upArrows, downArrows, rightArrows 

  screen.delete(leftArrows, upArrows, downArrows, rightArrows)



#***** KEYS *****

#Checks Whenever Left Mouse Key is Pressed
def mouseClickHandler(event): 
  global xMouse, yMouse

  xMouse = event.x 
  yMouse = event.y

  if introScreen == True: 
    checkIntro()

  elif rulesScreen == True: 
    checkRules()

  elif difficultyScreen == True: 
    checkDiff()

  elif triviaScreen == True: 
    checkTrivQues()

  elif gameOverScreen == True: 
    checkGameOver() 



#Checks When Arrow Keys are Pressed 
def keyHandler(event):
  
  if event.keysym == "Right":
    checkRightKey() 
  elif event.keysym == "Left":
    checkLeftKey()
  elif event.keysym == "Up": 
    checkUpKey()
  elif event.keysym == "Down": 
    checkDownKey()


#Checks Each Key
def checkLeftKey():
  global yLeft, yLeftFall, yLeftSpeed, score, combo, highestCombo

  dist = math.dist([yLeft], [yLeftFall])

  if dist < 30: 

    yLeftFall = -10 
    score = score + 100 
    combo = combo + 1
    colLeft() 
    if yLeftSpeed < 7.5:
      yLeftSpeed = yLeftSpeed * 1.1

    if combo > highestCombo: 
      highestCombo = combo 


def checkUpKey(): 
  global yUp, yUpFall, yUpSpeed, score, combo, highestCombo

  dist = math.dist([yUp], [yUpFall])

  if dist < 40:

    yUpFall = -50 
    score = score + 100
    combo = combo + 1 
    colUp()
    if yUpSpeed < 7.5: 
      yUpSpeed = yUpSpeed * 1.1

    if combo > highestCombo: 
      highestCombo = combo 


def checkDownKey(): 
  global yDown, yDownFall, yDownSpeed, score, combo, highestCombo

  dist = math.dist([yDown], [yDownFall])

  if dist < 40:

    yDownFall = -10 
    score = score + 100 
    combo = combo + 1 
    colDown()
    if yDownSpeed < 7.5: 
      yDownSpeed = yDownSpeed * 1.1

    if combo > highestCombo: 
      highestCombo = combo


def checkRightKey():
  global yRight, yRightFall, yRightSpeed, score, combo, highestCombo

  dist = math.dist([yRight], [yRightFall])
  
  if dist < 30: 

    yRightFall = -10 
    score = score + 100 
    combo = combo + 1
    colRight()
    if yRightSpeed < 7.5:
      yRightSpeed = yRightSpeed * 1.1

    if combo > highestCombo: 
      highestCombo = combo



#Uploads Backgrounds of Pre-Game Screens
def uploadBacks(): 
  global intro, rules, rulesBackdrop, diff

  intro = PhotoImage(file="introscreen.gif")
  rulesBackdrop = PhotoImage(file="rulesBackground.gif")
  diff = PhotoImage(file="diffBack.gif")



#***** INTRO SCREEN *****

def introduction(): 
  global introBack, introScreen, intro, triviaScreen, gameOverScreen, rulesScreen, difficultyScreen, rulesBackdrop

  uploadBacks()

  #Other Screens 
  introScreen = True
  triviaScreen = False
  gameOverScreen = False 
  rulesScreen = False
  difficultyScreen = False

  introBack = screen.create_image(400, 400, image = intro)


#Checks Buttons
def checkIntro(): 
  global xMouse, yMouse

  if 70 < xMouse < 325 and 434 < yMouse < 589: 
    deleteIntro()
    introScreen = False
    difficulty() 

  elif 455 < xMouse < 710 and 434 < yMouse < 589:
    deleteIntro()
    introScreen = False
    rules()


#Deletes Intro Screen
def deleteIntro():
  global introBack

  screen.delete(introBack)

  

#***** DIFFICULTY SCREEN *****

def difficulty(): 
  global difficultyScreen, introScreen, triviaScreen, gameOverScreen, difficultyBack, diff
  
  #Other Screens 
  difficultyScreen = True
  introScreen = False 
  triviaScreen = False 
  gameOverScreen = False 
  
  difficultyBack = screen.create_image(400, 400, image = diff) 


#Checks Buttons
def checkDiff(): 
  global xMouse, yMouse, mode 

  if 195 < xMouse < 605 and 225 < yMouse < 350: 
    deleteDiff()
    mode = "Normal"
    runGame()

  elif 195 < xMouse < 605 and 415 < yMouse < 550:
    deleteDiff()
    mode = "Hard" 
    runGame()

  elif 195 < xMouse < 605 and 595 < yMouse < 720: 
    deleteDiff() 
    mode = "Extreme"
    runGame()


#Deletes Difficulty Screen
def deleteDiff(): 
  global difficultyBack 

  screen.delete(difficultyBack)



#***** RULES SCREEN *****

def rules():
  global rulesBack, rulesScreen, rulesBackdrop, introScreen, triviaScreen, gameOverScreen
  
  #Other Screens 
  rulesScreen = True
  introScreen = False 
  triviaScreen = False 
  gameOverScreen = False

  rulesBack = screen.create_image(400, 500, image = rulesBackdrop) 


#Checks Buttons
def checkRules():
  global xMouse, yMouse, rulesScreen

  if 44 < xMouse < 194 and 25 < yMouse < 95: 
    deleteRules()
    rulesScreen = False 
    introduction()


#Deletes Rules Screen
def deleteRules(): 
  global rulesBack

  screen.delete(rulesBack)
  


#***** TRIVIA SCREEN *****
def trivia():
  global lives, triviaScreen, triviaChances

  triviaChances = triviaChances + 1 
  triviaScreen = True
  triviaQuestions()
  triviaBox()
  
  
#Draws Screen  
def triviaBox():

  global numQues , triQues, triAns, triWrong, anSide, trivSelect, trivText, trivLeft, trivRight, leftAns, rightAns, quesBack

  quesBack = screen.create_image(400, 400, image = triviaBack)
  trivText = screen.create_text(400, 300, text = triQues[numQues], font = "times 30", fill = "white")
  
  #Randomizes Side of Answers
  trivSelect = randint(1,2) 

  if trivSelect == 1: 
    leftAns = screen.create_text(215, 505, text = triAns[numQues], font = "times 15", fill = "black")
    rightAns = screen.create_text(570, 505, text = triWrong[numQues], font = "times 15", fill = "black")

  else: 
    leftAns = screen.create_text(215, 505, text = triWrong[numQues], font = "times 15", fill = "black")
    rightAns = screen.create_text(570, 505, text = triAns[numQues], font = "times 15", fill = "black")
  

#Stores and Selects Trivia Question and Answers
def triviaQuestions():
  global triQues, triAns, triWrong, numQues


  triQues = ["What African country used \nto be called Swaziland?", "  How many players are on \n a Quidditch team?", "What is the largest ocean?", "Which country useses red \ntext on their license plates?", "What is the smallest country?", "How many hearts does \nan octopus have?", "What country produces the \nmost coffee in the world?", "How many Pyramids of\n Giza were made?", "Which planet was named \nafter the Roman God of War?", "What is Shakespeares \nlongest play?", "How many ribs are in a \nhuman body?", "What is the world's biggest \nisland?", "What is the smallest ocean \nin the world?", "What country won the first \nFIFA World Cup?", "How many eyes does a bee \nhave?", "What rock band was formed \nby Jimmy Page?", "Where was Beethoven born?", "What country made \nCaesar Salad?", "Which country did bagels \noriginate from?", "Which country has the most \nvending machines?", "What is the driest continent?", "What colour is a polar bear's \nskin?", "What currency is used in \nSouth Africa?", "Which name is a city on \nevery continent?", "Which element has the \nchemical symbol of Hg?", "What language has the most \nwords?", "How many phases does the \nmoon have?", "How many rides are at \nDisney World?", "How many time-zones are \nthere in the world?", "How many years is an eon?", "Which organ do insects \nnot have?", "What is the fastest fish in \nthe sea?", "What bird can fly backwards?", "One kilogram is how many \npounds?", "What is the largest rodent in \nNorth America", "What is wiccaphobia?", "Where is the Rhine River?", "How many teeth does an \nadult cat have?", "What side of the road does \nJapan drive on?", "Which country's flag \nfeatures a dragon?", "What colour are Tunisia's \nlicense plates?", "What language has this \ncharacter: ł?", "What is the fourth string \nof a guitar?", "How long is an EP?", "How many countries are in \nEurope?"]


  triAns = ["Eswatini", "Seven", "Pacific", "Belgium", "Vatican City", "Three", "Brazil", "Three", "Mars", "Hamlet", "Twenty-Four", "Greenland", "The Arctic", "Uruguay", "Five", "Led Zeppelin", "Berlin", "Mexico", "Poland", "Japan", "Antartica", "Black", "Rand", "Rome", "Mercury", "English", "Eight", "Fifty-Two", "Twenty-Four", "Billion", "Lungs", "Sailfish", "Hummingbird", "2.2", "Beaver", "Fear of Witchcraft", "Europe", "Thirty", "Left", "Bhutan", "Black", "Polish", "D", "Thirty minutes \nor less", "Fourty-Four"]


  triWrong = ["Rwanda", "Eight", "Atlantic", "Turkey", "Monaco", "Two", "Colombia", "Five", "Saturn", "Cymbeline", "Twenty-Two", "New Guinea", "Southern", "Argentina", "Three", "The Rolling Stones", "Vienna", "Italy", "Netherlands", "Australia", "Africa", "Orange", "Naira", "Paris", "Copper", "Arabic", "Seven", "Fifty-Four", "Twenty", "Million", "Intestine", "Swordfish", "Mockingbird", "2.15", "Porcupine", "Fear of spider webs", "Central America", "Twenty-Five", "Right", "Nepal", "Yellow", "Lithuanian", "G", "Twenty minutes \nor less", "Fourty-Two"]

  numQues = randint(0, len(triQues)-1)


#Checks Buttons
def checkTrivQues(): 
  global xMouse, yMouse, trivSelect

  if 100 < xMouse < 330 and 410 < yMouse < 600: 
    
    if trivSelect == 1: 
      secondChance() 
    else: 
      gameOver()

  elif 450 < xMouse < 680 and 410 < yMouse < 600: 

    if trivSelect == 1: 
      gameOver()
    else: 
      secondChance() 


#Continues Game
def secondChance(): 
  global alive, lives, triviaScreen  

  deleteTrivia()
  lives = 6 
  triviaScreen = False
  alive = True
  reUpdate()
  continueGame()
  

#Gives Player a Smoother Transition to Continue
def reUpdate(): 
  global yLeftFall, yUpFall, yDownFall, yRightFall, yLeftSpeed, yUpSpeed, yDownSpeed, yRightSpeed

  yLeftFall = yLeftFall - 300 
  yUpFall = yUpFall - 300
  yDownFall = yDownFall - 300
  yUpFall = yUpFall - 300 

  yLeftSpeed = yLeftSpeed - (yLeftSpeed*0.5)
  yUpSpeed = yUpSpeed - (yUpSpeed*0.5) 
  yDownSpeed = yDownSpeed - (yDownSpeed*0.5) 
  yRightSpeed = yRightSpeed - (yRightSpeed*0.5)
  

#Deletes Trivia Screen
def deleteTrivia(): 
  global quesBack, trivText, leftAns, rightAns 

  screen.delete(quesBack, trivText, leftAns, rightAns)



#Checks how many lives player has
def checkLives(): 
  global alive 

  if lives > 0: 
      alive = True 
  else: 
    alive = False
    if triviaChances < 3: 
      trivia()
    else: 
      gameOver()



#***** GAME OVER SCREEN *****
def gameOver(): 
  global gameOverScreen, introScreen, rulesScreen, difficultyScreen, triviaScreen
  
  #Other Screens
  gameOverScreen = True 
  introScreen = False
  rulesScreen = False
  difficultyScreen = False 
  triviaScreen = False

  gameOverBackground()
  

#Draws Screen
def gameOverBackground(): 
  global overScore, gameOverBack, overCombo

  screen.create_image(400, 400, image = gameOverBack)
  overScore = screen.create_text(400, 335, text = str(score), font = "times 40", fill = "white")
  overCombo = screen.create_text(400, 520, text = str(highestCombo), font = "times 40", fill = "white")


#Checks Buttons
def checkGameOver(): 
  global xMouse, yMouse, gameOverScreen

  if 290 < xMouse < 510 and 640 < yMouse < 730: 
    deleteGameOver() 
    gameOverScreen = False
    runGame() 


#Deletes Screen
def deleteGameOver(): 
  global overScore, gameOverBack

  screen.delete(overScore, gameOverBack, overCombo)



#Runs Game 
def runGame():
  global introScreen, triviaScreen, gameOverScreen, rulesScreen, difficultyScreen
  
  #Screens
  introScreen = False 
  triviaScreen = False
  gameOverScreen = False
  rulesScreen = False
  difficultyScreen = False
  
  setInitialValues()
  createBackground()
  colArrow()
  checkLives()
  continueGame() 


#Continues Game
def continueGame(): 
  global alive 

  while alive == True:
    updateArrows()
    drawArrows()
    updateScore()
    updateCombo()
    drawLives()
    screen.update()
    sleep(0.01)
    deleteArrows()
    deleteScore()
    deleteCombo()
    deleteHearts()
    checkLives()
    checkBack()



#Keybinds
screen.bind("<Button-1>", mouseClickHandler) 
screen.bind( "<Key>", keyHandler)  


root.after(500, introduction)

screen.pack()
screen.focus_set()
root.mainloop()
