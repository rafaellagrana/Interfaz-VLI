import turtle
from math import *
from library import *
#from writer import *

#crear unna tortuga llamada turtle
turtle=turtle

#esconder tortuga
turtle.ht()

#Velocidad 1 min 10 max
turtle.speed(9)

#abrir el file a leer y llamarlo f
f=open("/Users/rafaella/Documents/Interfaz VLI/probando.txt","r")
#guardar en s el string de todo el file
s=f.read()

pt=40
posx= -250
posy= 300
out=[]

#def sim():
for count in range(len(s)):
    x=s[count]
    if x==' ':
        x='space'
    elif x=='\n':
        x='backslash'
    out.extend(eval(x)(pt,posx,posy,turtle)) #esta es la funcion que llama a la libreria
    out.extend(noescribir(turtle.xcor(),turtle.ycor(),turtle.xcor()+0.2*pt,turtle.ycor(),turtle))

    posx=turtle.xcor()
    posy=turtle.ycor()

print out
#sim()

#def esc():
#    while x==1:
#        f.write(recopilar(turtle))
#        time.sleep(.500)
