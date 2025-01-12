import pgzrun, random, time

WIDTH = 900
HEIGHT = 700
TITLE = "GALAGA"

ship = Actor("galaga")
enemy = Actor("bug")

ship.pos = (WIDTH/2, HEIGHT-60)

enemies = []
enemies.append(enemy)

enemies[-1].x = random.randint(50, WIDTH-50)
enemies[-1].y = -150

bullets = []

score = 0
speed = 5

def draw():
    screen.clear()
    
    screen.fill("black")
    
    ship.draw()
    for i in enemies: 
        i.draw()
    for i in bullets:
        i.draw()    
        
def update():
    global score, speed
     
    if keyboard.left:
         ship.x -= speed
         if ship.x < 50:
             ship.x = 50
         
    elif keyboard.right:
        ship.x += speed
        if ship.x > WIDTH-50:
            ship.x = WIDTH-50
            
    for i in enemies:
        i.y += 5
        if i.y > HEIGHT:
            i.y = -100
            i.x = random.randint(50, WIDTH-50)
        for j in bullets:
            if j.colliderect(i):
                score += 100
                enemies.remove(i)
                bullets.remove(j)  
                  
    for i in bullets:
        if i.y < 0:
            bullets.remove(i)
        else:
            i.y -= 1            

def on_key_down(key):
    if key == keys.SPACE:
        bullet = Actor("bullet")
        bullets.append(bullet)                  
        
        bullets[-1].x = ship.x
        bullets[-1].y = ship.y-50    

pgzrun.go()