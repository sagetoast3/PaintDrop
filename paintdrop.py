from Tkinter import *
import math
import random
import tkColorChooser 
 
#Control#

#Clicking#
def mousePressed(event):
    x=event.x
    y=event.y
    print x,y
    ShapeEnclosed = canvas.find_closest(x,y, halo=2) #find shape that was clicked
    ShapeTag= canvas.gettags(ShapeEnclosed)#find its associated tag
    canvas.data.currentShape=ShapeEnclosed
    canvas.data.currentTag=ShapeTag #find tags for buttons/objects
#Tools#
    #Pen#
    if 'PenButton' in ShapeTag:
        turnAllStatesOffExcept("draw")
        clearMode()
        penMode()
        #print canvas.data.stateDict
        #Pen Sub-Tools#
    if 'small' and 'pen' in ShapeTag:
        canvas.data.drawModes["size"]='small'
    if 'medium' and 'pen' in ShapeTag:
        canvas.data.drawModes["size"]='medium'
    if 'large' and 'pen' in ShapeTag:
        canvas.data.drawModes['size']='large'
    if 'Pen' and 'Fill' in ShapeTag:
        #color chooser should pop up
        #then save that color for use in the mouseMotion and pass it in the draw function that's called
        color=tkColorChooser.askcolor()
        canvas.data.drawModes["fill"]=color[1]
    #Brush#
    if 'brush' in ShapeTag:
        turnAllStatesOffExcept("brush")
        clearMode()
        thickBrushMode()
    #if 'brush' and 'fill' in ShapeTag:
    if 'reds' in ShapeTag:
        canvas.data.thickBrushModes['color theme']='reds'
    if 'blues' in ShapeTag:
        canvas.data.thickBrushModes['color theme']='blues'
    if 'greens' in ShapeTag:
        canvas.data.thickBrushModes['color theme']='greens'
    print canvas.data.thickBrushModes['color theme']
    #Ribbon#    
    if 'Calligraph' in ShapeTag:
        turnAllStatesOffExcept("calligraph")
        clearMode()
        ribbonMode()
        #Ribbon Sub Tools
    if 'Horizontal' in ShapeTag:
        #draw function takes in parameter for flat brush
        canvas.data.ribbonModes["tilt"]='horizontal'
    if 'Vertical' in ShapeTag:
        #draw function takes in parameter for vert brush (which is default)
        canvas.data.ribbonModes["tilt"]='vertical'
    if 'Ribbon' and 'Fill' in ShapeTag:
        color=tkColorChooser.askcolor()
        canvas.data.ribbonModes["fill"]=color[1]
    if 'Ribbon' and 'Outline' in ShapeTag:
        color=tkColorChooser.askcolor()
        canvas.data.ribbonModes["outline"]=color[1]
    #Eraser
    if  'Eraser' in ShapeTag: 
        turnAllStatesOffExcept("eraser")
        clearMode()
    #Shapes
    if 'SquareButton' in ShapeTag:
        #createSquare with default values and tag 'movable'
        turnAllStatesOffExcept()
        canvas.create_rectangle(400,300, 450,350, fill="light blue", outline="white", tag='movable')
        clearMode()
        shapeMode()
    if 'CircleButton' in ShapeTag:
        #createCircle with default values and tag 'movable'
        turnAllStatesOffExcept()
        canvas.create_oval(300,200, 400, 300, fill="light yellow",outline="white", tag='movable')
        clearMode()
        shapeMode()
    if 'TriangleButton' in ShapeTag:
        #createCircle with default values and tag 'movable'
        turnAllStatesOffExcept()
        canvas.create_polygon(300,300,350,250,400,300, fill="light pink", outline="white", tag='movable')
        clearMode()
        shapeMode()
    if 'movable' in ShapeTag:
        #create handles at corners and midpoints each tagged accordingly
        canvas.data.startx=x
        canvas.data.starty=y
        #Shape Sub Tools
    if 'Shape Outline' in ShapeTag:
        color=tkColorChooser.askcolor()
        lineColor=color[1]
        c=canvas.data.currentlySelected
        canvas.config(c,outline=lineColor)
    if 'Shape Fill' in ShapeTag:
        color=tkColorChooser.askcolor()
        fillColor=color[1]
        c=canvas.data.currentlySelected
        print 'c is', c
        canvas.config(c,fill=fillColor)
        
        
