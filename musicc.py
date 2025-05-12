import turtle
import pygame
import os
import sys  

# Initialize pygame mixer
pygame.mixer.init()

# Initialize screen
screen = turtle.Screen()
screen.bgcolor("gray30")
screen.setup(width=1000, height=600)
screen.title("MUSIC+")

# Create piano keys
def draw_rectangle(x, y, height, width, color):  
    turtle.penup()  
    turtle.goto(x, y)  
    turtle.pendown()  
    turtle.fillcolor(color)  
    turtle.begin_fill()           
    for _ in range(2):  
        turtle.forward(width)  
        turtle.right(90)  
        turtle.forward(height)  
        turtle.right(90)  
    turtle.end_fill()      
    turtle.speed(100)      
    turtle.hideturtle()
# رسم مستطیل اول (47 در 157)  


# فاصله دادن تا مستطیل بعدی (مثلاً کمی کنار)  

# رسم مستطیل دوم (25 در 109)  


# White keys 
white_keys_positions = [-385, -330, -275, -220, -165, -110, -55, 0, 55, 110, 165, 220, 275, 330]  
for x in white_keys_positions:  
    draw_rectangle(x, 37, 157, 47, "#D9D9D9")  

# black keys 
black_keys_positions = [-350, -287, -180, -151+25, -117+45, -350+385, -287+385, -160+365, -151+385+25, -117+385+45]  
for x in black_keys_positions:  
    draw_rectangle(x, 37, 109, 25, "#323731")  



# Sound functions
def load_sound(filename):
    try:
        sound = pygame.mixer.Sound(filename)
        return sound
    except:
        print(f"Error loading sound file: {filename}")
        return None

# Load sounds
sounds = {
    'C4': load_sound('./C4.mp3'),
    'D4': load_sound('./D4.mp3'),
    'Db4': load_sound('./Db4.mp3'),
    'E4': load_sound('./E4.mp3'),
    'Eb4': load_sound('./Eb4.mp3'),
    'F4': load_sound('./F4.mp3'),
    'G4': load_sound('./G4.mp3'),
    'Gb4': load_sound('./Gb4.mp3'),
    'A4': load_sound('./A4.mp3'),
    'Ab4': load_sound('./Ab4.mp3'),
    'B4': load_sound('./B4.mp3'),
    'Bb4': load_sound('./Bb4.mp3'),
    'C5': load_sound('./C5.mp3'),
    'D5': load_sound('./D5.mp3'),
    'Db5': load_sound('./Db5.mp3'),
    'E5': load_sound('./E5.mp3'),
    'Eb5': load_sound('./Eb5.mp3'),
    'F5': load_sound('./F5.mp3'),
    'G5': load_sound('./G5.mp3'),
    'Gb5': load_sound('./Gb5.mp3'),
    'A5': load_sound('./A5.mp3'),
    'Ab5': load_sound('./Ab5.mp3'),
    'B5': load_sound('./B5.mp3'),
    'Bb5': load_sound('./Bb5.mp3')    
}

def play_sound(note):
    sound = sounds.get(note)
    if sound:
        sound.play()

# Key bindings
screen.onkeypress(lambda: play_sound('C5'), "z")
screen.onkeypress(lambda: play_sound('C5'), "Z")
screen.onkeypress(lambda: play_sound('D5'), "x")
screen.onkeypress(lambda: play_sound('D5'), "X")
screen.onkeypress(lambda: play_sound('Db5'), "s")
screen.onkeypress(lambda: play_sound('Db5'), "S")
screen.onkeypress(lambda: play_sound('E5'), "c")
screen.onkeypress(lambda: play_sound('E5'), "C")
screen.onkeypress(lambda: play_sound('Eb5'), "d")
screen.onkeypress(lambda: play_sound('Eb5'), "D")
screen.onkeypress(lambda: play_sound('F5'), "v")
screen.onkeypress(lambda: play_sound('F5'), "V")
screen.onkeypress(lambda: play_sound('G5'), "b")
screen.onkeypress(lambda: play_sound('G5'), "B")
screen.onkeypress(lambda: play_sound('Gb5'), "g")
screen.onkeypress(lambda: play_sound('Gb5'), "G")
screen.onkeypress(lambda: play_sound('A5'), "n")
screen.onkeypress(lambda: play_sound('A5'), "N")
screen.onkeypress(lambda: play_sound('Ab5'), "h")
screen.onkeypress(lambda: play_sound('Ab5'), "H")
screen.onkeypress(lambda: play_sound('B5'), "m")
screen.onkeypress(lambda: play_sound('B5'), "M")
screen.onkeypress(lambda: play_sound('Bb5'), "j")
screen.onkeypress(lambda: play_sound('Bb5'), "J")

