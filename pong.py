###########################################
# PONG PAR GABRIEL STIK ET MAXIME COUETTE #
###########################################

# -*- coding: utf-8 -*-

# Supporté par Python 3 et Python 2
# Python 2 est recommandé

try:
	from Tkinter import * # Python 3
except:
	from tkinter import * # Python 2
import random
try:
	import pygame # Python 3
	from pygame import mixer # Python 3
except:
	pass # Python 2
import time
import os

fichier_score = open("score.txt", "r") # on lit le score dans son fichier
hiscore = fichier_score.read() # puis on le met dans la variable hiscore
fichier_score.close()
precision = random.randint(1,140)-110 # INTRODUCTION DES VARIABLES ESSENTIELLES
vitesse = 10
yp1 = 270 # coordonnée verticale de la raquette 1
yp2 = 270 # coordonnée verticale de la raquette 2
xb = 80 # coordonnée horizontale de la balle
yb = 300 # coordonnée verticale de la balle
ab = 0 # coeficient directeur de la balle
pt1 = 0 # score du joueur 1
pt2 = 0 # score du joueur 2
multi = False # mode multijoueur activé ?
service = 2  # qui a le service
stop = True # si le jeu est en cours # FIN D'INTRODUCTION DES VARIABLES ESSENTIELLES

def clear(): # lorsqu'on a besoin d'effacer un groupe d'élément de l'interface
	can.delete(menu)
	can.delete(easy1)
	can.delete(regular1)
	can.delete(hard1)
	can.delete(easy2)
	can.delete(regular2)
	can.delete(hard2)
	can.delete(singleplayer)
	can.delete(multiplayer)
	can.delete(best)
	can.delete(controls)
	can.delete(spcmd)
	can.delete(mpcmd)
	can.delete(best)
	can.delete(spc)

def perdu(): # lorsqu'on perd en mode hardcore ou qu'on appuie sur echap
	global menu, singleplayer, multiplayer, balle, easy1, easy2, regular1, regular2, hard1, hard2, score1, score2, player1, player2, pt1, pt2, stop, yp1, yp2, xb, yb, ab, service, controls, spcmd, mpcmd, best, spc # les variables communes au programme principal
	yp1 = 270
	yp2 = 270
	xb = 80
	yb = 300
	ab = 0
	pt1 = 0
	pt2 = 0
	multi = False
	service = 2
	stop = True
	menu = can.create_rectangle(170,155,630,500, fill="black", outline="white") # ON REMET LES ELEMENTS DU MENU EN PLACE
	controls = can.create_text(400,410, text="controls :", fill="white", font=("Courier",24))
	spc = can.create_text(400,440, text="service: spacebar", fill="white", font=("Courier",16))
	spcmd = can.create_text(280,462, text="P1: up/down: arrows", fill="white", font=("Courier",16))
	mpcmd = can.create_text(520,470, text="P1: up/down: z/s\nP2: up/down: arrows", fill="white", font=("Courier",16))
	singleplayer = can.create_text(280,180, text="singleplayer", fill="white", font=("Courier",24))
	multiplayer = can.create_text(520,180, text="multiplayer", fill="white", font=("Courier",24))
	easy1 = can.create_text(280,250, text="easy (W)", fill="white", font=("Courier",24))
	easy2 = can.create_text(520,250, text="easy (V)", fill="white", font=("Courier",24))
	regular1 = can.create_text(280,300, text="regular (X)", fill="white", font=("Courier",24))
	regular2 = can.create_text(520,300, text="regular (B)", fill="white", font=("Courier",24))
	hard1 = can.create_text(280,350, text="hardcore (C)", fill="white", font=("Courier",24))
	hard2 = can.create_text(520,350, text="hard (N)", fill="white", font=("Courier",24))
	can.delete(player1) # ON SUPPRIME LES ELEMENTS DE JEU POUR LES REINITIALSIER PROPREMENT
	can.delete(player2)
	can.delete(score1)
	can.delete(score2)
	can.delete(balle)
	can.delete(best)
	score1 = can.create_text(300,100, text=pt1, fill="white", font=("Courier",80)) # ON REPLACE LES ELEMENTS DE JEUX
	score2 = can.create_text(500,100, text=pt2, fill="white", font=("Courier",80))
	balle = can.create_rectangle(xb,yb,xb+20,yb+20, fill="white")
	player1 = can.create_rectangle(20,yp1,40,yp1+80, fill="white")
	player2 = can.create_rectangle(760,yp2,780,yp2+80, fill="white")
	fichier_score = open("score.txt", "r") # ON ACTUALISE LA VARIABLE HISCORE
	hiscore = fichier_score.read()
	fichier_score.close()
	best = can.create_text(280,370, text="best: "+str(hiscore), fill="white", font=("Courier",14))

