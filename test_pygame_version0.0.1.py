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
def create_white_key(x, y):
    key = turtle.Turtle()
    key.speed(0)
    key.penup()
    key.goto(x, y)
    key.shape("square")
    key.shapesize(stretch_wid=10, stretch_len=4)
    key.color("white")

def create_black_key(x, y):
    key = turtle.Turtle()
    key.speed(0)
    key.penup()
    key.goto(x, y)
    key.shape("square")
    key.shapesize(stretch_wid=6, stretch_len=2)
    key.color("#323731")

# White keys
white_positions = [-400, -311, -222, -133, -44, 45, 134]
for x in white_positions:
    create_white_key(x, 0)

# Black keys
black_positions = [-355, -265, -85, 0, 90]
for x in black_positions:
    create_black_key(x, 40)

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