from gamelib import*

game = Game(1000,500,"Fighter")
bk = Animation("images//background.png",8,game,1536/2,1472/4)
bk.resizeTo(game.width,game.height)


spiderstance = Animation("images//spiderstance.png",10,game,342/3,392/4,frate=4)
spiderwalk = Animation("images//spiderwalk.png",12,game,364/4,279/3,frate=4)
spiderkick = Animation("images//spiderkick.png",9,game,510/3,387/3,frate=3)
spiderpunch = Animation("images//spiderpunch.png",10,game,549/3,500/4,frate=3)
spidertrip = Animation("images//spiderlowkick.png",9,game,430/2,300/5,frate=3)
spiderelbow = Animation("images//spiderelbow.png",9,game,402/2,300/5,frate=3)

spiderx = 150
spidery= 410

spiderstatus = "stand"

venomstance = Animation("images//vstance.png",13,game,459/3,585/5,frate=4)
venomwalk = Animation("images//vwalk.png",10,game,453/3,488/4,frate=4)
venompunch = Animation("images//vpunch.png",4,game,216/1,468/4,frate=5)
venomheavy = Animation("images//vhardpunch.png",8,game,543/3,552/3,frate=2.5)
venomdef = Animation("images//venomdef.png",12,game,744/3,728/4,frate=2.5)

venomx = 800
venomy = 410

venomstatus = "vstand"

jumping_1 = False
jumping_2 = False
landed_1 = False
landed_2 = False
factor_1 = 1
factor_2 = 1

title = Image("images//title.png",game)
bk.move()
title.draw()
game.drawText("Press (SPACE) to play",350,340,Font(red,50,green))
game.update(1)
game.wait(K_SPACE)

gameover = Image("images//game over.jpg", game)
gameover.resizeTo(game.width,game.height)

spiderstance.health = 100
venomstance.health = 100

while not game.over:
    game.processInput()

    bk.move()
    spiderstance.health = 30
    venomstance.health = 30
    mouse.visible = False
    
    if keys.Pressed[K_a]:
        spiderstatus = "walkleft"
        spiderx -= 8
    elif keys.Pressed[K_d]:
        spiderstatus = "walkright"
        spiderx += 8
    elif keys.Pressed[K_k]:
        spiderstatus = "kick"
    elif keys.Pressed[K_j]:
        spiderstatus = "punch"
    elif keys.Pressed[K_u]:
        spiderstatus = "elbow"
    elif keys.Pressed[K_i]:
        spiderstatus = "trip"
    if not keys.Pressed[K_a] and not keys.Pressed[K_w] and not keys.Pressed[K_d] and not keys.Pressed[K_i] and not keys.Pressed[K_u] and not keys.Pressed[K_j] and not keys.Pressed[K_k]:
        spiderstatus = "stand"


    if spiderstatus == "walkleft":
        spiderwalk.x = spiderx
        spiderwalk.y = spidery
        spiderwalk.nextFrame()
    elif spiderstatus == "walkright":
        spiderwalk.x = spiderx
        spiderwalk.y = spidery
        spiderwalk.prevFrame()
    elif spiderstatus == "kick":
        spiderkick.moveTo(spiderx,spidery)
        spiderkick.draw()
    elif spiderstatus == "punch":
        spiderpunch.moveTo(spiderx,spidery)
        spiderpunch.draw()
    elif spiderstatus == "trip":
        spidertrip.moveTo(spiderx,spidery)
        spidertrip.draw()
    elif spiderstatus == "elbow":
        spiderelbow.moveTo(spiderx,spidery)
        spiderelbow.draw()    

    else:
        spiderstance.moveTo(spiderx,spidery)
        spiderstance.draw()

        
    if spiderstance.y >= 410:
        landed_1 = True

    if jumping_1:
        spiderstance.y -= 24 * factor_1
        factor_1 *= .93
        landed_1 = False
        if factor_1 < .18:
            jumping_1 = False
            factor_1 = 1

    if keys.Pressed[K_w] and landed_1 and not jumping_1:
        jumping_1 = True

    if not landed_1:
        spiderstance.y += 9
    
    if keys.Pressed[K_LEFT]:
        venomstatus = "vwalkleft"
        venomx -= 8
    elif keys.Pressed[K_RIGHT]:
        venomstatus = "vwalkright"
        venomx += 8
    elif keys.Pressed[K_n]:
        venomstatus = "vheavy"
    elif keys.Pressed[K_b]:
        venomstatus = "vpunch"
    elif keys.Pressed[K_m]:
        venomstatus = "vdefend"
    if not keys.Pressed[K_LEFT] and not keys.Pressed[K_RIGHT] and not keys.Pressed[K_n] and not keys.Pressed[K_b] and not keys.Pressed[K_m] and not keys.Pressed[K_UP]:
        venomstatus = "vstand"

    if venomstatus == "vwalkleft":
        venomwalk.x = venomx
        venomwalk.y = venomy
        venomwalk.nextFrame()
    elif venomstatus == "vwalkright":
        venomwalk.x = venomx
        venomwalk.y = venomy
        venomwalk.prevFrame()
    elif venomstatus == "vheavy":
        venomheavy.moveTo(venomx,venomy)
        venomheavy.draw()
    elif venomstatus == "vdefend":
        venomdef.moveTo(venomx,venomy)
        venomdef.draw()
    elif venomstatus == "vpunch":
        venompunch.moveTo(venomx,venomy)
        venompunch.draw()

    else:
        venomstance.moveTo(venomx,venomy)
        venomstance.draw()

    if venomwalk.y >= 410:
        landed_2 = True

    if jumping_2:
        venomwalk.y -= 24 * factor_2
        factor_2 *= .93
        landed_2 = False
        if factor_2 < .18:
            jumping_2 = False
            factor_2 = 1


    if keys.Pressed[K_UP] and landed_2 and not jumping_2:
        jumping_2 = True
        

    if not landed_2:
        venomwalk.y += 9

    if spiderpunch.collidedWith(venomstance):
        venomstance.health -= 10

    if spiderkick.collidedWith(venomstance):
        venomstance.health -= 13

    if spidertrip.collidedWith(venomstance):
        venomstance.health -= 12

    if spiderelbow.collidedWith(venomstance):
        venomstance.health -= 12

    if venompunch.collidedWith(spiderstance):
        spiderstance.health -= 13

    if venomheavy.collidedWith(spiderstance):
        spiderstance.health -= 15

    if venomdef.collidedWith(spiderstance):
        spiderstance.health -= 2

    if spiderstance.health < 0 or venomstance.health < 0:
        game.over = True
    
    game.drawText("VENOM: " + str(venomstance.health),5,5)
    game.drawText("SPIDER: " + str(spiderstance.health),115,5)
    
    game.update(20)

gameover.draw()
game.drawText("Press SPACE to end", 350,340)
game.update(1)
game.wait(K_SPACE)
game.quit()
