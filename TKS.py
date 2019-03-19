import pygame
import time
import random 
from pygame.locals import *
pygame.init()

scwid,scht=800,600

gameDis=pygame.display
gameDis.set_caption("The Killer Space")
scr=gameDis.set_mode((scwid,scht))
timer=pygame.time.Clock()
bg=pygame.image.load("data\\assets\\bg.png")

#getting colors
bll=(0,0,0) #format: r,g,b
wht=(255,255,255)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)

ast=pygame.image.load("data\\assets\\ast.png")

def ast(x,y):
	scr.blit(ast,(x,y))

def scoreScr(scotxt):
	scotxt="[ YOU SCORED: "+scotxt+" ]"
	scscr=pygame.font.Font('C:\\Windows\\Fonts\\Arial.ttf',35).render(scotxt,True,blue)
	scr.blit(scscr,(0,0))
	
def level(lvl):
	scotxt="LEVEL "+str(lvl)
	scscr=pygame.font.Font('C:\\Windows\\Fonts\\Arial.ttf',45).render(scotxt,True,blue)
	scr.blit(scscr,(450,0))

def txt_S(tx,fnt):
	txsfc=fnt.render(tx,True,bll)
	return txsfc,txsfc.get_rect()
	
def msg_show(tx,ti):
	ltxt=pygame.font.Font('C:\\Windows\\Fonts\\Arial.ttf',115) #-> fnt
	txSr,txRe=txt_S(tx,ltxt)
	txRe.center=((scwid*0.5,scht*0.5))
	scr.blit(txSr,txRe)
	
	gameDis.update()
	
	time.sleep(ti)
	
	runGame(0,0,0,4,1)
	
def abort():
	msg_show("GAME Over",2)
	
def block(bx,by,bw,bh,col):
	pygame.draw.rect(scr,col,[bx,by,bw,bh])

def rx():
		return random.randrange(0,scwid)
		
def ry():
		return random.randrange(100,scwid-150)
		
def rectDrawer(col,xpos):
	pygame.draw.rect(scr,col,(xpos,400,100,40))
	
def imgLoc(x,y):
	scr.blit(datImg,(x,y)) #scr & gameDis arent the same; blit simply places the image at the specified loaction
	#note we're using scr not gameDis[its just short for pygame.display]
#x,y=scwid*0.5,scht*0.5

def credits():
	cre=pygame.image.load("data\\assets\\cre.png")
	scr.blit(cre,cre.get_rect())
	gameDis.update()
	time.sleep(2)
	scotxt="[ skrstv123@gmail.com ]"
	scscr=pygame.font.Font('C:\\Windows\\Fonts\\Arial.ttf',35).render(scotxt,True,blue)
	scr.blit(scscr,(0,0))
	gameDis.update()
	time.sleep(5)
	
	

def ufo(ufo,ux,uy):
	scr.blit(ufo,(ux,uy))	
	
def menu():
	o=0
	scr.fill(wht)
	scr.blit(bg,bg.get_rect())
	title=pygame.image.load("data\\assets\\title.png")
	scr.blit(title,title.get_rect())
	gameDis.update()
	time.sleep(4)
	scr.fill(wht)
	scr.blit(bg,bg.get_rect())
	
	while 1:
		
	
		#scr.fill(wht)
		surf=pygame.font.Font('C:\\Windows\\Fonts\\Arial.ttf',75).render("JUST THE MENU",True,green)
		recta=surf.get_rect()
		recta.center=((400,200))
		scr.blit(surf,recta)
		#gameDis.update()
	
		
		paktoc=pygame.font.Font('C:\\Windows\\Fonts\\Arial.ttf',45).render("press any key to continue",True,blue)
		scr.blit(paktoc,(120,500))
		
		moupos=pygame.mouse.get_pos()
		mx,my=moupos[0],moupos[1]
		
		rectDrawer(blue,120)
		rectDrawer(blue,600)
		
		if (mx>120 and mx<220) and (my>400 and my<440):
			rectDrawer(green,120)
			for evm in pygame.event.get():
				if evm.type==pygame.MOUSEBUTTONUP:
					runGame(0,0,0,4,1)
		elif (mx>600 and mx<700) and (my>400 and my<440):
			rectDrawer(red,600)
			for evm2 in pygame.event.get():
				if evm2.type==pygame.MOUSEBUTTONUP:
					pygame.quit()
					quit()
		
		start=pygame.font.Font('C:\\Windows\\Fonts\\Arial.ttf',25).render("START",True,wht)
		scr.blit(start,(130,408))
		
		quitt=pygame.font.Font('C:\\Windows\\Fonts\\Arial.ttf',25).render("QUIT",True,wht)
		scr.blit(quitt,(615,410))
		
		gameDis.update()
		timer.tick(60)
			
		for eve in pygame.event.get():
			if eve.type==pygame.KEYDOWN:
				runGame(0,0,0,4,1)