#Allow Canvas Color Changes when user clicks the color boxes
    i=canvas.find_withtag('drawBox')
    j=canvas.find_withtag('eraserMark')
    if 'cc1' in ShapeTag:
        newfill='navajo white'
        canvas.data.currentCanvasColor=newfill
        canvas.itemconfig(i,fill=newfill,outline=newfill)
        for item in j:
            canvas.itemconfig(item,fill=newfill, outline=newfill)
        canvas.data.currentCanvasColor=newfill
    elif 'cc2' in ShapeTag:
        newfill='ghost white'
        canvas.data.currentCanvasColor=newfill
        canvas.itemconfig(i,fill=newfill,outline=newfill)
        for item in j:
            canvas.itemconfig(item,fill=newfill, outline=newfill)
        canvas.data.currentCanvasColor=newfill
    elif 'cc3' in ShapeTag:
        newfill='papaya whip'
        canvas.data.currentCanvasColor=newfill
        canvas.itemconfig(i,fill=newfill,outline=newfill)
        for item in j:
            canvas.itemconfig(item,fill=newfill, outline=newfill)
        canvas.data.currentCanvasColor=newfill
    elif 'cc4' in ShapeTag:
        newfill='light yellow'
        canvas.data.currentCanvasColor=newfill
        canvas.itemconfig(i,fill=newfill,outline=newfill)
        for item in j:
            canvas.itemconfig(item,fill=newfill, outline=newfill)
        canvas.data.currentCanvasColor=newfill
    elif 'cc5' in ShapeTag:
        newfill='dark slate grey'
        canvas.data.currentCanvasColor=newfill
        canvas.itemconfig(i,fill=newfill,outline=newfill)
        for item in j:
            canvas.itemconfig(item,fill=newfill, outline=newfill)
        canvas.data.currentCanvasColor=newfill
    elif 'cc6' in ShapeTag:
        newfill='dim grey'
        canvas.data.currentCanvasColor=newfill
        canvas.itemconfig(i,fill=newfill,outline=newfill)
        for item in j:
            canvas.itemconfig(item,fill=newfill, outline=newfill)
        canvas.data.currentCanvasColor=newfill
    elif 'cc7' in ShapeTag:
        newfill='slate grey'
        canvas.data.currentCanvasColor=newfill
        canvas.itemconfig(i,fill=newfill,outline=newfill)
        for item in j:
            canvas.itemconfig(item,fill=newfill, outline=newfill)
        canvas.data.currentCanvasColor=newfill
    elif 'cc8' in ShapeTag:
        newfill='Ivory4'
        canvas.data.currentCanvasColor=newfill
        canvas.itemconfig(i,fill=newfill,outline=newfill)
        for item in j:
            canvas.itemconfig(item,fill=newfill, outline=newfill)
        canvas.data.currentCanvasColor=newfill
    doubleCShapes=canvas.data.currentlySelected #this is the list of the selected shapes
    if checkIfSelectedIsMovable():
        if 'Shape' and 'Layer' and 'Raise' in ShapeTag:
        #if user clicks on the Raise or Lower option on the left, check if there's a shape whose layer
        #should be adjusted (raised or lowered)
            for i in xrange(len(doubleCShapes)):
                canvas.tag_raise(doubleCShapes[i])
        if 'Shape' and 'Layer' and 'Lower' in ShapeTag:
            for i in xrange(len(doubleCShapes)):
                canvas.tag_lower(doubleCShapes[i]) 
                
def checkIfSelectedIsMovable():
    listOfShapes=canvas.data.currentlySelected
    if len(listOfShapes)==0:
        return False
    else:
        for i in xrange(len(listOfShapes)):
            if 'movable' not in canvas.gettags(listOfShapes[i]):
             return False
    return True