def echap(event): # si on appuie sur echap, on lance perdu()
	perdu()

def se(event): # singleplayer easy
	global vitesse, precision, ab, controls, hardcore
	hardcore = False
	root.bind("<space>",go) # on active les touches corespondantes
	root.bind("<Escape>",echap)
	root.bind("<Up>",monter1)
	root.bind("<Down>",descendre1)
	vitesse = 5 # vitesse variable selon le mode
	precision = random.randint(1,100)-50
	ab = random.randint(1,20)-10 # angle variable selon le mode
	clear()

def sr(event):
	global vitesse, precision, ab, hardcore
	hardcore = False
	root.bind("<space>",go)
	root.bind("<Escape>",echap)
	root.bind("<Up>",monter1)
	root.bind("<Down>",descendre1)
	vitesse = 10
	precision = random.randint(1,100)-50
	ab = random.randint(1,30)-15
	clear()

def sh(event):
	global vitesse, precision, ab, hardcore
	hardcore = True
	root.bind("<space>",go)
	root.bind("<Escape>",echap)
	root.bind("<Up>",monter1)
	root.bind("<Down>",descendre1)
	vitesse = 15
	precision = random.randint(1,100)-50
	ab = random.randint(1,40)-20
	clear()

def me(event):
	global vitesse, multi, precision, ab, hardcore
	hardcore = False
	root.bind("<space>",go)
	root.bind("<Escape>",echap)
	multi = True
	root.bind("<z>",monter1)
	root.bind("<s>",descendre1), ab
	root.bind("<Up>",monter2)
	root.bind("<Down>",descendre2)
	vitesse = 5
	precision = random.randint(1,100)-50
	ab = random.randint(1,20)-10
	clear()

def mr(event):
	global vitesse, multi, precision, ab, hardcore
	hardcore = False
	root.bind("<space>",go)
	root.bind("<Escape>",echap)
	multi = True
	root.bind("<z>",monter1)
	root.bind("<s>",descendre1), ab
	root.bind("<Up>",monter2)
	root.bind("<Down>",descendre2)
	vitesse = 10
	precision = random.randint(1,100)-50
	ab = random.randint(1,30)-15
	clear()

def mh(event):
	global vitesse, multi, precision, ab, hardcore
	hardcore = False
	root.bind("<space>",go)
	root.bind("<Escape>",echap)
	multi = True
	root.bind("<z>",monter1)
	root.bind("<s>",descendre1), ab
	root.bind("<Up>",monter2)
	root.bind("<Down>",descendre2)
	vitesse = 15
	precision = random.randint(1,100)-50
	ab = random.randint(1,40)-20
	clear()

def bot(): # jeu de l'ordinateur
	global balle, yp1, yp2, xb, yb, ab, pt1, player1, player2, score1, pt2, score2, precision
	yp2 = yb+precision # la precision de l'ordinateur à chaque touche
	if yp2 > 60 and yp2 < 480:
		can.coords(player2, 760,yp2,780,yp2+80) # il se déplace
	root.after(50,bot) # boucle qui s'actualise toute les 50ms