#importing ship's image
datImg=pygame.image.load("data\\assets\\ship.png")
ht,wd=150,150



		
def runGame(score,by,sby,bxvel,lvl):
	abrt=False
	x,y=325,220
	dx,dy=0,0
	
	#lvl=1
	validity,validator,validator2=True,True,True
	print(bxvel)
	if score>=10:
		validator=False
	if score>=20:
		validator2=False
	
	#score=0
	go=pygame.image.load("data\\assets\\go.png")
	brd=pygame.image.load("data\\assets\\brdr.png")
	gob=pygame.image.load("data\\assets\\bgo.png")
	ufo=pygame.image.load("data\\assets\\ufo.png")
	angali=pygame.image.load("data\\assets\\angali.png")
	lvlup=pygame.image.load("data\\assets\\lvlup.png")
	ufocrash=pygame.image.load("data\\assets\\crash.png")
	ast=pygame.image.load("data\\assets\\ast.png")
	freak=pygame.image.load("data\\assets\\jai.png")
	bebr=pygame.image.load("data\\assets\\bebr.png")
	
	#arguments for the block
	bx,sbx=rx(),rx()
	#bx=300
	#by,sby=0,0
	#bxvel=4
	bw=5
	bh=100
	
	#arguments for ufo
	ux=-100
	uy=ry()
	uvel=3
	
	#arguments for the meteor
	ax,ay=rx(),800
	avel=2
	
	while not abrt:
	
		
		
		
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				scr.fill(wht)
				scr.blit(bebr,(90,200))
				gameDis.update()
				time.sleep(2)
				pygame.quit()
				quit()
			#============================#
			#if event.type==pygame.KEYDOWN:
				#if event.key==pygame.K_Q:
					#abrt=True
				""" dx=-5
				elif event.key==pygame.K_RIGHT:
					dx=5
				elif event.key==pygame.K_UP:
					dy=-5
				elif event.key==pygame.K_DOWN:
					dy=5"""
					
			#print(event)
				
				
			if event.type==pygame.KEYUP:
				if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT or event.key==pygame.K_UP or event.key==pygame.K_DOWN:
					dx,dy=0,0
			
			#============================#
		hKeys=pygame.key.get_pressed()# it requires pygame.locals
		if hKeys[K_UP]:				  #or just with pygame, it should have been pygame.locals.K_UP
			y-=5
		if hKeys[K_DOWN]:
			y+=5
		if hKeys[K_LEFT]:
			x-=5
		if hKeys[K_RIGHT]:
			x+=5
			#==================#
			x+=dx
			y+=dy
			#==================#
			#print(event)
			
		
		#the boundary
		if x>scwid-wd or x<0 or y>scht-ht or y<0:
			#print("CROSSING BOUNDARY") 
			#abrt=True
			#abort()
			scr.blit(brd,brd.get_rect())
			gameDis.update()
			time.sleep(2)
			runGame(0,0,0,4,1)
			
			
		scr.fill((0,0,0))#fill function covers everything already present on the screen
		level(lvl)
		scr.blit(bg,bg.get_rect())
		
		
		imgLoc(x,y)  #so, if we draw the image before fill, we'll get nothing on the screen
		block(bx,by,bw,bh,green)
		block(sbx,sby,bw,bh,red)
		by+=bxvel
		sby+=bxvel
		
		
		#firing an ufo
		if lvl==2 and ux<900:
			scr.blit(ufo,(ux,uy))
			ux+=uvel
		
		if lvl==3 and ux<900:
			scr.blit(ufo,(ux,uy))
			ux+=(uvel-1)
		
		if ux>850:
			ux=-100 
			uy=ry()
		
		#following 'if' handles a crash with the ufo
		if ((uy-y)<=140 and (uy-y)>=-40) and (ux-x>=-100 and ux-x<=125):
			scr.blit(ufocrash,(285,230))
			gameDis.update()
			time.sleep(1)
			scr.blit(angali,(310,140))
			gameDis.update()
			time.sleep(1)
			scr.blit(gob,(scwid*0.2,scht*0.1))
			scr.blit(go,go.get_rect())
			gameDis.update()
			time.sleep(1)
			runGame(0,0,0,4,1)
		
		#firing a meteor
		if score>18:
			scr.blit(ast,(ax,ay))
			ay-=avel
		if ay<-70:
			ay=800
			
		#following 'if' handles a crash with the meteor	
		if ((ay-y)<=125 and (ay-y)>=-70) and (ax-x>=-45 and ax-x<=115):
			scr.blit(freak,(225,50))
			gameDis.update()
			time.sleep(2)
			scr.blit(gob,(scwid*0.2,scht*0.1))
			scr.blit(go,go.get_rect())
			gameDis.update()
			time.sleep(2)
			runGame(0,0,0,4,1)
			
		
		scoreScr(str(score))
		#following 'if' lines handles a crash with the blocks(or laser beams?)
		if (((y-by)<=85 and (y-by)>=-135) and (bx-x>=15 and bx-x<=130)) or (((y-sby)<=85 and (y-sby)>=-135) and (sbx-x>=15 and sbx-x<=130)):
			#abort()
			scr.blit(gob,(scwid*0.2,scht*0.1))
			scr.blit(go,go.get_rect())
			gameDis.update()
			time.sleep(2)
			runGame(0,0,0,4,1)
		#print(x,y)
		#print(bx,by,"box")
		
		#regenerating the beams,giving them both a new horizontal position,velocity(+1) and giving 1 of them a slightly different height
		if by>scht:
			sby=-scht
			bx,sbx,by=random.randrange(0,scwid),random.randrange(0,scwid),sby+random.randrange(-250,250)
			#print(by,sby)
			score+=1
			bxvel+=1
			#scotxt=str(score)
		
		lcheck=score//10
		#if lcheck==1 and (by<100 and sby<100):
		if (lcheck==1 and (by<100 and sby<100)) and validator:
			lvl=2
			scr.blit(lvlup,(280,220))
			gameDis.update()
			time.sleep(1)
			by,sby=-400,-400
			bxvel=6
			validator=False
			runGame(10,by,sby,bxvel,lvl)
			
		#elif lcheck==2 and (by<100 and sby<100):
		if (lcheck==2 and (by<100 and sby<100)) and validator2:
			lvl=3
			scr.blit(lvlup,(280,220))
			gameDis.update()
			time.sleep(1)
			by,sby=-400,-400
			bxvel=8
			validator2=False
			runGame(20,by,sby,bxvel,lvl)
			
			
		if score==35 and validity:
			validity=False
			credits()
			
			
		gameDis.update() 
		""" here we can also use gameDis.flip(), update() when used with a parameter updates
			only that specified part whereas flip instead updates whole screen"""
			
		timer.tick(60) #usage under doubt, but i think it was for fps, but then why its being used so?
		
			
menu()
runGame(0,0,0,4,1) #===========# THE GAME RUNS NOW #===========#

pygame.quit()
quit() #to end the pygame instance we're running