def mouseMotion(event):
    endx=event.x
    endy=event.y
    startx=canvas.data.startx
    starty=canvas.data.starty
    diffx, diffy =(endx-canvas.data.startx), (endy-canvas.data.starty)
    currentShape=canvas.data.currentShape
    ShapeTag=canvas.data.currentTag
    stateDict=canvas.data.stateDict
    #assocShapes=canvas.assocShapes
    if 'movable' in ShapeTag and stateDict["draw"]==False and stateDict["brush"]==False and stateDict["calligraph"]==False and stateDict["eraser"]==False: 
        if endx>160 and endx<890 and endy>150 and endy<510:
            canvas.move(currentShape, diffx, diffy)
        #shapes associated with the currentShape, those tagged with the original shapeID
            #move all handles/nodes associated with current shape as well
    if stateDict['draw']==True:
        turnAllStatesOffExcept('draw')
        color=canvas.data.drawModes["fill"]
        size=canvas.data.drawModes["size"]
        if endx>160 and endx<900 and endy>110 and endy<540:
            drawWithPen(size,color,endx,endy)
    if stateDict['brush']==True:
        turnAllStatesOffExcept('brush')
        #check the theme color that is currently chosen
        if endx>160 and endx<900 and endy>110 and endy<540:
            drawWithBrush(endx,endy)
    if stateDict['calligraph']==True:
        #canvas.data.draw==False
        #canvas.data.brush=False
        turnAllStatesOffExcept('calligraph')
        tilt= canvas.data.ribbonModes["tilt"]
        fill= canvas.data.ribbonModes["fill"]
        outline= canvas.data.ribbonModes["outline"]
        if endx>160 and endx<900 and endy>110 and endy<540:
            drawCalligraph(endx,endy,tilt,fill,outline)
        
    if stateDict['eraser']==True:
        turnAllStatesOffExcept('eraser')
        if endx>165 and endx<900 and endy>110 and endy<540:
            erase(endx,endy)
    canvas.data.startx=endx
    canvas.data.starty=endy

#Brush Helper Function

def drawWithPen(size,color,x,y):
    size=canvas.data.drawModes['size']
    if size=='small':
        canvas.create_oval(x,y,x,y,fill=color,outline=color)
    elif size=='medium':
        canvas.create_oval(x,y,x+2,y+2,fill=color,outline=color)
    elif size=='large':
        canvas.create_oval(x,y,x+8,y+8, fill=color,outline=color)
        
def erase(x,y):
    color=canvas.data.currentCanvasColor
    canvas.create_rectangle(x-5,y-5,x+5,y+5,fill=color, outline=color, tag='eraserMark')


def drawWithBrush(x,y):
    colortheme=canvas.data.thickBrushModes['color theme']
    for i in xrange(30): #create more random variation through varied locations for ovals and multicolor 
            radius=(random.randrange(10))/100
            degree= math.radians(random.randrange(1,365))
            pointx= ((math.cos(degree))*x)/100.0 +x
            pointy= ((math.sin(degree))*y)/100.0 +y
            ovalR= 3
            if colortheme=='reds':
                color=['plum','pink','salmon','indian red','pale violet red']
                canvas.create_oval(pointx-ovalR,pointy-ovalR,pointx+ovalR,pointy+ovalR, outline=color[random.randrange(5)])
            if colortheme=='blues':
                color=['light blue', 'powder blue', 'pale turquoise', 'dark turquoise', 'medium turquoise']
                canvas.create_oval(pointx-ovalR,pointy-ovalR,pointx+ovalR,pointy+ovalR, outline=color[random.randrange(5)])
            if colortheme=='greens':
                color=['DarkSeaGreen1', 'SeaGreen3', 'PaleGreen1','green2','green4']
                canvas.create_oval(pointx-ovalR,pointy-ovalR,pointx+ovalR,pointy+ovalR, outline=color[random.randrange(4)])
                
def drawCalligraph(x,y,tilt,fillColor,outlineColor):
    if tilt=='vertical': #draw the three vertical lines per x,y coordinate
        canvas.create_line(x,y-7,x,y+5,smooth=0,width=5,fill=fillColor)
        canvas.create_line(x,y-7,x,y-9, width=2, fill=outlineColor)
        canvas.create_line(x,y+5,x,+y+7, width=2, fill=outlineColor)
    if tilt=='horizontal':#draw the three horizontal lines per x,y coordinate
        canvas.create_line(x-7,y,x+5,y, smooth=0, width=5, fill=fillColor)
        canvas.create_line(x-7,y,x-9,y,width=2, fill=outlineColor)
        canvas.create_line(x+5,y,x+7,y,width=2,fill=outlineColor)
