from sense_hat import SenseHat
import time
import pygame
pygame.init()
pygame.display.set_mode()
s = SenseHat()
s.low_light = True
green = (0, 255, 0)
lightgreen = (46, 160, 20)
yellow = (255, 255, 0)
blue = (0, 0, 0255)
red = (255, 0, 0)
white = (255,255,255)
nothing = (0,0,0)
pink = (255,105, 180)
purple = (185, 66, 244)
bluee = (109, 221, 249)
pinkk = (229, 99, 147)
black = (17, 13, 13)
brown = (175, 118, 61)
brownlight = (232, 225, 196)
pin = ( 242, 162, 162)
lightbrown = (238,227,214)
thatblue = (69,135,160)
espblue = (27, 164, 189)
orange = (198, 129, 39)



R = red
W = white
O = nothing
B= black
Y= yellow
P = pink
L = bluee
N= orange
X = pinkk
PP = purple
V = brown
VV = brownlight
PI  = pin
A = lightbrown
C = thatblue
M = espblue
Z= lightgreen
G = green

one = "Lejos!"
two = "Medio lejos!"
three = "Medio cerca!"
four = "Cerca!"



poke1 = [
	B, B, O, O, O, O, B, B,
	O, B, B, O, O, B,  B, O,
	O, Y, B, Y,  Y,  B,  Y,  O,
	O, Y,  Y, Y,  Y,  Y,  Y,  O,
	Y, Y, Y, B,  Y,  B,  Y,  Y,
	Y, Y , Y, Y,  Y,  Y,  Y,  Y,
	Y, Y,  R,  Y,  P, Y,  R, Y,
	O, Y, Y,  Y,  Y,  Y,  Y, O,
	]
	
poke2 = [
	O, O, L, L, L, L, O, O,
	O,  L, L, L, L, L, L, O,
	L, L, X, L, L, X, L, L,
	L, L, L, L, L, L, L, L,
	L, L, L, L, L, L, L, L,
	L, L, B, L, L, B, L, L,
	O, L, L, B, B, L, L, O,
	O, O, L, L, L, L, O, O,
	]

poke3 = [
	O, PP, PP, O, O, PP, PP, O,
	O, PP,P , P, P, P, PP, O,
	O, P, P, P, P, P, P, O,
	O, P, R, P, P, R, P, O,
	O, P, P, P, P, P, P, O,
	O, P, P, B, B, P, P, O,
	O, P, P, P, P, P, P, O,
	O, O, O, O, O, O, O, O,
	]

poke4 = [
	V, O, O, O, O, O, O, V,
	O, V, O, O, O, O, V, O,
	O, V, V, V, V, V, O, O,
	O, V, B, V, B, V, O, O,
	O, V, V, V, V, V, O, O,
	O, V, V, B, V, V, O, O,
	O, VV, V, V, VV, O, O, O,
	O, O, VV, VV, VV, O, O, O,
	]



poke5 = [
	PI, PI, O, O, O, O, PI , PI,
	PI, PI, PI, PI, PI, PI, PI, PI,
	O, PI, M, PI, PI, M, PI, O,
	O, PI, M, PI, PI, M, PI, O,
	O, PI, PI, PI, PI, PI, PI, O,
	O, PI, PI, PI, PI, PI, PI, O,
	O, PI, PI, PI, PI, PI, PI, O,
	O, O, O, O, O, O, O, O,
	]

poke6 = [
	C, C, C, C, C, C, C, C,
	C, A, A, C, C, A, A, C,
	C, A, A, A, A, A, A, C,
	C, R, O, R, R, O, R, C,
	C, R, O, R, R, O, R, C,
	C, R, R, R, R, R, R, C,
	C, R, R, R, R, R, R, C,
	C, R, O, R, R, O, R, C,
	]

poke7 = [
  O, O, Z, O, O, Z, O, O,
	V,  Z, V, Z,  Z,  V, Z, V,
	O, Z, Z, Y, Y, Z, Z, O,
	O, V,  Y, B, B, Y, V, O,
	V, V, Z, Y,  Y,  Z, V, V,
	O, V , N, N, N, N, V, O,
	O, Z, Z, N, N, Z, Z, O,
	O, O, Z, Z , Z,  Z, O, O,
	]

lejos = [
  G, G, G, G, G, G, G, G,
  G, G, G, G, G, G, G, G,
  O, O, O, O, O, O, O, O,
  O, O, O, O, O, O, O, O,
  O, O, O, O, O, O, O, O,
  O, O, O, O, O, O, O, O,
  O, O, O, O, O, O, O, O,
  O, O, O, O, O, O, O, O,
    ]

