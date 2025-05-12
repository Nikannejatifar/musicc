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
    turtle.speed(10)      
# رسم مستطیل اول (47 در 157)  


# فاصله دادن تا مستطیل بعدی (مثلاً کمی کنار)  

# رسم مستطیل دوم (25 در 109)  


# White keys 
white_keys_positions = [-385, -330, -275, -220, -165, -110, -55, 0, 55, 110, 165, 220, 275, 330]  
for x in white_keys_positions:  
    draw_rectangle(x, -10, 157, 47, "#D9D9D9")  

# black keys 
black_keys_positions = [-350, -287, -160, -151+25, -117+25, -350+385, -287+385, -160+385, -151+385+25, -117+385+25]  
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

screen.onkeypress(lambda: play_sound('C4'), "e")
screen.onkeypress(lambda: play_sound('C4'), "E")
screen.onkeypress(lambda: play_sound('D4'), "r")
screen.onkeypress(lambda: play_sound('D4'), "R")
screen.onkeypress(lambda: play_sound('Db4'), "4")
screen.onkeypress(lambda: play_sound('Db4'), "4")
screen.onkeypress(lambda: play_sound('E4'), "t")
screen.onkeypress(lambda: play_sound('E4'), "T")
screen.onkeypress(lambda: play_sound('Eb4'), "5")
screen.onkeypress(lambda: play_sound('Eb4'), "5")
screen.onkeypress(lambda: play_sound('F4'), "y")
screen.onkeypress(lambda: play_sound('F4'), "Y")
screen.onkeypress(lambda: play_sound('G4'), "u")
screen.onkeypress(lambda: play_sound('G4'), "U")
screen.onkeypress(lambda: play_sound('Gb4'), "7")
screen.onkeypress(lambda: play_sound('Gb4'), "7")
screen.onkeypress(lambda: play_sound('A4'), "i")
screen.onkeypress(lambda: play_sound('A4'), "I")
screen.onkeypress(lambda: play_sound('Ab4'), "8")
screen.onkeypress(lambda: play_sound('Ab4'), "8")
screen.onkeypress(lambda: play_sound('B4'), "o")
screen.onkeypress(lambda: play_sound('B4'), "O")
screen.onkeypress(lambda: play_sound('Bb4'), "9")
screen.onkeypress(lambda: play_sound('Bb4'), "9")

# Create info panel
panel = turtle.Turtle()
panel.speed(0)
panel.penup()
panel.goto(335, -10)
panel.shape("square")
panel.shapesize(stretch_len=13, stretch_wid=21)
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

title = create_label(335, 150, "")
title.write("PIANO TUTORIAL KEYS", align="center", font=("impact", 20))

key_bindings = [
    ("z", "C5"), ("x", "D5"), ("s", "Db5"), ("c", "E5"),
    ("d", "Eb5"), ("v", "F5"), ("b", "G5"), ("g", "Gb5"),
    ("n", "A5"), ("h", "Ab5"), ("m", "B5"), ("j", "Bb5")
]

y_pos = 120
for key, note in key_bindings:
    label = create_label(335, y_pos, "")
    label.write(f"button {key} = {note}", align="center", font=("Bookman Old Style", 20))
    y_pos -= 30

# Start listening
screen.listen()
turtle.done()