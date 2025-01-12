import pgzrun

TITLE = "The HARRY POTTER QUIZ GAME"
WIDTH = 900
HEIGHT = 700

score = 0
timer = 10
questionFile = "pyGame\questionsHW.txt"

marqueeMessage = ""
gameState = "play"

marqueeBox = Rect(0,0, 870, 80)
questionBox = Rect(0,0, 650, 150)
timerBox = Rect(0,0, 150, 150)
skipBox = Rect(0,0, 150, 300)
answerBox1 = Rect(0,0, 300, 150)
answerBox2 = Rect(0,0, 300, 150)
answerBox3 = Rect(0,0, 300, 150)
answerBox4 = Rect(0,0, 300, 150)

answerBox = [answerBox1, answerBox2, answerBox3, answerBox4]
questions = []
questionCount = 0
questionIndex = 0

marqueeBox.move_ip(0,0)
questionBox.move_ip(20, 100)
timerBox.move_ip(700, 100)
skipBox.move_ip(700, 270)
answerBox1.move_ip(20, 270)
answerBox2.move_ip(370, 270)
answerBox3.move_ip(20 ,450)
answerBox4.move_ip(370, 450)

def draw():
    global marqueeMessage
    
    screen.clear()
    
    screen.draw.filled_rect(marqueeBox, "blue")
    screen.draw.filled_rect(questionBox, "lime")
    screen.draw.filled_rect(timerBox, "lime")
    screen.draw.filled_rect(skipBox, "cyan")
    
    for i in answerBox:
        screen.draw.filled_rect(i, "red")
    
    marqueeMessage = "Welcome to the Harry Potter Quiz!"
    marqueeMessage += f"Q: {questionIndex} of {questionCount}"        

    screen.draw.textbox(marqueeMessage, marqueeBox, color = "black")
    screen.draw.textbox(str(timer), timerBox, color = "black")
    screen.draw.textbox(question[0], questionBox, color = "black")
    screen.draw.textbox("SKIP", skipBox, color = "black", angle = -90)
    
    index = 1
    
    for i in answerBox:
        screen.draw.textbox(question[index].strip(), i, color = "black")
        index += 1
        
def update():
    marqueeBox.x -= 2
    
    if marqueeBox.right < 0:
        marqueeBox.left = WIDTH
                   
def readQuestionFile():
    global questionCount, questions
    
    question_file = open(questionFile, "r")
    
    for i in question_file:
        questions.append(i)
        questionCount += 1
    question_file.close()    

def readNextQuestion():
    global questionIndex
    questionIndex += 1
    
    return questions.pop(0).split(",")

def on_mouse_down(pos):
    index = 1
    
    for i in answerBox:
        if i.collidepoint(pos):
            if index is int(question[5]):
                correctAnswer()
            else:
                gameOver()        
        index += 1
        
    if skipBox.collidepoint(pos):
        skipQuestion()
                    
def correctAnswer():
    global score, question, timer, questions
    
    score += 1
    
    if questions:
        question = readNextQuestion()
        timer = 10
    else:
        gameOver()
        
def skipQuestion():
    global question, timer
    
    if questions and gameState == "play":
        question = readNextQuestion()
        timer = 10
    else:
        gameOver()

def updateTimer():
    global timer
    
    if timer:
        timer -= 1
    else:
        gameOver()                             
        
def gameOver():
    global question, timer, gameState
    
    message = f"Game Over!\n You got {score} of {questionCount} questions correct!"
    question = [message, "-", "-", "-", "-", 4]
    timer = 0
    gameState = "over"                    
         
readQuestionFile()
question = readNextQuestion()
clock.schedule_interval(updateTimer, 1)

pgzrun.go()