def mdroite(): # mouvement de la baller vers la droite
	global balle, yp1, yp2, xb, yb, ab, pt1, player1, player2, score1, pt2, score2, precision, vitesse, service, stop
	if stop == False: # si la partie est en cours
		xb += vitesse
		yb += ab # on ajoute l'angle aux coordonnées verticles
		can.delete(balle)
		balle = can.create_rectangle(xb,yb,xb+20,yb+20, fill="white")
		if yb >= 560: # si la balle atteint le mur du bas
			ab = 0-ab # on inverse son sens
			try:
				mixer.init() # on joue un son
				mixer.music.load('poc.mp3')
				mixer.music.play()
			except:
				pass
		if yb <= 40: # si la balle atteint le mur du haut
			ab = 0-ab
			try:
				mixer.init()
				mixer.music.load('poc.mp3')
				mixer.music.play()
			except:
				pass
		if xb >= 740 and yb-45 <= yp2+40 <= yb+45: # si la balle et la raquette entrent en contact
			ab = random.randint(1,20)-10
			try:
				mixer.init()
				mixer.music.load('pac.mp3')
				mixer.music.play()
			except:
				pass
			mgauche() # on change de sens
		else: # sinon on marque un point et on réinitialise le jeu
			if xb >= 800:
				yp1 = 270
				yp2 = 270
				xb = 720
				yb = 300
				ab = 0
				pt1 += 1
				service = 1
				can.delete(balle)
				can.delete(player1)
				can.delete(player2)
				can.delete(score1)
				can.delete(score2)
				score1 = can.create_text(300,100, text=pt1, fill="white", font=("Courier",80))
				score2 = can.create_text(500,100, text=pt2, fill="white", font=("Courier",80))
				balle = can.create_rectangle(xb,yb,xb+20,yb+20, fill="white")
				player1 = can.create_rectangle(20,yp1,40,yp1+80, fill="white")
				player2 = can.create_rectangle(760,yp2,780,yp2+80, fill="white")
				try:
					mixer.init()
					mixer.music.load('gol.mp3')
					mixer.music.play()
				except:
					pass
			else:
				root.after(20,mdroite)

def mgauche(): # idem que pour mdroite()
	global balle, yp1, yp2, xb, yb, ab, pt1, player1, player2, score1, pt2, score2, precision, vitesse, service, stop, hardcore, hiscore, fichier_score
	if stop == False:
		xb -= vitesse
		yb += ab
		can.coords(balle, xb,yb,xb+20,yb+20)
		if yb >= 560:
			ab = 0-ab
			try:
				mixer.init()
				mixer.music.load('pac.mp3')
				mixer.music.play()
			except:
				pass
		if yb <= 40:
			ab = 0-ab
			try:
				mixer.init()
				mixer.music.load('pac.mp3')
				mixer.music.play()
			except:
				pass
		if xb <= 40 and yb-45 <= yp1+40 <= yb+45:
			ab = random.randint(1,20)-10
			precision = random.randint(1,140)-110
			try:
				mixer.init()
				mixer.music.load('poc.mp3')
				mixer.music.play()
			except:
				pass
			mdroite()
		else:
			if xb <= -20:
				if hardcore == True:
					if pt1 >= int(hiscore):
						fichier_score = open("score.txt", "w")
						fichier_score.write(str(pt1))
						fichier_score.close()
					perdu()
				else:
					yp1 = 270
					yp2 = 270
					xb = 80
					yb = 300
					ab = 0
					pt2 += 1
					service = 2
					can.delete(balle)
					can.delete(player1)
					can.delete(player2)
					can.delete(score1)
					can.delete(score2)
					score1 = can.create_text(300,100, text=pt1, fill="white", font=("Courier",80))
					score2 = can.create_text(500,100, text=pt2, fill="white", font=("Courier",80))
					balle = can.create_rectangle(xb,yb,xb+20,yb+20, fill="white")
					player1 = can.create_rectangle(20,yp1,40,yp1+80, fill="white")
					player2 = can.create_rectangle(760,yp2,780,yp2+80, fill="white")
					try:
						mixer.init()
						mixer.music.load('gol.mp3')
						mixer.music.play()
					except:
						pass
			else:
				root.after(20,mgauche)

def go(event): # lorsqu'on appuie sur espace, on démarre la partie
	global balle, player1, player2, yp1, yp2, xb, yb, ab, service, stop
	if multi == False:
		bot()
	if service == 1:
		stop = False
		mgauche()
	if service == 2:
		stop = False
		mdroite()