def doubleClick(event):
    x=event.x
    y=event.y
    ShapeEnclosed = canvas.find_closest(x,y, halo=2) #find shape that was clicked
    canvas.data.currentlySelected=ShapeEnclosed
    print "doubleClick", ShapeEnclosed
    ShapeTag= canvas.gettags(ShapeEnclosed) #find its associated tag
    #tag the shape as current, and later its associated nodes
    if 'movable' in ShapeTag:
        #if you double click and the tag says movable its a shape thats been laid down
        turnAllStatesOffExcept() #this makes sure that if you're in the middle of using a brush you can just double
                                #click to make sure that you exit draw mode and grab the shape your after
        canvas.data.doubleClicked=True
        clearMode() #this will reset the mode options
        shapeMode()
    canvas.data.current=ShapeEnclosed

def deleteShape(event):
    print "delete", canvas.data.current 
    item = canvas.data.current
    canvas.delete(item)

def displayShapeHandles(ShapeEnclosed):
    #If its not a circle
    listPoints=canvas.coords(ShapeEnclosed)
    nodes=createNodes(listPoints,ShapeEnclosed)

def createNodes(coordinates, ShapeEnclosed):
    ovalR=3
    #check if itemType!=circle then give each corner a node
    #put these into loop...
    UpperL1= (coordinates[0]-ovalR,coordinates[1]-ovalR)
    UpperL2= (coordinates[0]+ovalR,coordinates[1]+ovalR)
    canvas.create_oval(UpperL1,UpperL2,fill="red",tag="node")
    LowerR1= (coordinates[2]-ovalR,coordinates[3]-ovalR)
    LowerR2= (coordinates[2]+ovalR,coordinates[3]+ovalR)
    canvas.create_oval(LowerR1,LowerR2, fill="red", tag="node")
    canvas.addtag_withtag("current","node")
    
#Layout#
#Bordered Background#
def tempLayout():
    bkground()
    shapesButtons()
    toolsButtons()
    genButtons()
    canvasColors()
    drawBox()
    shapeLayerButtons()
    #shapeMode()
    #penMode()
    #ribbonMode()
    #thickBrushMode()
def bkground():
    canvas.create_rectangle(0,0,1100,600, fill="midnightblue")
    for i in xrange(10,1110, 10):
        for j in xrange(10,610,10):
            canvas.create_oval((i-10,j-10),(i,j), outline='dark slate grey', activefill="dim grey", fill='dark slate grey')
    canvas.create_rectangle(40,100, 1060,570, fill="misty rose")
    canvas.create_rectangle(40,40,1060,90, fill="misty rose")
    canvas.create_text(135,65, text='Paint Drop',font='Calibri 30',fill='light Sea Green')

def canvasColors():
    #This is the whole box's dimensions (905,405) (1050,540)
    canvas.create_rectangle(915,440, 940, 480, outline='navajo white', fill='navajo white',tag='navajo white cc1')
    canvas.create_rectangle(945,440, 970, 480, outline='ghost white', fill='ghost white',tag='ghost white cc2')
    canvas.create_rectangle(975,440, 1000, 480, outline='papaya whip', fill='papaya whip', tag='papaya whip cc3')
    canvas.create_rectangle(1005,440, 1030, 480, outline='light yellow', fill='light yellow',tag='light yellow cc4')
    #next color options
    canvas.create_rectangle(915,490,940,530, outline='dark slate grey', fill='dark slate grey', tag='dark slate grey cc5')
    canvas.create_rectangle(945,490,970,530, outline='dim grey', fill='dim grey', tag= 'dim grey cc6')
    canvas.create_rectangle(975,490,1000,530, outline='slate grey', fill='slate grey', tag= 'slate grey cc7')
    canvas.create_rectangle(1005,490,1030,530, outline='Ivory4', fill='Ivory4',tag='Ivory4 cc8')


def clearMode():
    canvas.create_rectangle((50,370),(150,540),width=1, outline="azure", fill="dark slate grey", tag='mode')
