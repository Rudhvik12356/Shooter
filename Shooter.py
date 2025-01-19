import pgzrun, random, time

WIDTH = 900
HEIGHT = 700
TITLE = "GALAGA"

direction = 1

ship = Actor("galaga")
ship.pos = (WIDTH/2, HEIGHT-60)

enemies = []
for i in range(8):
    enemy = Actor("bug")
    enemies.append(enemy)

    enemies[-1].x = 80 * i + 100
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
        
    screen.draw.text("Score: " + str(score), (50, 50))        
        
def update():
    global score, speed, direction
     
    if keyboard.left:
         ship.x -= speed
         if ship.x < 50:
             ship.x = 50
         
    elif keyboard.right:
        ship.x += speed
        if ship.x > WIDTH-50:
            ship.x = WIDTH-50
            
    if len(enemies) > 0 and (enemies[0].x < 50 or enemies[-1].x > WIDTH - 50):
        direction = direction * (-1)
        
    for i in enemies:
        i.x += 2 * direction
        i.y += 3
        if i.y > HEIGHT:
            i.y = -100
        for j in bullets:
            if j.colliderect(i):
                score += 100
                enemies.remove(i)
                bullets.remove(j)  
                  
    for i in bullets:
        if i.y < 0:
            bullets.remove(i)
        else:
            i.y -= 5            

def on_key_down(key):
    if key == keys.SPACE:
        bullet = Actor("bullet")
        bullets.append(bullet)                  
        
        bullets[-1].x = ship.x
        bullets[-1].y = ship.y-50    

pgzrun.go()