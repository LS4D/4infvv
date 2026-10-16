import turtle
import math
import random

# Scherm instellen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Python Cyber-Tunnel Effect")
screen.tracer(0)  # Schakel automatische updates uit voor supervloeiende animatie

# De 'pen' instellen
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)

# Kleurenpalet
colors = ["#FF0055", "#00FFCC", "#0099FF", "#FF9900", "#CC00FF", "#FFFF00"]

angle = 0

def draw_cyber_pattern():
    global angle
    pen.clear()
    
    # Gebruik de muispositie om de vorm dynamisch te vervormen
    mouse_x, mouse_y = screen.cv.winfo_pointerx() - screen.window_width() // 2, \
                      -(screen.cv.winfo_pointery() - screen.window_height() // 2)
    
    factor = max(1, abs(mouse_x) / 50 + 1)
    
    # Teken 36 roterende polygonen die een 3D-diepte-effect creëren
    for i in range(36):
        pen.penup()
        pen.goto(0, 0)
        pen.pendown()
        
        # Selecteer kleur op basis van de lus
        pen.color(colors[i % len(colors)])
        pen.pensize(2)
        
        # Bepaal hoek en straal
        rad = math.radians(i * 10 + angle)
        size = 50 + math.sin(math.radians(angle * 2 + i * 10)) * 40
        
        # Teken een hypnotiserend patroon
        for _ in range(4):
            pen.forward(size * factor)
            pen.right(90)
            pen.circle(size / 2, 90)
        
        pen.right(10)

    angle += 3
    screen.update()
    
    # Blijf de animatie continu herhalen (60 FPS)
    screen.ontimer(draw_cyber_pattern, 16)

# Start de animatielus
draw_cyber_pattern()

# Sluit het venster bij een klik
screen.exitonclick()