screen.onkeypress(lambda: play_sound('C4'), "q")
screen.onkeypress(lambda: play_sound('C4'), "Q")
screen.onkeypress(lambda: play_sound('D4'), "w")
screen.onkeypress(lambda: play_sound('D4'), "W")
screen.onkeypress(lambda: play_sound('Db4'), "2")
screen.onkeypress(lambda: play_sound('Db4'), "2")
screen.onkeypress(lambda: play_sound('E4'), "e")
screen.onkeypress(lambda: play_sound('E4'), "E")
screen.onkeypress(lambda: play_sound('Eb4'), "3")
screen.onkeypress(lambda: play_sound('Eb4'), "3")
screen.onkeypress(lambda: play_sound('F4'), "r")
screen.onkeypress(lambda: play_sound('F4'), "R")
screen.onkeypress(lambda: play_sound('G4'), "t")
screen.onkeypress(lambda: play_sound('G4'), "T")
screen.onkeypress(lambda: play_sound('Gb4'), "5")
screen.onkeypress(lambda: play_sound('Gb4'), "5")
screen.onkeypress(lambda: play_sound('A4'), "y")
screen.onkeypress(lambda: play_sound('A4'), "Y")
screen.onkeypress(lambda: play_sound('Ab4'), "6")
screen.onkeypress(lambda: play_sound('Ab4'), "6")
screen.onkeypress(lambda: play_sound('B4'), "u")
screen.onkeypress(lambda: play_sound('B4'), "U")
screen.onkeypress(lambda: play_sound('Bb4'), "7")
screen.onkeypress(lambda: play_sound('Bb4'), "7")



# write keys on keys!
def write_key_white(x, y):
    key = turtle.Turtle()
    key.hideturtle()
    key.penup()
    key.goto(x,-110)
    key.color("#323731")
    key.write(y ,font=("Bookman Old Style", 24, "bold"))
    
def write_key_black(x, y):
    key = turtle.Turtle()
    key.hideturtle()
    key.penup()
    key.goto(x,-60)
    key.color("#FAF3F0")
    key.write(y ,font=("Bookman Old Style", 20, "bold"))






write_key_white(-371,"q")
write_key_white(-316,"w")
write_key_white(-258,"e")
write_key_white(-203,"r")
write_key_white(-148,"t")
write_key_white(-95,"y")
write_key_white(-40-5,"u")

write_key_white(15,"z")
write_key_white(70-1,"x")
write_key_white(125,"c")
write_key_white(180+2,"v")
write_key_white(235,"b")
write_key_white(290,"n")
write_key_white(343-3,"m")



write_key_black(-343-1, "2")
write_key_black(-281-1, "3")
write_key_black(-281+105+1, "5")
write_key_black(-281+105+1+54, "6")
write_key_black(-281+105+1+54+54, "7")

write_key_black(-281+105+1+54+54+107+2-1, "s")
write_key_black(-281+105+1+54+54+107+2+62-1, "d")
write_key_black(-281+105+1+54+54+107+2+62-1+107, "g")
write_key_black(-281+105+1+54+54+107+2+62-1+107+54, "h")
write_key_black(-281+105+1+54+54+107+2+62-1+107+54+54+2+2+2, "j")






# Create info panel
panel = turtle.Turtle()
panel.speed(0)
panel.penup()
panel.goto(0, 200)
panel.shape("square")
panel.shapesize(stretch_len=46, stretch_wid=9)
panel.color("#5244a8")

# Create text labels
def create_label(x, y, text):
    label = turtle.Turtle()
    label.speed(0)
    label.hideturtle()
    label.penup()
    label.goto(x, y)
    label.color("white")
    return label

title = create_label(-50, 250, "")
title.write("PIANO TUTORIAL KEYS", align="center", font=("impact", 20))

key_bindings = [
    ("q", "C5"), ("w", "D5"), ("2", "Db5"), ("e", "E5"),
    ("3 -> Eb5"), ("r -> F5"), ("t -> G5"), ("5 -> Gb5"),
    ("y -> A5"), ("6 -> Ab5"), ("u -> B5"), ("7 -> Bb5"),
    ("z", "C4"), ("x", "D4"), ("s", "Db4"), ("c", "E4"),
    ("d -> Eb4"), ("v -> F4"), ("b -> G4"), ("g -> Gb4"),
    ("n -> A4"), ("h -> Ab4"), ("m -> B4"), ("j -> Bb4")
]