mediolejos = [
  O, O, O, O, O, O, O, O, 
  O, O, O, O, O, O, O, O,
  Y, Y, Y, Y, Y, Y, Y, Y, 
  Y, Y, Y, Y, Y, Y, Y, Y,
  O, O, O, O, O, O, O, O,
  O, O, O, O, O, O, O, O,
  O, O, O, O, O, O, O, O,
  O, O, O, O, O, O, O, O,
    ]

mediocerca = [
  O, O, O, O, O, O, O, O, 
  O, O, O, O, O, O, O, O,
  O, O, O, O, O, O, O, O, 
  O, O, O, O, O, O, O, O,
  N, N, N, N, N, N, N, N,
  N, N, N, N, N, N, N, N,
  O, O, O, O, O, O, O, O,
  O, O, O, O, O, O, O, O,
    ]

cerca = [
  O, O, O, O, O, O, O, O, 
  O, O, O, O, O, O, O, O,
  O, O, O, O, O, O, O, O,
  O, O, O, O, O, O, O, O,
  O, O, O, O, O, O, O, O,
  O, O, O, O, O, O, O, O,
  R, R, R, R, R, R, R, R,
  R, R, R, R, R, R, R, R,
    ]


#poke1 = pikachu
#poke2 = squirtle
#poke3 = gengar
#poke4 = eevee
#poke5 = mewtwo
#poke6 = snorlax
#poke7 = grookey






import random 
import time
import pygame
pygame.init()
pygame.display.set_mode()
lista = []
poke = nothing




while True:
  msg1= "Pikachu"
  msg2= "Mewtwo"
  msg3= "Snorlax"
  p = random.randint(0,8)
  l = random.randint(1,100)

#print(“Press 0 to initialize game.”)  

  for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); #sys.exit() if sys is imported
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_0:
                print("Hey, you have just initialized this amazing game, press 1 to start. Each time you press 1, is a attempt to catch a Pokemon. Catch as many as you can! To access the Pokemon you have trapped, press 8. If the game is being laggy after an attempt or after you consult your Pokemon list, just click on the Sense Hat machine to refresh the page.")
                s.set_pixels(poke2)
            if event.key == pygame.K_1:
              if p == 1:
                s.set_pixels(poke1)
                time.sleep(2)
                s.set_pixels(cerca)
                time.sleep(2)
                poke = poke1
                lista.append(msg1)
                print("Excellent, you trapped a Pokemon!")
                
              elif p == 2:
                s.set_pixels(poke2)
                time.sleep(2)
                s.set_pixels(mediocerca)
                time.sleep(2)
                poke = poke2
                print("You were close! Try again")
              
              
              elif p == 3:
                s.set_pixels(poke3)
                time.sleep(2)
                s.set_pixels(mediolejos)
                time.sleep(2)
                poke = poke3
                print("You missed by a little bit, try again")                

              elif p == 4:
                s.set_pixels(poke4)
                time.sleep(2)
                s.set_pixels(lejos)
                time.sleep(2)
                poke = poke4
                print("You weren’t close at all, try again")                

              elif p == 5:
                s.set_pixels(poke5)
                time.sleep(2)
                s.set_pixels(cerca)
                time.sleep(2)
                poke = poke5
                lista.append(msg2)
                print("Excellent, you trapped a Pokemon!")               

              elif p == 6:
                s.set_pixels(poke6)
                time.sleep(2)
                s.set_pixels(cerca)
                time.sleep(2)
                poke = poke6
                lista.append(msg3)
                print("Excellent, you trapped a Pokemon!")                

              elif p == 7:
                s.set_pixels(poke7)
                time.sleep(2)
                s.set_pixels(mediocerca)
                time.sleep(2)
                poke = poke7
                print("You missed by a little bit, try again")                
              
              time.sleep(2)
              
              
              if (l <= 76 and l >= 100):
                s.set_pixels(lejos)
                time.sleep(1)
                s.show_message(str(one) , scroll_speed=0.5, back_colour = nothing)

              elif (l <= 51 and l >= 75):
                s.set_pixels(mediolejos)
                time.sleep(1)
                s.show_message(str(two) , scroll_speed=0.5, back_colour = nothing)

              elif (l <= 26 and l >= 50):
                s.set_pixels(mediocerca)
                time.sleep(1)
                s.show_message(str(three) , scroll_speed=0.5, back_colour = nothing)
               
                
              elif (l<=0 and l<25):
                s.set_pixels(cerca)
                time.sleep(1)
                s.show_message(str(four) , scroll_speed=0.5, back_colour = nothing)
                lista.append(poke)
                
              #time.sleep(2)
                
            if event.key == pygame.K_8:
              print("Hey! These are the Pokemon you have trapped: "+ str (lista))