def shapeMode():
    #Header
    drawTextButton(60,385,75,'Shape Tool','Shape Options','dark slate grey')
    #Option for opacity with arrow controls
    drawTextButton(60,410,75,'Opacity','Opacity','dim grey')
    drawArrowButton(105,440,'left','Decrease Shape Opacity')
    drawArrowButton(105,440,'right','Increase Shape Opacity')
    #Color control of outline and fill
    drawTextButton(60,470, 75,'Outline','Shape Outline', 'dim grey')
    drawTextButton(60,500,75,'Fill','Shape Fill','dim grey')


def penMode():
    #Header
    drawTextButton(60,385,75,'Pen Tool','Pen Options','dark slate grey')
    #Size
    drawTextButton(60,410,75,'Size','Pen Size','dim grey')
    drawArrowButton(98,440,'left','small pen')
    canvas.create_oval(90,433,99,446, fill='dim grey',outline='dim grey', activeoutline='pink',tag='medium pen')
    drawArrowButton(110,440,'right', 'large pen')
    #Color Option
    drawTextButton(60,480,75,'Fill','Pen Fill','dim grey')

def ribbonMode():
    #Header
    drawTextButton(60,385,75,'Ribbon Tool','Ribbon Options','dark slate grey')
    #Shift the angle of the brush
    drawTextButton(60,410,75,'Horizontal','Horizontal','dim grey')
    drawTextButton(60,440,75,'Vertical','Vertical', 'dim grey')
    #Color options for fill and outline
    drawTextButton(60,480,75,'Fill','Ribbon Fill','dim grey')
    drawTextButton(60,510,75, 'Outline', 'Ribbon Outline', 'dim grey')
    
def thickBrushMode():
    #Header
    drawTextButton(60,385,75,'Thick Brush','Thick Brush','dark slate grey')
    drawTextButton(60,410,75,'Color Theme','Color Themes','dim grey')
    canvas.create_oval(85,430,105,450,fill='misty rose', outline='misty rose', tag='reds')
    canvas.create_oval(85,460,105,480,fill='powder blue', outline='powder blue', tag='blues')
    canvas.create_oval(85,490,105,510,fill='seagreen', outline='seagreen', tag='greens')

#(905,110,1050,400,
def shapeLayerButtons():
    drawTextButton(915,150,123, 'Raise','Shape Layer Raise', 'light sea green')
    drawTextButton(915,180,123, 'Lower','Shape Layer Lower', 'light sea green')
    autofill() 

def autofill():
    canvas.create_rectangle(915,210,1040,380, outline='darkseagreen', activeoutline='pink', fill='Darkseagreen')
    
    
def drawArrowButton(x,y, direction,tags):
    #given the center coordinates and string 'left' or 'right' this draws a small arrow button
    if direction=='right':
        canvas.create_polygon(x-7,y-7, x+5,y,x-7,y+7, outline='dim grey',activeoutline='pink', fill="dim grey",tag=tags)
    if direction=='left':
        canvas.create_polygon(x-12,y-7, x-24,y,x-12,y+7, outline='dim grey',activeoutline='pink', fill='dim grey',tag=tags)

def drawTextButton(x,y,length,string,tag, color):
    #Takes the upper corner coordinate of a button and it's label and draw's it
    canvas.create_rectangle(x,y-10, x+length, y+10, fill=color, outline=color, tag=tag)
    canvas.create_text(x+35,y, text=string, fill='pink',tag=tag)
    
#Buttons Layout#
def shapesButtons():
    #Square
    canvas.create_rectangle((50,110),(100,160), width=1, outline="white", fill="pink", tag="SquareButton")
    canvas.create_text(75,150, fill="White", text="Square",tag="SquareButton") #temp label
    #Circle
    canvas.create_rectangle((100,110),(150,160),width=1, outline="white", fill="pink", tag="CircleButton")
    canvas.create_text(125,150, fill="White", text="Circle", tag="CircleButton") 
    #Triangle
    canvas.create_rectangle((50,160),(100,210),width=1, outline="white", fill="pink", tag="TriangleButton")
    canvas.create_text(75,200, fill="White", text="Triangle", tag="TriangleButton")
    #Pen
    canvas.create_rectangle((100,160),(150,210),width=1, outline="white", fill="pink", tag="PenButton")
    canvas.create_text(125, 200, fill="White", text="Pen",tag="PenButton")
    
