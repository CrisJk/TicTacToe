import turtle
t=turtle.Turtle()

m = [['-','-','-'],['-','-','-'],['-','-','-']]
a = 1
b = 1


def getNumberOfClicks(a=[0]):
    a[0]+= 1
    return (a[0])


def drawBoard():
    "This function will draw a tic tac toe board"
    t.up()
    t.ht()
    t.goto(0,0)
    t.down()    
    t.forward(240)
    t.right(90)
    t.forward(240)
    t.right(90)
    t.forward(240)
    t.right(90)
    t.forward(240)
    t.up()
    t.goto(80,-240)
    t.down()
    t.forward(240)
    t.up()
    t.goto(160,-240)
    t.down()
    t.forward(240)
    t.up()
    t.right(90)
    t.goto(0,-80)
    t.down()
    t.forward(240)
    t.up()
    t.goto(0,-160)
    t.down()
    t.forward(240)
    



def getPos(x,y):
    global a
    a = x
    global b
    b = y



def getShitDone(x,y):
    temp = getNumberOfClicks()
    getPos(x,y)
    valid = True
    
    if 80 > a >0 and -80<b<0:
        i=0
        j=0
    elif 80 > a >0 and -160<b<-80:
        i=1
        j=0
    elif 80 > a >0 and -240<b<-160:
        i=2
        j=0
    elif 160 > a >80 and -80<b<0:
        i=0
        j=1
    elif 160 > a >80 and -160<b<-80:
        i=1
        j=1
    elif 160 > a >80 and -240<b<-160:
        i=2
        j=1
    elif 240 > a >160 and -80<b<0:
        i=0
        j=2
    elif 240 > a >160 and -160<b<-80:
        i=1
        j=2
    elif 240 > a >160 and -240<b<-160:
        i=2
        j=2
    else:
        print("Veuillez selectionner une case appropriee svp.")
        valid = False
        
    if temp%2==0 and valid == True:
        t.up()
        t.goto(0+j*80,0-i*80)
        t.down()
        t.right(45)
        t.forward(113.137085)
        t.right(90)
        t.up()
        t.goto(80+j*80,0-i*80)
        t.down()
        t.forward(113.137085)
        t.left(135)
        m[i][j]="X"
        print(m)
        temp += 1
    elif temp%2 != 0 and valid == True:
        t.up()
        t.goto(40+j*80,-80-i*80)
        t.down()
        t.circle(40)
        m[i][j] = "O"
        temp += 1
        print(m)
        
turtle.Screen().onscreenclick(getShitDone)
drawBoard