def write_text_up(x, y):  
    label3 = turtle.Turtle()
    label3.hideturtle()
    label3.penup()
    label3.goto(x,200)
    label3.color("white")
    label3.write(y ,font=("Bookman Old Style", 11))
    
    
def write_text_down(x, y):  
    label3 = turtle.Turtle()
    label3.hideturtle()
    label3.penup()
    label3.goto(x,150)
    label3.color("white")
    label3.write(y ,font=("Bookman Old Style", 11))
    


write_text_up(-450+10+20, "z -> C4")
write_text_up(-390+10+20+5, "x -> D4")
write_text_up(-325+10+20+5+5, "s -> Db4")
write_text_up(-255+10+20+5+5+5, "c -> E4")
write_text_up(-190+10+20+5+5+5+5, "d -> Eb4")
write_text_up(-120+10+20+5+5+5+5+5, "v -> F4")
write_text_up(-60+10+20+5+5+5+5+5+5, "b -> G4")
write_text_up(0+10+20+5+5+5+5+5+5+5, "g -> Gb4")
write_text_up(70+10+20+5+5+5+5+5+5+5+5, "n -> A4")
write_text_up(130+10+20+5+5+5+5+5+5+5+5+5, "h -> Ab5")
write_text_up(200+10+20+5+5+5+5+5+5+5+5+5+5, "m -> B4")
write_text_up(260+10+20+5+5+5+5+5+5+5+5+5+5+5, "j -> Bb4")

write_text_down(-450+10+20, "q -> C5")
write_text_down(-390+10+20+5, "w -> D5")
write_text_down(-325+10+20+10, "2 -> Db5")
write_text_down(-255+10+20+15, "e -> E5")
write_text_down(-190+10+20+20, "3 -> Eb5")
write_text_down(-120+10+20+25, "r -> F5")
write_text_down(-60+10+20+30, "t -> G5")
write_text_down(0+10+20+35, "5 -> Gb5")
write_text_down(70+10+20+40, "y -> A5")
write_text_down(130+10+20+45, "6 -> Ab5")
write_text_down(200+10+20+50, "u -> B5")
write_text_down(260+10+20+55, "7 -> Bb5")







botton1 = turtle.Turtle()
botton1.penup()
botton1.goto(-355,-200)
botton1.shape("square")
botton1.shapesize(3.75,10.5)
botton1.color("dodger blue")

label2 = turtle.Turtle()
label2.hideturtle()
label2.penup()
label2.goto(-450,-210)
label2.color("Black")
label2.write("APP CRAETORS",font=("Cascadia Code", 17))

botton2 = turtle.Turtle()
botton2.penup()
botton2.goto(-270,-200)
botton2.shape("square")
botton2.shapesize(3.75,2)
botton2.color("orange")

def one():
    y3 = turtle.Turtle()
    y3.shape("square")
    y3.shapesize(stretch_len=50,stretch_wid=30)
    y3.color("gray30")
    y3.penup()
    y3.goto(0, 0)
    
    x1 = turtle.Turtle()
    x1.hideturtle()
    x1.penup()
    x1.goto(-450,200)
    x1.color("red")
    x1.write("# MUSIC+ app creators",font=(("Dubai"),23))
    
    x2 = turtle.Turtle()
    x2.hideturtle()
    x2.penup()
    x2.goto(-480,0)
    x2.color("white")
    x2.write("     @ NOYAN GOLALIZADE      @ NIKAN NEJATIFAR",font=(("Dubai"),23))
    
    x3 = turtle.Turtle()
    x3.penup()
    x3.goto(450,250)
    x3.shape("square")
    x3.shapesize(3,3)
    x3.color("red")

    def koo2():
        y3.goto(1000,0)
        x1.clear()
        x1.write("")
        x2.clear()
        x2.write("")
        x3.goto(1000,0)
    x3.onclick(lambda x,y:koo2())        
    
botton2.onclick(lambda x, y: one())

label4 = turtle.Turtle()
label4.penup()
label4.goto(-100,-200)
label4.shape("square")
label4.shapesize(3.75,8)
label4.color("dodger blue")

label5 = turtle.Turtle()
label5.hideturtle()
label5.penup()
label5.goto(-170,-210)
label5.color("Black")
label5.write("bg color",font=("Cascadia Code", 17))

botton3 = turtle.Turtle()
botton3.penup()
botton3.goto(-40,-200)
botton3.shape("square")
botton3.shapesize(3.75,2)
botton3.color("orange")


def koo():
    x10 = turtle.textinput("backgraound custumization","put your color name or code here!")
    screen.bgcolor(x10)   
botton3.onclick(lambda x,y:koo())

# Start listening
screen.listen()
turtle.done()