def monter1(event): # on enlève 20px pour monter
	global player1, yp1
	if yp1 > 60:
		yp1 -= 20
		can.coords(player1, 20,yp1,40,yp1+80)

def descendre1(event): # on ajoute 20px pour descendre
	global player1, yp1
	if yp1 < 480:
		yp1 += 20
		can.coords(player1, 20,yp1,40,yp1+80)

def monter2(event):
	global player2, yp2
	if yp2 > 60:
		yp2 -= 20
		can.coords(player2, 760,yp2,780,yp2+80)

def descendre2(event):
	global player2, yp2
	if yp2 < 480:
		yp2 += 20
		can.coords(player2,760,yp2,780,yp2+80)

root = Tk() # AFFICHAGE DE LA FENETREE ET DE TOUTES SES DONNÉES
root.title("PONG")
can = Canvas(root, width=800, height=620, highlightthickness=0, bg="black")
can.pack()
can.create_rectangle(20,20,780,40, fill="white") # Mur du haut
can.create_rectangle(20,580,780,600, fill="white") # Mur du bas
can.create_rectangle(390,60,410,80, fill="white") # DEBUT POINTILLÉS
can.create_rectangle(390,100,410,120, fill="white")
can.create_rectangle(390,140,410,160, fill="white")
can.create_rectangle(390,180,410,200, fill="white")
can.create_rectangle(390,220,410,240, fill="white")
can.create_rectangle(390,260,410,280, fill="white")
can.create_rectangle(390,300,410,320, fill="white")
can.create_rectangle(390,340,410,360, fill="white")
can.create_rectangle(390,380,410,400, fill="white")
can.create_rectangle(390,420,410,440, fill="white")
can.create_rectangle(390,460,410,480, fill="white")
can.create_rectangle(390,460,410,480, fill="white")
can.create_rectangle(390,500,410,520, fill="white")
can.create_rectangle(390,540,410,560, fill="white") # FIN POINTILLÉS
score1 = can.create_text(300,100, text=pt1, fill="white", font=("Courier",80)) # Score joueur 1
score2 = can.create_text(500,100, text=pt2, fill="white", font=("Courier",80)) # Score joueur 2
balle = can.create_rectangle(xb,yb,xb+20,yb+20, fill="white") # Balle
player1 = can.create_rectangle(20,yp1,40,yp1+80, fill="white") # Raquette joueur 1
player2 = can.create_rectangle(760,yp2,780,yp2+80, fill="white") # Raquette joueur 2
menu = can.create_rectangle(170,155,630,500, fill="black", outline="white")
singleplayer = can.create_text(280,180, text="singleplayer", fill="white", font=("Courier",24))
multiplayer = can.create_text(520,180, text="multiplayer", fill="white", font=("Courier",24))
easy1 = can.create_text(280,250, text="easy (W)", fill="white", font=("Courier",24))
easy2 = can.create_text(520,250, text="easy (V)", fill="white", font=("Courier",24))
regular1 = can.create_text(280,300, text="regular (X)", fill="white", font=("Courier",24))
regular2 = can.create_text(520,300, text="regular (B)", fill="white", font=("Courier",24))
hard1 = can.create_text(280,350, text="hardcore (C)", fill="white", font=("Courier",24))
best = can.create_text(280,370, text="best: "+str(hiscore), fill="white", font=("Courier",14))
hard2 = can.create_text(520,350, text="hard (N)", fill="white", font=("Courier",24))
controls = can.create_text(400,410, text="controls :", fill="white", font=("Courier",24))
spc = can.create_text(400,440, text="service: spacebar", fill="white", font=("Courier",16))
spcmd = can.create_text(280,462, text="P1: up/down: arrows", fill="white", font=("Courier",16))
mpcmd = can.create_text(520,470, text="P1: up/down: z/s\nP2: up/down: arrows", fill="white", font=("Courier",16))
root.bind("<w>",se) # touches à utiliser
root.bind("<x>",sr)
root.bind("<c>",sh)
root.bind("<v>",me)
root.bind("<b>",mr)
root.bind("<n>",mh)
root = mainloop()
