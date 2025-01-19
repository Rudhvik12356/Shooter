import pgzrun, random, time

WIDTH = 1000
HEIGHT = 1500
TITLE = "Bow and Arrow"

bow = Actor("crossbow")
enemy = Actor("person")

bow.pos = (WIDTH/2, HEIGHT-400)

enemies = []
enemies.append(enemy)

enemies[-1].x = random.randint(50, WIDTH-50)
enemies[-1].y = -150

arrows = []

score = 0
speed = 10

def draw():
    screen.clear()
    
    screen.fill("black")
    
    bow.draw()
    for i in enemies: 
        i.draw()
    for i in arrows:
        i.draw()    
        
def update():
    global score, speed
     
    if keyboard.left:
         bow.x -= speed
         if bow.x < 50:
             bow.x = 50
         
    elif keyboard.right:
        bow.x += speed
        if bow.x > WIDTH-50:
            bow.x = WIDTH-50
            
    for i in enemies:
        i.y += 5
        if i.y > HEIGHT:
            i.y = -100
            i.x = random.randint(50, WIDTH-50)
        for j in arrows:
            if j.colliderect(i):
                score += 100
                enemies.remove(i)
                arrows.remove(j)  
                  
    for i in arrows:
        if i.y < 0:
            arrows.remove(i)
        else:
            i.y -= 10           

def on_key_down(key):
    if key == keys.SPACE:
        arrow = Actor("arrow")
        arrows.append(arrow)                  
        
        arrows[-1].x = bow.x
        arrows[-1].y = bow.y-50    

pgzrun.go()