def toolsButtons():
    #Brush
    canvas.create_rectangle((50,210),(100,260),width=1, outline="white",fill="pink", tag="brush")
    canvas.create_text(75,250, fill="White", text="Brush",tag="brush")
    #Calligraph
    canvas.create_rectangle((100,210),(150,260), width=1, outline="white", fill="pink", tag="Calligraph")
    canvas.create_text(125,250, fill="white", text= "Ribbon", tag="Calligraph")
    #PresetShape1
    canvas.create_rectangle((50,260),(100,310), width=1, outline="white", fill="pink", tag='Select')
    canvas.create_text(75,300, fill="white", text='Select',tag='Select')
    #PresetShape2
    canvas.create_rectangle((100,260),(150,310),width=1, outline="white", fill="pink", tag='Eraser')
    canvas.create_text(125,300, fill="white", text='Eraser', tag='Eraser')
    
def genButtons():
    #Mode box for each tool
    canvas.create_rectangle((50,370),(150,540),width=1, outline="azure", fill="dark slate grey", tag='mode')
    #canvas.create_text(100,380, text='[mode]', fill='white', tag='mode')
    #Colors
    canvas.create_rectangle(905,110,1050,400, fill="azure", outline='pink', tag='layer options')
    canvas.create_text(970,125, text='Layer Options', fill='dark sea green')
    #Canvas Colors
    canvas.create_rectangle(905,405,1050,540, fill="light grey", outline='pink', tag='Canvas Colors')
    canvas.create_text(970,418, text='Canvas Color', fill='azure')
    
#Draw Space#
def drawBox():
    canvas.create_rectangle((160,110),(900,540), width=1, outline="pink", fill="white", tag='drawBox')
    #canvas.create_rectangle((590,100), (1050,550), width=1, outline="misty rose", fill="white
    
def init():
    canvas.data.starty = 0
    canvas.data.startx = 0
    canvas.data.listpoints=()
    canvas.data.currentCanvasColor='white'
    canvas.data.currentlySelected=[] #keep a list of shapes that are either double clicked or selected
    canvas.data.stateDict = {
        "draw":False,
        "brush":False,
        "calligraph":False,
        "eraser":False
    }
    canvas.data.drawModes = {
        "size":'small', #create a function that takes in the points neccessary to draw, then checks the state of this mode dict,
        "fill":'black'   #take in user input in the mouseClicked section, which changes these states
    }
    canvas.data.thickBrushModes = {
        "size":'medium', #or small or large
        "color theme": 'reds'
    }
    canvas.data.ribbonModes= {
        "tilt":'vertical', #or 'Horizontal'
        "fill":'papaya whip',
        "outline":'powder blue' #changes when user clicks outline button, chooses color, this changes
    }
    canvas.data.eraserModes= {
        "size": 'medium', #represent as eraser shapes
        "shape": 'square', #or circle
    }
    canvas.data.shapeModes= { 
        "opacity": 'none', #if none then clicking this > button has no effect, if middle or low you can
        "outline": 'pink', #user controlled
        "fill": 'pink' #user controlled
    }
    #canvas.data.theme= list of color combinations for boxes and buttons and background
    tempLayout()
    
def turnAllStatesOffExcept(*states):
    # set everything in the dictionary to False
    #use iterkeys to move through all items in stateDict
    stateDict= canvas.data.stateDict
    for key in stateDict.iterkeys():
        stateDict[key]=False
    for state in states:
        stateDict[state]=True
def run():
    # create the root and the canvas
    global canvas
    width=1100
    height=600
    root = Tk()
    canvas = Canvas(root, width=1100, height=600)
    canvas.pack()
    # Set up canvas data and call init
    class Struct: pass
    canvas.data = Struct()
    init()
    # set up events
    root.bind("<Button-1>", mousePressed)
    #root.bind("<Key>", keyPressed)
    root.bind("<B1-Motion>", mouseMotion)
    root.bind("<Double-1>", doubleClick)
    root.bind("<Delete>", deleteShape)
    #timerFired()
    # and launch the app
    root.mainloop()  # This call BLOCKS (so your program waits until you close the window!)

run()
 

    
